from config import Config
from .base_model import BaseModel
import keras


class DNN(BaseModel):
    def __init__(self):
        super().__init__()

    def get_model(self, path=None):
        if path is None:
            path = Config.DNN_MODEL_PATH
        return keras.models.load_model(path)