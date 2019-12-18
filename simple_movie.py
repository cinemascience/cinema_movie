#! /usr/bin/env python
# Code to take in a Cinema database and make a movie from it.
#
# Developer: Terry Turton, Los Alamos National Laboratory
#

import cv2
import numpy as np
import pandas as pd
import os, sys
import yaml

### Setup ####

with open(r'movie.yaml') as file:
    movie_params = yaml.full_load(file)

# Read in data.csv and sort by column of interest
pathIn = './data/' + movie_params.get("cdb_name") + '/'
csv_filename = pathIn + 'data.csv'

dfCDB = pd.read_csv(csv_filename, sep=',')
cdbCols = list(dfCDB.columns)


control_var = movie_params.get("frame_var")
sys.stdout.write ( 'Control Variable: {}\n'.format(control_var))
dfCDB.sort_values(by=control_var, axis=0, ascending=True, inplace=True, kind='quicksort', na_position='last')

outputMovie =  movie_params.get("movie_name")
fps = movie_params.get("frame_rate")

frame_array = []
files = dfCDB['FILE'].to_numpy()

for i in range(len(files)):
    filename = pathIn + files[i]
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    #inserting the frames into an image array
    frame_array.append(img)

out = cv2.VideoWriter(outputMovie, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

for i in range(len(frame_array)):
    out.write(frame_array[i])

out.release()