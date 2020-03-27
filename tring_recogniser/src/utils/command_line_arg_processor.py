import sys, argparse





class CommandLineArgProcessor:
    def __init__(self, argvs):
        self.inputfile = None

        parser = argparse.ArgumentParser(description='Recognise start and end of Tring sound in a call recording')
        parser.add_argument('--input', 
                        help='--Path of input file')

        if len(argvs) == 0:
            parser.print_help()
        else:
            args = vars(parser.parse_args(argvs))
            self.inputfile = args['input']
        

    
    def get_input(self):
        return self.inputfile