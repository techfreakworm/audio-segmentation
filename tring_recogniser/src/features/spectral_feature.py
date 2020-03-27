from .base_feature import BaseFeature
import numpy as np
import librosa


class SpectralFeature(BaseFeature):
    def __init__(self):
        super().__init__()

    def extract(self, audio_chunk: np.ndarray, sampling_rate: int):
        x  = audio_chunk.copy()
        sr = sampling_rate
        chroma_stft = librosa.feature.chroma_stft(y=x, sr=sr)
        chroma_cens = librosa.feature.chroma_cens(y=x, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=x, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=x, sr=sr)
        spec_cont = librosa.feature.spectral_contrast(y=x, sr=sr)
        spec_flat = librosa.feature.spectral_flatness(y=x)
        rolloff = librosa.feature.spectral_rolloff(y=x, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(x)
        mfcc = librosa.feature.mfcc(y=x, sr=sr)
        rms = librosa.feature.rms(y=x)
        poly = librosa.feature.poly_features(y=x,sr=sr)
        tonnetz = librosa.feature.tonnetz(y=x,sr=sr)
        chroma_cqt = librosa.feature.chroma_cqt(y=x, sr=sr)
        to_append = f'{np.mean(chroma_stft)} {np.mean(chroma_cqt)} {np.mean(chroma_cens)} {np.mean(rms)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(spec_cont)} {np.mean(spec_flat)} {np.mean(rolloff)} {np.mean(zcr)} {np.mean(poly)} {np.mean(tonnetz)}'    
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        return np.array(to_append.split())