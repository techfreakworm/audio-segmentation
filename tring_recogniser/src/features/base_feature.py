from abc import ABC, abstractmethod
import numpy as np


class BaseFeature(ABC):
    """Base class for all classes in 'feature' module"""    
    def __init__(self):
        """Default constructor"""        
        pass

    @abstractmethod
    def extract(self, audio_chunk: np.ndarray):
        """Abstract method for child classes to override
        
        Arguments:
            audio_chunk {np.ndarray} -- Audio chunk loaded from audio processing lib
        """        
        pass
