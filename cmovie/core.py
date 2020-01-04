# Tools for cinema_movie application

import yaml
import sys
import cv2

################## Greet users #################################
def hello():
    sys.stdout.write ('{}\n'.format("Let's make a Cinema movie") )

################## Get parameters for movie ####################
def get_params(file = 'movie.yaml'):
    with open(file, 'r') as file:
        try:
            return yaml.full_load(file)
        except yaml.YAMLError as exc:
            sys.stderr.write ('YAML file error: {}\n'.format(exc))

################## Make the movie ####################
def output_movie(name, fps, path, df) :
    fr_array = []
    files = df['FILE'].to_numpy()

    for i in range(len(files)):
        filename = path + files[i]
        img = cv2.imread(filename)
        if img is not None:
            height, width, layers = img.shape
            size = (width,height)
            #inserting the frames into an image array
            fr_array.append(img)
        else :
            sys.stderr.write ( 'WARNING skipping missing image: {}\n'.format(filename))

    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(fr_array)):
        out.write(fr_array[i])

    out.release()
