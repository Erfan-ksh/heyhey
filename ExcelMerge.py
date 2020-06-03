import pandas as pd
import os

excels_location = 'D:/Games/excelfiles/'

excel_formats = ['.xlr', '.xlw', '.xla', '.xlam', '.xml', '.xls',
                 '.xlt', '.xls', '.xltm', 'xltx', '.xlsb', '.xlsm', 'xlsx']

files_tedad = []

for filename in os.listdir(excels_location):
    if filename.endswith(tuple(excel_formats)):
        files_tedad.append(excels_location+filename)

files_readshode = [pd.read_excel(i) for i in files_tedad]

file_head = [list(i.head()) for i in files_readshode]

list_akhar = []

for i in files_tedad:
    list_akhar.append(pd.read_excel(i)[list(pd.read_excel(i).head())])


join = pd.concat(list_akhar, ignore_index=True)

join.to_excel('output.xlsx')
