# cinema_movie

This repository is for python scripts used to make movies from Cinema databases.

## Requirements

- python 3.7 or later
- pandas, numpy, openCV-python installed

## Files

```
cinema_movie - main program
cmovie - movie production module
```

The **cinema_movie** script takes in a Cinema database (CDB) and creates a movie based on the set of frames given in the frames.csv file.  The movie will use the order of frames given in the frames.csv file.  Control is through command line arguments.   The cmovie module contains the functions needed to create the movie.  

## Control Parameters
The control parameters are given as options on the command line:

```
  cdb:    Set input path and Cinema database name (default: ./data/example_data.cdb)
  frames: Set input csv file name to choose views in the movie; assumes path is cdb (default: ./data/example_data.cdb/frames.csv)
  FILE:   Set the image column used from the CDB (default: FILE)
  fps:    Set the frame rate for the movie (default: 5 fps)
  opath:  Set/creates path to output movie (default: ./)
  movie:  Set output movie name (default: cinema.mp4)

```

There are error checks on the path, the Cinema database name, the frames.csv file and to verify the columns that will be used in the movie.  If the output movie path does not exist, it will be created.  If there are no images found that satisfy the requested movie parameters, a warning message will print.  

## Usage

Edit a frames.csv file to define the list of images that will be used to create the movie.  Edit the FILE variable if using a different FILE column of images.

Make a movie by running the script with optional command arguments

```
./cinema_movie --fps 10 --path ./tmp --cdb "my.cdb"

```

### Note on fps
Occasionally the movie will be generated without error and the images will appear correctly for some fps values, but the images will not appear correctly for other fps values.   Example: for the example_data.cdb, fps=2 produces a movie with images that have obvious color errors.  This phenomenon is not yet understood.

### ToDo

Need to set up the use case of a single view (defined by set of parameter values) going over all values of another parameter, e.g. over time.  
