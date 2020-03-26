from features import SpectralFeature
from files import AudioFileManager
from models import DNN
from scalers import NormalisedScaler



minus_i = 0
for i in range(44100,len(y1[:40*sr,]), 44100):
    chunk = y1[minus_i:i,]
#     print(chunk)
    print(f'{minus_i/44100} to {i/44100}:', model.predict_classes(scale_features([extract_features(chunk, 44100)])))
    minus_i = i