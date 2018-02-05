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
from os.path import basename
import pandas as pd

def gather_data(folder):
    """
    this function gathers together all
    the data of interest
    @param folder is a starting folder
    @returns tuple of (seed files, rachis files)
    """
    
    search_params = '{0}*/*.csv'
    candidate_files = glob(search_params.format(folder))
    # we aren't bothered about the raw files so lets remove them
    [candidate_files.remove(f) for f in candidate_files if 'raw' in f]
    # now let's separate out the rachis
    rachis = [f for f in candidate_files if 'rachis' in f]
    # and just assume the rest is what we want 
    [candidate_files.remove(f) for f in candidate_files if 'rachis' in f]
    return (candidate_files, rachis)

def make_dataframe(grain_files, rachis_files=None):
    """
    this function returns a dataframe of 
    grain parameters and optionally of the rachis top and bottom
    @param grain_files is the output from gather_data
    @param rachis_files is an optional output from gather_data also
    """
    # load the files as dfs 
    dfs = {basename(f).split('.',1)[0]:pd.read_csv(f) for f in grain_files}
    # load the files for rachis too
    if rachis_files:
        rachis = {basename(f).split('.',1)[0]:pd.read_csv(f) for f in rachis_files}
    # add plant name to files 
    # and rachis if applicable 
    for k, v in dfs.items():
        v['plantid'] = k     
        if rachis_files:
            v['rtop'] = rachis[k]['rtop'][0]
            v['rbot'] = rachis[k]['rbot'][0]
    return pd.concat(dfs.values())
    
    