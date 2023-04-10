#!/usr/bin/env python3

import os
import sys
from network import callGPT
from configparser import ConfigParser

def main():

    DATA = {}
    cg = ConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = "settings/settings.ini"
    settings_file_path = os.path.join(dir_path, 'settings', 'settings.ini')
    cg.read(settings_file_path)
    print(settings_file_path)

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