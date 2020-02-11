from configparser import ConfigParser
import os

def get_config(file):
    dir = os.path.dirname(os.path.realpath(__file__))
    parser = ConfigParser()
    parser.read('{}/resources/{}'.format(dir,file))
    return parser


print(get_config('titanic.cfg')['DEFAULT']['dir_raw'])





