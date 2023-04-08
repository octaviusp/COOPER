import sys
from network import callGPT
from configparser import ConfigParser

def main():

    DATA = {}
    
    cg = ConfigParser()
    cg.read("./settings/settings.ini")
    
    DATA['MODEL'] = cg.get('CONFIG', 'MODEL')
    DATA['TEMPERATURE'] = cg.getfloat('CONFIG', 'TEMPERATURE')
    DATA['MAX_TOKENS'] = cg.getint('CONFIG', 'MAX_TOKENS')
    DATA['RESPONSES'] = cg.getint('CONFIG', 'RESPONSES')
    DATA['VOICE'] = cg.getboolean('CONFIG', 'VOICE')

    prompt = " ".join(sys.argv[1:])
    if prompt and DATA:
            callGPT.promptDataToGPT(prompt, DATA)
    else:
        print(f"\n [COOPER] - Please provide an action to perform and config settings correctly. \n")
    
if __name__ == "__main__":
    main()