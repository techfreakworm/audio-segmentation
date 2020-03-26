from .base_feature import BaseFeature
import numpy as np
import librosa


class SpectralFeature(BaseFeature):
    def __init__(self):
        super().__init__()

    def extract(self, audio_chunk: np.array, sampling_rate: int):
        y  = audio_chunk
        sr = sampling_rate
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=sr)
        chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        spec_cont = librosa.feature.spectral_contrast(y=y, sr=sr)
        spec_flat = librosa.feature.spectral_flatness(y=y)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        rms = librosa.feature.rms(y=y)
        poly = librosa.feature.poly_features(y=y,sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y,sr=sr)
        to_append = f'{np.mean(chroma_stft)} {np.mean(chroma_cqt)} {np.mean(chroma_cens)} {np.mean(rms)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(spec_cont)} {np.mean(spec_flat)} {np.mean(rolloff)} {np.mean(zcr)} {np.mean(poly)} {np.mean(tonnetz)}'    
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        return np.array(to_append.split())