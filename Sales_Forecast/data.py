import pandas as pd
import matplotlib as plt
import numpy as np
from pandas import DataFrame, Series
import IPython
import string
import re
from datetime import datetime
 
def data_Dealer(self,self_DealerNo):
    """Find the data of the Dealer"""
    dealer_data = self[self['Dealer'] == self_DealerNo]
    return dealer_data
    #print dealer_data

def str_cut(str):
    """String segmentation"""
    item_name = re.findall(r'[A-Za-z]+(?#\d)',str)[0]
    return item_name
        
       
def data_Item(self,self_ItemNo):
    """Find the data of the Item"""
    Item_data = self[self['ITEM NO'] == self_ItemNo]
    return Item_data

def data_Date(self_series,self_Date):
    """Find the data in the Date"""
    Date_data = self_series['self_Data']
    return Date_data
    
def data_average(self):
    """Calculate the mean of the data"""
    if len(self.index) == 0:
        return 0
    else:
        return (self['EXT PRICE'].sum())/(len(self.index))
    

def data_sum(self):
    """Calculate the sum of the data"""
    return self['EXT PRICE'].sum()
