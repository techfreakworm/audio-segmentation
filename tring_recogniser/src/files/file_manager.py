from abc import ABC, abstractmethod


class FileManager(ABC):
    """Base class for all classes in 'files' module"""
    def __init__(self):
        """Default constructor"""        
        pass

    @abstractmethod
    def load(self, path=None):
        """Load method to load file
        
        Keyword Arguments:
            path {str} -- Path of file to load (default: {None})
        """        
        pass