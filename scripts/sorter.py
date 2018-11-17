# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:52:53 2018

@author: James
"""

from pathlib import Path
import pathlib
import os
import shutil
import pandas as pd


my_path = Path().resolve()
# =============================================================================
# pics_path = pathlib.PurePath(my_path, 'pics')
# =============================================================================
pics_path = pathlib.PurePath(r'D:\Google drive sync\unilaptop\scrappedpics')
copy_path = pathlib.PurePath(my_path, 'sorted2')

df =  pd.read_csv('clean.csv')
df['id'] = df['id'].apply(lambda x: str(x).zfill(7))
df['department'].value_counts()


def sortfile(filepath):
    table = pd.DataFrame(columns=['id','name','department'])
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.endswith(".jpg"):
                try: 
                    folder = (df.loc[df['id'] == file[1:8]]['department'].values[0])
                    os.makedirs(pathlib.PurePath(copy_path, folder), exist_ok=True)
                    path_file = pathlib.PurePath(root, file)
                    shutil.copy(path_file, pathlib.PurePath(copy_path, folder, file))
                    row = (df.loc[df['id'] == file[1:8]])
                    table = pd.concat([table,row])
                except: 
                    print (file + ' not found in csv')
    table.to_csv('sortedpics.csv', index=False)
sortfile(pics_path)

table =  pd.read_csv('sortedpics.csv')
table['department'].value_counts()
