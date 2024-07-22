#this file is created to take data from the cli and all the related functions related to that
from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E" : "Expense"}

def get_date(prompt, allow_default=False):
#prompt is what we're going to ask the user to input before they give us the date.
#The reason why I'm doing this is that we can be getting the date in multiple 
#different places, and we may be asking for the date for a different reason.
#allow default is going to tell us if we should have the default value of today's date.
#The reason why I'm doing this is I want someone to be able to just hit enter, and by default it will just select the current date so they don't need to enter the date
#if the date is today, because that's probably a common, entry method using today's date.
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)    #here we create a date object
        return valid_date.strftime(date_format)  
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)  #this is recursive function as it calls the get_date function again
    

def get_amount():
    try: 
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income and 'E' for Expense.): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income and 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")