from abc import ABC, abstractmethod
import numpy as np


class BaseScaler(ABC):
    """Base class for all Scalers in 'scalers' module"""
    def __init__(self):
        """Default constructor"""
        pass

    @abstractmethod
    def __get_scaler__(self, path=None):
        """Get scaler
        
        Keyword Arguments:
            path {str} -- File to load (default: {None})
        """        
        pass

    @abstractmethod
    def scale_features(self, features: np.ndarray):
        """Scale features
        
        Arguments:
            features {np.ndarray} -- Scaled features
        """        
        pass