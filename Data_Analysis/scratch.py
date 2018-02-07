"""
This file is purely for quickly prototyping
not to be released in any capacity
"""
from dataprep import gather_data, make_dataframe

# Define a few files and locations which are generally required

info_file = '../../Documents/List of primitives and synthetics final.xlsx'
prim_data_files = '../../Data/Primitives'

# load in grain and rachis files
g, r = gather_data(prim_data_files)

# create a dataframe
df = make_dataframe(g, rachis_files=r)
