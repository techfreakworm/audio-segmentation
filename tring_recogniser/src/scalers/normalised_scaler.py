import joblib
from config import Config
from .base_scaler import BaseScaler
import numpy as np


class NormalisedScaler(BaseScaler):
    def __init__(self, path=None):
        super().__init__()
        self.scaler = self.__get_scaler__(path=path)


    def __get_scaler__(self, path: str):
        if path is None:
            path = Config.NORMALISED_SCALER_PATH
        return joblib.load(path)

    def scale_features(self, features: np.ndarray):
        return self.scaler.transform(features)