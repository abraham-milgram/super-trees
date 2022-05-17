# super-trees
## Description
These programs collect and concentrate data from the 2015 new york tree census and compares it to the air quality data of uhf neighborhoods from 2015.
> _Note: uhfs is a system used to define 42 neighborhoods in New York City_  
## File Map
#### air_quality_2015.csv
This file contians the air quality data from 2015. 
- Source: https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r
#### UHF.csv
This file contains the zip codes that are within each uhf in order to find the aproximate area of the uhfs
- Source: https://www1.nyc.gov/assets/doh/downloads/pdf/ah/zipcodetable.pdf
#### 2015_Street_Tree_Census_Tree_Data.csv
This file contains the location, species, health, etc of every tree in New York City
- Source: https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh
> _Note: This file is too large to be uploaded to GitHub and is not in this repository_
#### air.csv
This file contains the data from air_quality_2015.csv compared to the area of the uhfs found in uhfProcessed.csv by UHFarea.py
#### trees.csv
This file contains the tree data concetrated to the tallies of trees in each uhf and the trees per km^2 by TreeTallies2Uhf.py
#### uhfProcessed.csv
This file contians the areas of each uhf by getting the sum of the areas of their zipcodes by UHFarea.py
#### FINAL.csv
The culmination of all of this data, comparing the density of trees found in trees.csv and the concentrating of greenhouse gasses in air.csv
