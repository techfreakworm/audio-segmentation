from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_model(self, path=None):
        return path