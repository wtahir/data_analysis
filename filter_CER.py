import os
import pandas as pd
import csv


path = os.chdir('/home/waqas/sandbox/bas/bas1/output/open_alpr_comVersion_report/latest_result_without_emptyTags/')

def get_cer_0_fer_0(tsv_file):   
    df = pd.read_csv(tsv_file, sep='\t')
    df = df.loc[df.CER == 0.0].count(axis='rows')
    print (df)
    

def get_cerGreater_0_lessThan_Threshold(tsv_file):
    df = pd.read_csv(tsv_file, sep='\t')
    df = df.loc[(df.CER > 0.0) & (df.CER <= 25)].count(axis='rows')
    print (df)

def get_cerGreater_threshold(tsv_file):
    df = pd.read_csv(tsv_file, sep='\t')
    df = df.loc[(df.CER > 25)].count(axis='rows')
    print (df)

def get_cer0_ferGreater_0(tsv_file):
    df = pd.read_csv(tsv_file, sep='\t')
    df = df.loc[(df.CER == 0) & (df.FER > 0)].count(axis='rows')
    print (df)

