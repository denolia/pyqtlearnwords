
import yaml


def read_config(section):

    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    return cfg[section]
