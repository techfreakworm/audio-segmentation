from abc import ABC, abstractmethod


class BaseScaler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_scaler(self, path=None):
        return path