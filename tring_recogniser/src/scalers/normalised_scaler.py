import joblib
from config import Config
from .base_scaler import BaseScaler

class NormalisedScaler(BaseScaler):
    def __init__(self):
        super().__init__()

    def get_scaler(self, path=None):
        if path is None:
            path = Config.NORMALISED_SCALER_PATH
        return joblib.load(path)