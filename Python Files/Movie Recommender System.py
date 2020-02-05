# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:30:47 2020

@author: abhij
"""

import numpy as np
import zipfile
import pickle
import os

file_name='MRS.zip'

with zipfile.ZipFile(file_name, 'r') as file:
    print(file.printdir())
    
    print('Extracting all files...')
    file.extractall()
    print('Done!')

model=pickle.load(open('model.pkl',"rb"))
movie_pivot=pickle.load(open('movies.pkl',"rb"))

print("Removing Extracted file to save disk space...")
os.remove("model.pkl")
os.remove("movies.pkl")
print("Done!")

def recommend(moviename):
    
    try:
        b_id=np.where(movie_pivot.index==moviename)[0][0]
    except IndexError:
        b_id=1
    distance,suggestion=model.kneighbors(movie_pivot.iloc[b_id,:].values.reshape(1,-1),n_neighbors=5)
    if b_id!=1:
        for i in suggestion[0]:
            print(movie_pivot.index[i])
    else:
        print('Movie not found')
        
recommend('xXx: State of the Union')