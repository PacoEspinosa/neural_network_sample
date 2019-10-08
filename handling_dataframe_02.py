# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:04:27 2019

@author: Francisco Espinosa
"""
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Open database connection / 34.194.95.85
db = pymysql.connect("192.168.0.34","root","Alb3rt-31nstein","pronosticos" )
#db = pymysql.connect("34.194.95.85","root","Alb3rt-31nstein","pronosticos" )

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# initialize variables/params
prediccion = 3000
tipo_juego = 'melate'

#create query
#X_ind = [0,2,4,8,12]

#data_source = "select media, desviacion, Latencia, MinLat, "
#data_source += " MaxLat, Inercia_prom, Inercia_extremo, Esperanza_1, level, position"
#data_source += " from Indice_centralidad where Tipo_juego = '" + tipo_juego + "' and Concurso = " + str(prediccion) + ';'
'''
>Min_concurso - 0
>media - 2
>Desviacion - 4
>latencia - 5
>inercia_prom - 8
>position - 12
'''

data_source = "select MinConcurso, media, desviacion, Latencia, position"
data_source += " from Indice_centralidad where Tipo_juego = '" + tipo_juego + "' and Concurso = " + str(prediccion) + ';'

# execute SQL query using execute() method.
#cursor.execute(data_source)

# Fetch whole dataset method.
X_df = pd.read_sql(data_source, db)

#X_df = pd.DataFrame(df)
X_corr = X_df.corr()
X_corr_mark = X_corr[X_corr >0.5]

# Generate a mask for the upper triangle
mask = np.zeros_like(X_corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(X_corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot= True)

ax = sns.heatmap(
    X_corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
        
X_ind = X_df[[0,2,4,8,12]]
X_corr = X_ind.corr()
