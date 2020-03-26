import sys, argparse





class CommandLineArgProcessor:
    def __init__(self, argvs):
        self.inputfile = None
        self.outputfile = None

        parser = argparse.ArgumentParser(description='Recognise start and end of Tring sound in a call recording')
        parser.add_argument('--output',
                        help='Path of output file')
        parser.add_argument('--input', 
                        help='--Path of input file')

        if len(argvs) == 0:
            parser.print_help()
        else:
            args = vars(parser.parse_args(argvs))
            self.inputfile = args['input']
            self.outputfile = args['output']
        

    
    def get_io(self):
        return self.inputfile, self.outputfile