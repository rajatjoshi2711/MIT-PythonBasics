# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:24:37 2018

@author: Rajat
"""

import pandas as pd

data = [['A',10],['B',12],['C',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)