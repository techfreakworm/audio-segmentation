from abc import ABC, abstractmethod


class FileManager(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load(self, path=None):
        pass