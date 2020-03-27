from .file_manager import FileManager
from config import Config
import librosa



class AudioFileManager(FileManager):
    """Manage Audio files"""    
    def __init__(self):
        """Default constructor"""
        super().__init__()

    def load(self, path=None, sampling_rate=Config.SAMPLING_RATE) -> tuple:
        """Load an audio file
        
        Keyword Arguments:
            path {str} -- Path of file (default: {None})
            sampling_rate {int} -- Sampling rate to keep (default: {Config.SAMPLING_RATE})
        
        Returns:
            tuple -- Tuple containing file data and sampling rate
        """        
        import warnings
        warnings.simplefilter("ignore")
        file_data, sr = librosa.load(path=path, sr=sampling_rate)
        return file_data, sr
        