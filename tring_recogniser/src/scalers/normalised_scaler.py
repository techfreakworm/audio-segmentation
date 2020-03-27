import joblib
from config import Config
from .base_scaler import BaseScaler
import numpy as np


class NormalisedScaler(BaseScaler):
    """Normalised scaler pre fit with data"""

    def __init__(self, path=None):
        """Constructor for NormalisedScaler
        
        Keyword Arguments:
            path {str} -- Path of scaler file saved with joblib
        """        
        super().__init__()
        self.scaler = self.__get_scaler__(path=path)


    def __get_scaler__(self, path: str):
        """Get scaler saved into file
        
        Arguments:
            path {str} -- Path of file
        
        Returns:
            StandardScaler -- StandardScaler from scikit learn
        """        
        if path is None:
            path = Config.NORMALISED_SCALER_PATH
        return joblib.load(path)

    def scale_features(self, features: np.ndarray) -> np.ndarray:
        """Scale features
        
        Arguments:
            features {np.ndarray} -- Array of features
        
        Returns:
            numpy.ndarray -- Scaled Features
        """        
        return self.scaler.transform(features)        