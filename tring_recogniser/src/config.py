import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DNN_MODEL_PATH = os.getenv('DNN_MODEL_PATH')
    NORMALISED_SCALER_PATH = os.getenv('NORMALISED_SCALER_PATH') 
