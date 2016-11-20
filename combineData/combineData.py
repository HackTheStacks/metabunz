# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:44:24 2016

@author: navrajnarula
"""

import csv
from collections import OrderedDict 


import pandas as pd
data1 = pd.read_csv("department.csv", encoding='utf-8', quotechar='"', delimiter=',') 
data2 = pd.read_csv("exhibition.csv", encoding='utf-8', quotechar='"', delimiter=',') 
data3 = pd.read_csv("expedition.csv", encoding='utf-8', quotechar='"', delimiter=',') 
data4 = pd.read_csv("person.csv", encoding='utf-8', quotechar='"', delimiter=',') 


filenames = data1, data2, data3, data4

data = OrderedDict()
fieldnames = []
for filename in filenames:
    with open(filename, "rt") as fp: 
        reader = csv.DictReader(fp)
        fieldnames.extend(reader.fieldnames)
        for row in reader:
            data.setdefault(row["exac_id"], {}).update(row)

fieldnames = list(OrderedDict.fromkeys(fieldnames))
with open("merged.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow(fieldnames)
    for row in data.itervalues():
        writer.writerow([row.get(field, '') for field in fieldnames])