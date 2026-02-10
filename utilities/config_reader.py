import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

def get_base_url():
    return config["API"]["base_url"]
