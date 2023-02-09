import pandas as pd
import csv
import re
import os

data = pd.read_csv('amazon_order_history.csv')
pd.DataFrame(data)
data['rupees'] = data['total'].str.strip('Rs.')
print(data['rupees'])

folder = "C:\\Users\\jayam\\PycharmProjects\\face_recognition_extraction\\2023\\"

for index, file_name in enumerate(os.listdir(folder)):
    first_five_name = data['items'][index]
    print(first_five_name)
    first_five_name = re.findall(r'\w+', first_five_name)[:5]
    first_five_name = " ".join(first_five_name)
    name = data['date'][index] + "_" + data['rupees'][index] + "_" + first_five_name
    print('renaming', name)
    #for name in data['new_name']:
    source = folder + file_name
    destination = folder + name +'.pdf'
    print(source)
    print(destination)
    os.rename(source, destination)

