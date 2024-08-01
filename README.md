# README

## Personal Finance Tracker

This is a simple command-line application for tracking personal finances. It allows users to log transactions, view summaries, and visualize income and expenses over a specified date range. The data is stored in a CSV file, making it easy to manage and analyze.

### Features

- **Add Transactions**: Log income and expenses with date, amount, category, and an optional description.
- **View Transactions**: Retrieve and display transactions within a specified date range, along with a summary of total income, expenses, and net savings.
- **Visualize Data**: Generate line plots to visualize income and expenses over time.
- **Data Persistence**: Transactions are saved in a CSV file for easy access and management.

### Requirements

- Python 3.x
- Pandas
- Matplotlib

### Usage

1. **Run the Application**:
   Open a terminal, navigate to the project directory, and run:
   ```bash
   python finance_tracker.py
   ```

2. **Menu Options**:
   - **Add new transaction**: Log a new income or expense.
   - **View transactions and summary within a date range**: Input a start and end date to view transactions and summary statistics.
   - **Exit**: Close the application.

### How to Add a Transaction

When prompted, enter the following details:
- **Date**: Enter the date of the transaction in `dd-mm-yyyy` format or press Enter to use today's date.
- **Amount**: Enter the transaction amount (must be a positive number).
- **Category**: Specify the category as 'I' for Income or 'E' for Expense.
- **Description**: Provide an optional description for the transaction.

### Viewing Transactions

When viewing transactions:
- Enter the start and end dates to filter transactions.
- A summary of total income, expenses, and net savings will be displayed.
- You can choose to visualize the data in a plot.

### Data Storage

Transactions are stored in a CSV file named `finance_data.csv`. The application will create this file if it does not already exist.

### Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the Pandas and Matplotlib libraries for providing powerful tools for data manipulation and visualization.
- Inspired by the need for better personal finance management.

