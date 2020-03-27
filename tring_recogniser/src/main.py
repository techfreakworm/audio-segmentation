from utils import CommandLineArgProcessor
import sys


if __name__ == '__main__':
    i= CommandLineArgProcessor(sys.argv[1:]).get_input()
    from tasks import TringPredict
    TringPredict(i)
