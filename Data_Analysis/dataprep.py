#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:09:35 2018

@author: Nathan


The goal of this file is to provide an efficent and 
reproducable method of cleaning micro-CT data

The functionality will include: 
    - reading data
    - removing error values
    - organising into concise dataframes
"""


from glob import glob
from os.path import basename, dirname
import pandas as pd
import numpy as np

def gather_data(folder):
    """
    this function gathers together all
    the data of interest
    @param folder is a starting folder
    @returns tuple of (seed files, rachis files)
    """
    #check the end of the folder has a '/'
    if folder[-1] != '/':
        folder = folder + '/'
    search_params = '{0}*/*.csv'
    candidate_files = glob(search_params.format(folder))
    # we aren't bothered about the raw files so lets remove them
    candidate_files = [f for f in candidate_files if 'raw' not in f]
    # now let's separate out the rachis
    rachis = [f for f in candidate_files if 'rachis' in f]
    # and just assume the rest is what we want 
    candidate_files = [f for f in candidate_files if 'rachis' not in f]
    return (candidate_files, rachis)

def make_dataframe(grain_files, rachis_files=None):
    """
    this function returns a dataframe of 
    grain parameters and optionally of the rachis top and bottom
    @param grain_files is the output from gather_data
    @param rachis_files is an optional output from gather_data also
    
    @returns a dataframe of the information pre-joining
    """
    # load the files as dfs 
    dfs = {f:pd.read_csv(f) for f in grain_files}
    # load the files for rachis too
    if rachis_files:
        rachis = {f:pd.read_csv(f) for f in rachis_files}
    # add plant name to files 
    # and rachis if applicable 
    for k, v in dfs.items():
        # Grab the plant name and the folder name 
        v['scanid'] = basename(k).split('.',1)[0]
        v['folderid'] = dirname(k).rsplit('/',1)[-1]
        if rachis_files:
            # reverse the rachis here so we don't have to later
            v['rbot'] = rachis['{0}-rachis.csv'.format(k[:-4])]['rtop'][0]
            v['rtop'] = rachis['{0}-rachis.csv'.format(k[:-4])]['rbot'][0]
    #Flip the scans so that the Z makes sense
    df = pd.concat(dfs.values())
    df['z'] = abs(df['z'] - df['z'].max())
    
    return df  
    



def remove_percentile(df, column):
    P = np.percentile(df[column], [10, 90])
    return df[(df[column] > P[0]) & (df[column] < P[1])]

def join_spikes(grain_df, excel_file, join_column):
    """
    This function should do something akin to joining spikes based
    on a config file
    
    @note there is some confusion in the NPPC about whether to use 
    folder name or file name as the unique id when this is made into 
    end-user software, a toggle should be added to allow this
    """
    
    info_file = pd.read_excel(excel_file)

    