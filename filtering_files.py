
import pandas as pd

def classes(txt_file):
    files = pd.read_csv(txt_file, delim_whitespace=True)

    files.columns = ['filename', 'class']
    class_ = files.where(files['class'] == 1)
    class_ = class_.dropna().iloc[300:400]
    class_ = class_.drop(columns=['class'])
    return class_.to_csv('class1.csv', sep=',', index=False, header=False)
