import csv
import os
import glob
import pandas as pd


def text_to_tab(path):
    os.chdir(path)
    filelist = []
    for files in glob.glob("*.txt"):
        filelist.append(os.path.basename(files))

    df_gt = pd.DataFrame()
    for file in filelist:
        frame = pd.read_csv(file,header=None,index_col=None)
        frame['filename'] = file[:].strip('.jpg.txt')
        frame['filename'] = frame['filename'].astype(str) + '.plate'
        df_gt = df_gt.append(frame)

    df_gt.columns = ('type', 'num_plate','filename','extra')
    columns1 = ['filename', 'num_plate', 'type', 'extra']
    df_gt = df_gt.reindex(columns=columns1)
    df_gt.drop(columns=['type', 'extra'], inplace=True)
    df_gt['num_plate'] = df_gt.num_plate.str.replace(' ', '')
    return df_gt.to_csv('gt.tab', header=None, sep='\t', index=None)
