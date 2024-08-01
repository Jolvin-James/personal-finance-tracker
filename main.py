import pandas as pd #allow us to load in the csv file
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt

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
        df = pd.read_csv(cls.CSV_FILE, skipinitialspace=True)
        #we're going to convert all of the dates inside of the date column to a date time object, 
        #so that we can actually use them to kind of filter by different transactions
        # Check if the DataFrame is empty
        if df.empty:
            print("The CSV file is empty or does not contain valid data.")
            return pd.DataFrame()  # Return an empty DataFrame

        # Print the DataFrame for debugging
        print(df.head())
        print(df.columns)
        
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


def plot_transactions(df):
    df.set_index("date", inplace=True)
    #the index is the way in which we locate and manipulate different rows. 
    #So we're using the date column because that's how we want to kind of find different information.

    income_df = (df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value = 0))
    #create two separate data frames the income data frame and the expense data frame. The reason for that is 
    #that I want to have income as one line and expenses as another line.
    #D stands for daily frequency
    #we're going to take our filtered data frame with all of the transactions that we want. 
    #We're going to look at them. And we're going to make sure that we now have a row for every single day. That's what resampling is doing
    #Think of resampling as just kind of filling in all of the missing days
    #next we are summing all the amounts
    #when we reindex, we just make sure that the data frame is going to conform to this index. And we fill in any missing values with zero
    expense_df = (df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value = 0))

    plt.figure(figsize=(10, 5))
    #figure is kind of setting up the screen or the canvas where we're going to actually be putting the graph.
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    #The index means we're plotting the data pretty much
    #income_df.index -> this as the x axis value which is the date and 
    #income_df["amount"] -> the amount as the y axis value
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    while True:
        print("\n1. Add new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            #we create the df variable so as to present it on graphs
            if input("Do you wanna see a plot (y/n)?: ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()

#CSV.initialize_csv() -- in first commit
#CSV.get_transactions("19-07-2024", "21-07-2024")  -- in third commit
#add()  -- in second commit