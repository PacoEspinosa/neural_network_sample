# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:00:56 2019

@author: Francisco Espinosa
"""
import pandas as pd

X_df = pd.DataFrame(X)
X_corr = X_df.corr()
X_corr_mark = X_corr >0.5
type(X_corr_mark)
X_corr_mark.iloc[10,:]
X_ind = X_df[X_corr_mark[:,12]]
