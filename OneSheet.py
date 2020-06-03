import pandas as pd
import os

excels_location = 'D:/Games/excelfiles/'

excel_formats = ['.xlr', '.xlw', '.xla', '.xlam', '.xml', '.xls',
                 '.xlt', '.xls', '.xltm', 'xltx', '.xlsb', '.xlsm', 'xlsx']


files_tedad = []

for filename in os.listdir(excels_location):
    if filename.endswith(tuple(excel_formats)):
        files_tedad.append(excels_location+filename)

for i in files_tedad:
    df = pd.concat(pd.read_excel(i, sheet_name=None), ignore_index=True)
    df.to_excel(i)