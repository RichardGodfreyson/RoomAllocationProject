import json
import pandas as pd

def readStudentData(path):
    '''
    reads the school student data from path (str)
    outputs a json-like data structure for data storage
    '''
    rawStudentData = pd.read_excel(path)
