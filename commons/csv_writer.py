import pandas as pd
from datetime import datetime

class CSVWriter:
    def __init__(self,file_name):
        self.file_name=file_name
        self.csv_input = pd.read_csv('Connections.csv')
        if 'Profile link' not in self.csv_input.columns:
            self.csv_input.insert(3, 'Phone Number', '')
            self.csv_input.insert(4, 'Description', '')
            self.csv_input.insert(4, 'Profile link', '')
            self.csv_input['Attempt Date'] = ''
            self.csv_input['Message'] = ''
            self.csv_input.to_csv(self.file_name, index=False)
        all_columns = list(self.csv_input)  # Creates list of all column headers
        self.csv_input[all_columns] = self.csv_input[all_columns].astype(str)
        self.csv_input['Attempt Date'] = pd.to_datetime(self.csv_input['Attempt Date'])

    def totalToday(self):
        count = 0
        for i in range(len(self.csv_input)):
            if self.csv_input.loc[i, 'Attempt Date'].date() == datetime.today().date():
                count += 1
        return count

    def total(self):
        count={'total':0,'done':0, 'pending':0}
        total,done,pending = 0,0,0
        for i in range(len(self.csv_input)):
            if self.csv_input.loc[i, 'Attempt Date'].date() == datetime.today().date():
                done += 1
        return done
    def read_csv(self):
        return self.csv_input
    def save_csv(self):
        self.csv_input.to_csv(self.file_name,index=False)
