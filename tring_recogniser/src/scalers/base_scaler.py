from abc import ABC, abstractmethod
from numpy import np


class BaseScaler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __get_scaler__(self, path=None):
        pass

    @abstractmethod
    def extract_features(self, features: np.array):
        pass