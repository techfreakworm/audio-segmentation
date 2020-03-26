import joblib
from config import Config


class NormalisedScaler:
    def __init__(self):
        pass

    def get_scaler(self, path=None):
        if path is None:
            path = Config.NORMALISED_SCALER_PATH
        return joblib.load(path)