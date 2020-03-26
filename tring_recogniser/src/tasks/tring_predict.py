import logging
from files import AudioFileManager
from features import SpectralFeature
from scalers import NormalisedScaler
from models import DNN
import numpy as np
import sys


class TringPredict:
    def __init__(self, input_file: str=None, output_file: str=None):
        logging.info(f'Using input file: {input_file}')
        logging.info(f'Using output file: {output_file}')
        if output_file:
            logging.basicConfig(filename=output_file)
        try:
            audio_data, sr = self.load_audio(input_file)
            self.spectral_feature = SpectralFeature()
            self.scaler = NormalisedScaler()
            self.model = DNN().get_model()
            self.prediction_loop(audio_chunk=audio_data, sr=sr)
        except BaseException as ex:
            logging.error(str(ex))
            sys.exit(ex)




    def load_audio(self, path=None):
        return AudioFileManager().load(path)


    def get_features(self, audio_data, sr):
        return self.spectral_feature.extract(audio_chunk=audio_data, sampling_rate=sr)


    def get_scaled_features(self, features: np.array):
        return self.scaler.scale_features(features=features)


    def predict(self, scaled_features):
        return self.model.predict_classes(scaled_features)

    def prediction_loop(self, audio_chunk, sr):
        last_chunk_index = 0
        last_prediction = -1
        start_printed = False
        # According to normalised scaler '0' stands for 'Talk', '1' stands for 'Tring Tring'
        for chunk_index in range(sr, len(audio_chunk), sr):
            current_chunk = audio_chunk[last_chunk_index:chunk_index,]
            prediction = self.predict(self.get_scaled_features([self.get_features(current_chunk, sr)]))[0]
            if prediction == last_prediction:
                logging.info(f'Tring Tring ended at: {chunk_index/sr}')
                sys.exit()
            elif prediction == 1 and not start_printed:
                logging.info(f'Tring Tring started at: {chunk_index/sr}')
            last_prediction = prediction
            last_chunk_index = chunk_index
        