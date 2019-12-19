# Tools for cinema_movie application

import yaml
import sys

################## Greet users #################################
def hello():
    sys.stdout.write ('{}\n'.format("welcome to cinema_movie") )

################## Get parameters for movie ####################
def get_params(file = 'movie.yaml'):
    with open(file, 'r') as file:
        try:
            return yaml.full_load(file)
        except yaml.YAMLError as exc:
            sys.stderr.write ('YAML file error: {}\n'.format(exc))
