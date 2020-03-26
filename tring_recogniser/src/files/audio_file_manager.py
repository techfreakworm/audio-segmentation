from .file_manager import FileManager
from config import Config
import librosa


class AudioFileManager(FileManager):
    def __init__(self):
        super().__init__()

    def load(self, path=None, sampling_rate=Config.SAMPLING_RATE):
        file_data, sr = librosa.load(path=path, sr=sampling_rate)
        return file_data, sr
        