#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:48:07 2018

@author: nathan

This file is for graphing functions that don't yet have a place
in the rest of the program
"""
import pandas as pd
import scipy.stats as stats
from scipy.stats.mstats import normaltest
import matplotlib.pyplot as plt
import numpy as np
from stats_test import qqplot
from scipy.stats import shapiro as normaltest

plt.style.use('ggplot')


def qq_grid(dataframe, attributes):
    fig, axes = plt.subplots(2,4, sharex=True, sharey=True)
    for idx, att in enumerate(attributes): 
        x = idx // 4
        y = idx % 4
        
        # Convert everything to log10 for this 
        qqplot(np.log10(dataframe[att]), plot=axes[x,y])
        axes[x,y].set_title(att)
        
        if x < 0:
            axes[x,y].set_xlabel('')
        
        if y == 0 or y == 4:
            axes[x,y].set_ylabel('Ordered Values')
        else:
            axes[x,y].set_ylabel('')
            
        axes[x,y].get_lines()[0].set_marker('o')
        axes[x,y].get_lines()[0].set_markerfacecolor('white')
        w, p = normaltest(dataframe[att])
        
        if p < 1e-2:
            p = '<0.01'
        elif p < 5e-1:
            p = '<0.05'
        else:
            p = '>0.05'
            
        axes[x,y].text(1,-6, r'$P${0}'.format(p))
    return axes