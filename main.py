import pandas as pd #allow us to load in the csv file
import csv
from datetime import datetime

class CSV:  #a class is created so to work easily with the csv file
    CSV_FILE = "finance_data.csv"

    #we need to create a file or read the csv file
    @classmethod #it'll have to class itself and not the instance of the class
    def initialize_csv(cls):
        try:    #if the csv file already exists then read
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:   #if the csv file doesn't exists then create one
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False) #take the above values of df and place it in csv file
    #a data frame is an object within pandas that allows us to really easily access 
    #different rows and columns from something like a CSV file.

    #add some entries into the file

CSV.initialize_csv()