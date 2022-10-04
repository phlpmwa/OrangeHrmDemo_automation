import os
from configparser import ConfigParser

file_path = os.path.join(os.path.dirname(__file__), '..', 'configData',
                         'config.ini')


def read_config(section, key):
    config = ConfigParser()
    config.read(file_path)
    return config.get(section, key)


#print(read_config(section="site-url", key="sport_pesa_base_url"))
