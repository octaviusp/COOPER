import sys

from helpers import utils
from network import callGPT
from configparser import ConfigParser

def main():

    DATA = {}
    
    cg = ConfigParser()
    cg.read("./settings/settings.ini")
    
    DATA['MODEL'] = cg.get('CONFIG', 'MODEL')
    DATA['TEMPERATURE'] = cg.getint('CONFIG', 'TEMPERATURE')
    DATA['MAX_TOKENS'] = cg.getint('CONFIG', 'MAX_TOKENS')
    DATA['RESPONSES'] = cg.getint('CONFIG', 'RESPONSES')

    prompt = " ".join(sys.argv[1:])
    if prompt:
            callGPT.promptDataToGPT(prompt, DATA)
    else:
        print(f"\n {utils.APP_NAME} - Please provide an action to perform. \n")
    
if __name__ == "__main__":
    main()