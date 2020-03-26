from abc import ABC, abstractmethod
import numpy as np


class BaseFeature(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def extract(self, audio_chunk: np.array):
        pass
