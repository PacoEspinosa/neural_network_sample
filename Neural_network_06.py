# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:49:50 2019

@author: fespinosa
"""

# first neural network with keras tutorial
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import pymysql
import pandas as pd
import numpy as np

# Open database connection / 34.194.95.85
db = pymysql.connect("192.168.0.34","root","Alb3rt-31nstein","pronosticos" )
#db = pymysql.connect("34.194.95.85","root","Alb3rt-31nstein","pronosticos" )

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# initialize variables/params
prediccion = 977
prediccionXp = prediccion + 1
tipo_juego = 'clasica'

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
Y_data_source = "select IFNULL(value, 0) from " 
Y_data_source += "(select distinct valor from Nvo_" + tipo_juego + " order by 1) a left join "
Y_data_source += "(select * , 1 as value from Nvo_" + tipo_juego + " where concurso = " + str(prediccion) + ") b on a.valor = b.valor "
Y_data_source += "order by a.valor;"
y = pd.read_sql(Y_data_source, db)

for i in range(3):
    if i==0:    
        X_data_source = "select valor, MinConcurso, media, desviacion, Latencia, position"
    else:
        X_data_source = "select MinConcurso, media, desviacion, Latencia, position"

    X_data_source += " from Indice_centralidad where Tipo_juego = '" + tipo_juego + "' and Concurso = " + str(prediccion) + ';'
    if i==0:
        X_df01 = pd.read_sql(X_data_source, db)
    elif i == 1:
        X_df02 = pd.read_sql(X_data_source, db)
    elif i == 2:
        X_df03 = pd.read_sql(X_data_source, db)
    
    prediccion -= ((i+1)**3-1)
#    print(prediccion,((i+1)**3-1),i)

X = pd.concat([X_df01, X_df02, X_df03], axis=1, sort=True)


# execute SQL query using execute() method.
#cursor.execute(data_source)

# Fetch whole dataset method.

#X_df = pd.DataFrame(df)
rows, column = X.shape

model = Sequential()
model.add(Dense(4, input_dim=column, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=1500, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))


for i in range(3):
    if i==0:    
        Xp_data_source = "select valor, MinConcurso, media, desviacion, Latencia, position"
    else:
        Xp_data_source = "select MinConcurso, media, desviacion, Latencia, position"

    Xp_data_source += " from Indice_centralidad where Tipo_juego = '" + tipo_juego + "' and Concurso = " + str(prediccionXp) + ';'
    if i==0:
        Xp_df01 = pd.read_sql(Xp_data_source, db)
    elif i == 1:
        Xp_df02 = pd.read_sql(Xp_data_source, db)
    elif i == 2:
        Xp_df03 = pd.read_sql(Xp_data_source, db)
    
    prediccionXp -= ((i+1)**3-1)

Xp = pd.concat([Xp_df01, Xp_df02, Xp_df03], axis=1, sort=True)

predictions = model.predict_classes(Xp)
print(predictions)