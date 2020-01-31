# Tools for cinema_movie application

import yaml
import os, sys
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

################## Validate CDB path and filename ###############
def validatePath(file) :
    if ( not os.path.isfile(file) ) :
        sys.stderr.write ( 'ERROR Cinema database does not exist: {}\n'.format(file) )
        sys.exit("Check CDB path and name.")


################## Validate yaml control variables ##############
def validateCDB(var, file_choice, views, df) :
    if var in list(df.columns.values) : # frame control variable exists
        sys.stdout.write ( 'Using control variable: {}\n'.format(var))
        if file_choice in list(df.columns.values) : # Image column exists
            sys.stdout.write ( 'Using image column: {}\n'.format(file_choice))
            if bool(views) : # View exists
                for x in views:
                    if x not in list(df.columns.values) :
                        sys.stderr.write ('ERROR Requested view variable does not exist : {}\n'.format(x) )
                        sys.exit ("Check view variable names.")

                sys.stdout.write ('Using requested view: {}\n'.format(views))
                return True
            else:
                sys.stdout.write ('WARNING No view specified, all images in database will go into the movie. \n'.format())
        else :
            sys.stderr.write ( 'ERROR Requested FILE image column does not exist : {}\n'.format(file_choice))
            sys.exit("Check FILE image column name.")
    else :
        sys.stderr.write ( 'ERROR Requested frame control variable does not exist : {}\n'.format(var))
        sys.exit("Check frame control variable name.")

    return False

################## Make the movie ##############################
def output_movie(name, fps, whichFILE, path, df) :
    fr_array = []
    files = df[whichFILE].to_numpy()
    size = (0,0)
    
    # for i in range(len(files)):
    for f in files:
        filename = os.path.join(path, f)
        img = cv2.imread(filename)
        if img is not None:
            height, width, layers = img.shape
            size = (width,height)
            #inserting the frames into an image array
            fr_array.append(img)
        else :
            sys.stderr.write ( 'WARNING skipping missing image: {}\n'.format(filename))

    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for f in fr_array:
        out.write(f)
    # for i in range(len(fr_array)):
        # out.write(fr_array[i])

    out.release()
    sys.stdout.write ( 'Movie is in: {}\n'.format( name ))
