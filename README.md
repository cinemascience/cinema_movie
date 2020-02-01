# cinema_movie

This repository is for python scripts used to make movies from Cinema databases.

## Requirements

- python 3.7 or later
- pandas, numpy, openCV-python installed

## Files

```
cinema_movie - main program
movie.yaml - control file
cmovie - movie production module
```

The **cinema_movie** script takes in a Cinema database (CDB) and creates a movie based on the primary frame variable within the CDB.  Control is through command line arguments.  Cinema_movie can be used to create a movie over time using the frames as defined in a frames CSV file.  The cmovie module contains the functions needed to create the movie.  

## Control Parameters
The control parameters are given as options on the command line:

```

    path:   Set input path to Cinema datbase (default: ./data)
    cdb:    Set input Cinema database name (default: example_data.cdb)
    frames: Set input csv file name to choose views in the movie; assumes ./ path (default: frames.csv)
    FILE:   Set the image column used from the CDB (default: FILE)
    fps:    Set the frame rate for the movie (default: 5 fps)
    movie:  Set output movie name (default: cinema.mp4)
```


There are error checks on the path, the Cinema database name, the frames.csv file and to verify the columns that will be used in the movie.  If there are no images found that satisfy the requested movie parameters, a warning message will print.  

## Usage

Edit a frames.csv file to define the list of images that will be used to create the movie.  Edit the FILE variable if using a different FILE column of images.

Make a movie by running the script with optional command arguments

```
./cinema_movie --fps 10 --path ./tmp --cdb "my.cdb"

```
