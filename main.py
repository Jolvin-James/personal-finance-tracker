import pandas as pd #allow us to load in the csv file
import csv
from datetime import datetime

class CSV:  #a class is created so to work easily with the csv file
    #to initialize a csv file:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    #we need to create a file or read the csv file
    @classmethod #it'll have to class itself and not the instance of the class
    def initialize_csv(cls):
        try:    #if the csv file already exists then read
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:   #if the csv file doesn't exists then create one
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False) #take the above values of df and place it in csv file
    #a data frame is an object within pandas that allows us to really easily access 
    #different rows and columns from something like a CSV file.

    #add some entries into the file:
    @classmethod
    def add_entry(cls, date, amount, category, description):
        #now we use a csv writer to add into the file
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:   #here we open our csv file
            #"a" means append mode to add values to csv file
            #newline="" i dont want to add new line while opening the file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            #we are going to take a dictionary and write it onto the csv file
            writer.writerow(new_entry)
        print("Entry added succesfully.")

CSV.initialize_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")