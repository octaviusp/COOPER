import sys

from helpers import utils
from network import callGPT

def main():

    DATA = {}
    #if not DATA:
    #    print(f"\n {utils.APP_NAME} try to provide all required data, type --help to more info. \n")
    # Getting the prompt text to generate bash code 

    prompt = " ".join(sys.argv[1:])
    if prompt:
            callGPT.promptDataToGPT(prompt, DATA)
    else:
        print(f"\n {utils.APP_NAME} - Please provide an action to perform. \n")
    
if __name__ == "__main__":
    main()