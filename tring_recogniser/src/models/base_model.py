from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Base class for all classes in 'models' module"""
    def __init__(self):
        """Default constructor"""
        pass

    @abstractmethod
    def get_model(self, path=None):
        """Get model
        
        Keyword Arguments:
            path {str} -- Get model from file (default: {None})
        """        
        pass