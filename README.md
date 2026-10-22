# Python Sales Calculator

A beginner-friendly Python application for recording sales, storing sales history, calculating key sales statistics, and visualizing sales performance.

## About the Project

The Python Sales Calculator was built to practise Python programming by solving a simple business problem: keeping track of sales and understanding sales performance.

The application uses a CSV file to store sales records, allowing previously saved sales to be loaded when the program runs again.

## Features

- **Record Sales:** Enter multiple sales amounts.
- **Input Validation:** Reject invalid numbers and negative sales amounts.
- **Persistent Storage:** Save sales records in a CSV file.
- **Date and Time Tracking:** Record when each sale is entered.
- **Sales Reports:** Calculate total sales, average sale, highest sale, and lowest sale.
- **Sales History:** View previously saved sales records.
- **Data Visualization:** Display recorded sales in a bar chart.
- **Menu-Driven Interface:** Navigate the application through a simple text menu.

## Technologies Used

- Python 3
- CSV module
- `pathlib`
- `datetime`
- Matplotlib

## Requirements

- Python 3 installed on your computer.
- Matplotlib installed in your Python environment.
- Visual Studio Code or another Python-compatible editor.

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/okonkwocharlie/python-sales-calculator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-sales-calculator
   ```

3. Install Matplotlib:

   ```bash
   python -m pip install matplotlib
   ```

4. Run the application:

   ```bash
   python sales_calculator.py
   ```


## How to Use

When the application starts, select an option from the menu to:

1. Record new sales.
2. View the sales report.
3. View sales history.
4. View the sales chart.
5. Exit the application.

The application saves sales records locally in a CSV file so that they can be retrieved during later runs.

## Project Structure

```text
python-sales-calculator/
├── sales_calculator.py
├── README.md
├── .gitignore
└── sales_records.csv  # Generated locally; not committed
```

The CSV file is generated locally when sales are saved and should be excluded from version control if it contains real or private data.

## What I Learned

Through this project, I practised:

- Writing and organizing Python functions.
- Using loops and conditional statements.
- Validating user input with exception handling.
- Reading and writing CSV files.
- Working with dates and times.
- Calculating descriptive statistics.
- Creating charts with Matplotlib.
- Building a menu-driven command-line application.

## Future Improvements

- Export sales reports.
- Filter sales by date.
- Compare sales across different periods.
- Add a graphical user interface.
- Add automated tests.

## Author

**OKONKWO CHARLES**

- GitHub: [okonkwocharlie](https://github.com/YOUR-USERNAME)
