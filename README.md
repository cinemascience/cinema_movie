# cinema_movie

This repository is for python scripts used to make movies from Cinema databases.  The requirements are:

- python 3.7 or later
- pyyaml, pandas, numpy installed

## Simple example:

```
simple_movie - main program
movie.yaml - control file
cmovie - movie production module
```

The **simple_movie** script takes in a Cinema database (CDB) and creates a movie based on primary frame variable within the CDB.  Control is through a human-readable YAML configuration file.  This is useful, for example, to create a movie over time for single static view as defined in the movie.yaml file.  The cmovie module contains the functions needed to create the movie.  

Usage:
Edit the movie.yaml file to point to the CDB, adjust the name of the output movie, choose movie frame rate, and choose the variable along which to make the movie.  Edit the views variable to define the single static view that will be used.  

```
$ ./simple_movie
```

# In Progress:

Development of more complex scripts to make and direct a movie along multiple axis (e.g., multiple views) is underway.  
