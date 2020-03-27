from abc import ABC, abstractmethod
import numpy as np


class BaseScaler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __get_scaler__(self, path=None):
        pass

    @abstractmethod
    def scale_features(self, features: np.ndarray):
        pass