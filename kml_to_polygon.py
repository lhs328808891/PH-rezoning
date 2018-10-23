# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:21:41 2018

@author: LN043-HB
"""
import pandas as pd

from fastkml import kml

def kml_to_polygon(kml_file):
    with open(kml_file, 'rt',encoding="utf-8") as myfile:
        doc=myfile.read().encode('utf-8')
    k=kml.KML()
    k.from_string(doc)
    features = list(k.features())
    listofeatures = list(features[0].features())
    polygon_df = pd.DataFrame(columns=['name','polygon'])
    for shape in listofeatures:
        try:
            polygon_df=polygon_df.append({'name':shape.name,'polygon':shape.geometry},ignore_index=True)
        except:
            pass
    return polygon_df