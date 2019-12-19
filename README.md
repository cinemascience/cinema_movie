# cinema_movie

This repository is for python scripts to make movies from Cinema databases.  The requirements are:

- python 3.7 or later
- pyyaml installed

## Simple example:

```
simple_movie.py
movie.yaml
```

The simple_movie.py script takes in a Cinema database (CDB) and creates a movie based on a single variable within the CDB.  Control is through a human-readable YAML configuration file.  This is useful, for example, to create a movie over time for a static (single view) CDB.

Usage:
Edit the movie.yaml file to point to the CDB, adjust the name of the output movie, choose movie frame rate, and choose the variable along which to make the movie.    

```
$ ./simple_movie
```

# In Progress:

Development of more complex scripts to make and direct a movie both spatially and temporarily is underway.  
