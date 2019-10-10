# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:52:53 2018
This sorts the scrapped images according to their faculty
@author: James
"""

from pathlib import Path
import pathlib
import os
import shutil
import pandas as pd


def sort_files(df, scrapped_path, copy_path):
    #create table to specify the sorted pictures
    table = pd.DataFrame(columns=['id','name','department'])
    for root, dirs, files in os.walk(scrapped_path):
        for file in files:
            if file.endswith(".jpg"):
                try: 
                    #the folder corresponds to the department of the student
                    folder = (df[df['id'] == file[1:8]]['department'].values[0])
                    #make the folder in the copy path
                    os.makedirs(pathlib.PurePath(copy_path, folder), exist_ok=True)
                    #copy the photo over
                    path_file = pathlib.PurePath(root, file)
                    shutil.copy(path_file, pathlib.PurePath(copy_path, folder, file))
                    #add info 
                    info = (df[df['id'] == file[1:8]])
                    table = pd.concat([table,info])
                except: 
                    print (file + ' not found in csv')
    #output a file specifying the pictures that were able to be sorted
    table.to_csv('sortedpics.csv', index=False)
if __name__ == '__main__' :
    my_path = Path().resolve()
    pics_path = pathlib.PurePath(input("Input filepath of scrapped images"))
    copy_path = pathlib.PurePath(my_path, 'sorted_')

    df =  pd.read_csv(input("Input filepath of csv file with columns id, name, department of students))
    df['id'] = df['id'].apply(lambda x: str(x).zfill(7))
    sort_files(df, pics_path, copy_path)
