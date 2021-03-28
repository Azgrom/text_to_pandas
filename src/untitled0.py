# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:02:17 2021

@author: Rafael Lúcio
"""


import os
import datetime as dt
import pandas as pd


# Finds sample data in function of the script folder
script_directory = os.getcwd()
project_directory = os.path.abspath(os.path.join(script_directory,
                             os.pardir))

sample_data_path = f'{project_directory}/sample_data'

data_structure = {
    'title': [],
    'author': [],
    'date_published': [],
    'link': [],
    'content': []
}

# Loop over files
for root, _, files in os.walk(sample_data_path):
    for report in files:
        with open(f'{root}/{report}', 'rt') as f:
            data_structure['title'].append(f.readline())
            data_structure['author'].append(f.readline())
            data_structure['date_published'].append(f.readline())
            data_structure['link'].append(f.readline())
            data_structure['content'].append(f.readlines())


data_structure = pd.DataFrame(data_structure)
