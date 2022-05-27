import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('Utils/properties.ini')
    return config

