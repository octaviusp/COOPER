import errors
from configparser import ConfigParser

def specs():
    DATA = {}
    config = ConfigParser()
    config.read("../settings/settings.ini")
    # GET USER SETTINGS FROM THE CONFIG INI

    #string
    DATA['MODEL'] = config.get('DEFAULT', 'MODEL').lower()
    DATA['LEVEL'] = config.get('DEFAULT', 'PERMISSION_LEVEL').lower()
    #float
    DATA['TEMPERATURE'] = config.getfloat('DEFAULT', 'TEMPERATURE')
    #int
    DATA['MAX_TOKENS'] = config.getint('DEFAULT', 'MAX_TOKENS')
    DATA['RESPONSES'] = config.getint('DEFAULT', 'NUMBER_OF_RESPONSES')
    #boolean
    DATA['CODE_PREVIEW'] =  config.getboolean('DEFAULT', 'CODE_PREVIEW')

    #verifying that all fields contains a value
    for _, value in DATA.items():
        if not value:
            raise errors.settingsError()

    #returning dictionary
    return DATA