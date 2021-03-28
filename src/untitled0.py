# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:02:17 2021

@author: Rafael Lúcio
"""


import os
import datetime as dt


# Finds sample data in function of the script folder
script_directory = os.getcwd()
project_directory = os.path.abspath(os.path.join(script_directory, 
                             os.pardir))


# List every report name folder name to be treated afterwards
report_dates = os.listdir(f'{project_directory}/sample_data')

def convert_string_to_date_object(str_list, date_format):
    aux = []
    for date in str_list:
        aux.append(dt.datetime.strptime(date, date_format))
        
    return aux

report_dates = convert_string_to_date_object(report_dates, '%Y-%m-%d')