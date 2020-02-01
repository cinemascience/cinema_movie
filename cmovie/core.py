# Tools for cinema_movie application

import os, sys
import cv2

################## Greet users #################################
def hello():
    sys.stdout.write ('{}\n'.format("Let's make a Cinema movie") )

################## Validate path and filename ###############
def validateFile(file) :
    if ( not os.path.isfile(file) ) :
        sys.stderr.write ( 'ERROR file does not exist: {}\n'.format(file) )
        sys.exit("Check file path and name.")

################## Validate DFs and variables ##############
def validateDFs(dfcdb, dfframes, file_choice) :

    if file_choice in list(dfcdb.columns.values) : # Image column exists
        sys.stdout.write ( 'Using image column: {}\n'.format(file_choice))
        colCDB = list(dfcdb.columns)
        colFrames = list(dfframes.columns)
        if(all(x in colCDB for x in colFrames)):
            sys.stdout.write ('Making movie over: {}\n'.format(colFrames))
            return True
        else :
            sys.stderr.write ( 'ERROR Some requested variables do not exist in Cinema database: \n')
            sys.stderr.write ( 'Columns in Cinema database: {} \n'.format(colCDB))
            sys.stderr.write ( 'Columns in frames file:     {} \n'.format(colFrames))
            sys.exit("Check columns in your frames CSV file.")
    else :
        sys.stderr.write ( 'ERROR Requested FILE image column does not exist : {}\n'.format(file_choice))
        sys.exit("Check FILE image column name.")

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
