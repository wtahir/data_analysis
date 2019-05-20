import pandas as pd
import csv
import glob
import json
import numpy as np
import os
from shapely.geometry import Polygon
from shapely.geometry import point


def get_biggest_rect(json_file):
    poly_array = []
    for c in json_file['results']:
        points = c['coordinates']
        po_array = []

        for xydict in points:
            po = Point(xydict['x'], xydict['y'])
            po_array.append(po)
        coords = [(pi.x,pi.y) for pi in po_array]
        poly = Polygon(coords)
        poly_array.append(poly.area)

    index = np.argmax(poly_array)
    plate = json_file["results"][index]["plate"]
    conf = json_file["results"][index]["confidence"]             
    return (plate,conf) 




def json_tab(json_path):
    os.chdir(json_path)
    filelist = []
    df_predicted = pd.DataFrame()

    for files in glob.glob('*.json'):
        filelist.append(os.path.basename(files))

    for file in filelist:
        with open(file, 'r') as json_data:
            data = json.load(json_data)

            if len(data["results"]) > 0:
                plate = data["results"][0]["plate"]
                conf = data["results"][0]["confidence"]
                df_predicted = df_predicted.append({'num_plate': plate,'conf': conf, 'file_name': file.strip('.jpg.json')}, ignore_index=True)
    df_predicted_adding_plate = df_predicted['file_name'].astype(str) + '.plate'
    df_predicted['file_name'] = df_predicted_adding_plate
    return df_predicted.to_csv('json.tab', header=None, sep='\t', index=None)