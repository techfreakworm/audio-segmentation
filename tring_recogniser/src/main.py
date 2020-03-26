from utils import CommandLineArgProcessor
import sys


if __name__ == '__main__':
    i, o = CommandLineArgProcessor(sys.argv[1:]).get_io()
    from tasks import TringPredict
    TringPredict(i, o)
