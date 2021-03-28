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
sample_dates = os.listdir(f'{project_directory}/sample_data')

