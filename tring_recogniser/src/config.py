import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DNN_MODEL_PATH = os.getenv('DNN_MODEL_PATH')
    NORMALISED_SCALER_PATH = os.getenv('NORMALISED_SCALER_PATH') 
    # DNN Model has only been developed for audio with sampling rate 44100
    # All the imported are upscaled/downscaled to 44100 automatically
    SAMPLING_RATE = 44100
