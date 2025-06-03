# Creating maps of pollution over the UK

A collection of scripts to create a map
of pollution over the UK. The input is the
simulation results from 
https://uk-air.defra.gov.uk/data/pcm-data


The scripts are:

*  preprocess.py  -  converts the data to latitude and longitude. input file mapno22023.csv from the government site. Creates the file data.csv. The  osgb library converts the coordinate system (https://github.com/thruston/grid-banger).
*  create_plot.py -  creates the map from the data.csv. It was created using Gemini. The underlying library is 
  folium https://python-visualization.github.io/folium/latest/


## Final plot

The scripts produce pollution over the UK

![test](https://github.com/cmcneile/pollution_uk/blob/main/no2UK.png?raw=true)




