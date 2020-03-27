from config import Config
from .base_model import BaseModel
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import keras


class DNN(BaseModel):
    """Deep Neural Network Model"""
    def __init__(self):
        """Default constructor"""
        super().__init__()

    def get_model(self, path=None) -> keras.models.Sequential:
        """Get model
        
        Keyword Arguments:
            path {str} -- Path to model file in hdf5 format (default: {None})
        
        Returns:
            Sequential -- Keras sequential Model
        """        
        if path is None:
            path = Config.DNN_MODEL_PATH
        return keras.models.load_model(path)