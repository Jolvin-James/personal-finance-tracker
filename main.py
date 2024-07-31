import pandas as pd #allow us to load in the csv file
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:  #a class is created so to work easily with the csv file
    #to initialize a csv file:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

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
    
    #give us all of the transactions within a date range.
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        #we're going to convert all of the dates inside of the date column to a date time object, 
        #so that we can actually use them to kind of filter by different transactions
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        #here we are taking the dates as string and parsing them as date object -> strptime
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        #now we'll create a mask:
        #mask is something that we can apply to the different rows inside of our data frame to see if we should select that row or not.
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        #checking if the data in the current row in the column date is greater than the start date, 
        #and if the data or the date in the current row that we're looking at is less than or equal to the ending
        filtered_df = df.loc[mask] #locating(loc) all of the different rows where this mask matches

        if filtered_df.empty:
            print("No transactions found in the given data range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters= {"date":lambda x : x.strftime(CSV.FORMAT)}))
            #So we put the column name as the key. And then we put a function that we want to apply to every single element inside of that column
            #formatters is to specify if we want to format any specific column.

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total_expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income-total_expense):.2f}")

        return filtered_df
                  

#we're going to write a function here that will call data_entry functions in the order that we want in order to collect our data
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

#CSV.initialize_csv()
CSV.get_transactions("19-07-2024", "21-07-2024")
#add()