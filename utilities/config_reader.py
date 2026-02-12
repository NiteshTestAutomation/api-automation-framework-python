import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")

config.read(config_path)

def get_base_url():
    return config['API']['base_url']

def get_object_base_url():
    return config['API']['restfull_base_url']