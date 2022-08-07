# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:11:57 2022

@author: Vishnu Thirumurugan
"""

# creating an array

import numpy as np
array_an = np.arange(1,100,5).reshape(2,10) 
print(array_an)


# extracting csv file from numpy using dataframe  (pandas)

import pandas as pd
data_frame = pd.DataFrame(array_an)     # converting array to dataframe
data_frame.to_csv("Data1.csv")          # extracting to csv
