from .file_manager import FileManager
import librosa


class AudioFileManager(FileManager):
    def __init__(self):
        super().__init__()

    def load(self, path=None, sampling_rate=44100):
        file_data, sr = librosa.load(path=path, sr=sampling_rate)
        return file_data, sr
        