from files import AudioFileManager
from features import SpectralFeature
from scalers import NormalisedScaler
from models import DNN
import numpy as np
import sys


class TringPredict:
    def __init__(self, input_file: str=None):
        print(f'Using input file: {input_file}')
        try:
            audio_data, sr = self.load_audio(input_file)
            self.spectral_feature = SpectralFeature()
            self.scaler = NormalisedScaler()
            self.model = DNN().get_model()
            self.prediction_loop(audio_chunk=audio_data, sr=sr)
        except BaseException as ex:
            print(str(ex))




    def load_audio(self, path=None):
        return AudioFileManager().load(path)


    def get_features(self, audio_data, sr):
        return self.spectral_feature.extract(audio_chunk=audio_data, sampling_rate=sr)


    def get_scaled_features(self, features: np.ndarray):
        return self.scaler.scale_features(features=features)


    def predict(self, scaled_features):
        return self.model.predict_classes(scaled_features)

    def prediction_loop(self, audio_chunk, sr):
        last_chunk_index = 0
        start_printed = False
        last_tring_time = -1
        talk_pred_list = list()
        # According to normalised scaler '0' stands for 'Talk', '1' stands for 'Tring Tring'
        for chunk_index in range(sr, len(audio_chunk), sr):
            current_chunk = audio_chunk[last_chunk_index:chunk_index,]
            prediction = self.predict(self.get_scaled_features([self.get_features(current_chunk, sr)]))[0]
            if prediction == 1 and not start_printed:
                print(f'Tring Tring started at: {chunk_index/sr}s')
                start_printed=True
            elif prediction == 0:
                talk_pred_list.append(0)
            elif prediction == 1:
                last_tring_time = chunk_index/sr
                talk_pred_list = list()
            if len(talk_pred_list)>1:
                print(f'Tring Tring ended at: {last_tring_time}s')
                break
            last_chunk_index = chunk_index
        