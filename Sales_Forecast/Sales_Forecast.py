import data
import machine_learning
import pandas as pd
import matplotlib as plt
import numpy as np
from pandas import DataFrame, Series
import IPython
import re
from datetime import datetime
import time

xls_file = pd.read_table("C:/analysis/sales list3.txt")
#read the file 
data_1316 = DataFrame(xls_file)
length = len(data_1316.index)

for i in range(0,length):
    data_1316.ix[i,'ITEM NO'] = data.str_cut(data_1316.ix[i,'ITEM NO'])
    data_1316.ix[i,'SCH_DATE'] = datetime.strptime(data_1316.ix[i,'SCH_DATE'], "%Y/%m/%d %H:%M")
    i = i+1
#1-cut all items NO. to find the truely items classic without number.
#2-change the time class from str to datetime

#data_2013 = data_2013.set_index(['SCH_DATE'])
#change the DataFrame index from num to SCH_DATE
i=1
for sample in data_1316['ITEM NO'].unique():
    #sales_data = data.data_Item(data_2013,sample)
    print i  , sample
    i = i+1

print length
    