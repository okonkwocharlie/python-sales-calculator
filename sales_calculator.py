
import csv
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt


# CSV file stored beside this Python file
CSV_FILE = Path(__file__).with_name("sales_records.csv")


# Calculate total sales
def calculate_total(sales):
    return sum(sales)


# Calculate average sales
def calculate_average(sales):
    if not sales:
        return 0

    return sum(sales) / len(sales)


# Find highest sale
def find_highest_sale(sales):
    if not sales:
        return 0

    return max(sales)


# Find lowest sale
def find_lowest_sale(sales):
    if not sales:
        return 0

    return min(sales)


# Load historical sales from CSV
def load_sales():
    sales = []

    if not CSV_FILE.exists():
        return sales

    try:
        with open(
            CSV_FILE,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            # Skip the heading
            next(reader, None)

            for row in reader:

                # New format: timestamp, amount
                # Old format: amount only
                try:
                    if len(row) >= 2:
                        amount = float(row[1])
                    elif len(row) == 1:
                        amount = float(row[0])
                    else:
                        continue

                    if amount >= 0:
                        sales.append(amount)

                except ValueError:
                    print(f"Skipping invalid CSV row: {row}")

    except OSError as error:
        print(f"Could not read sales file: {error}")

    return sales


# Save sales with date and time
def save_sales(sales):

    needs_header = (
        not CSV_FILE.exists()
        or CSV_FILE.stat().st_size == 0
    )

    try:
        with open(
            CSV_FILE,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if needs_header:
                writer.writerow([
                    "Sale Date & Time",
                    "Sale Amount (NGN)"
                ])

            for amount in sales:

                sale_time = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                writer.writerow([
                    sale_time,
                    amount
                ])

        print("\nSUCCESS: Sales saved.")
        return True

    except OSError as error:
        print(f"\nERROR: Could not save sales. {error}")
        return False


# Record new sales
def record_sales():

    while True:
        try:
            number_of_sales = int(
                input("\nHow many sales do you want to enter? ")
            )

            if number_of_sales <= 0:
                print("Enter a number greater than zero.")

            else:
                break

        except ValueError:
            print("Invalid input. Enter a whole number.")

    sales = []

    while len(sales) < number_of_sales:

        try:
            amount = float(
                input(f"Enter sale {len(sales) + 1}: ")
            )

            if amount < 0:
                print("Sales cannot be negative.")

            else:
                sales.append(amount)

        except ValueError:
            print("Invalid input. Enter a valid number.")

    # Save the new sales
    saved = save_sales(sales)

    if saved:
        print(f"\n{len(sales)} new sales recorded.")

    else:
        print("\nSales were not saved successfully.")


# View complete sales report
def view_sales_report():

    sales = load_sales()

    if not sales:
        print("\nNo sales records found.")
        return

    print("\n========== SALES REPORT ==========")

    print(f"Number of sales: {len(sales)}")

    print(
        f"Total sales:   NGN {calculate_total(sales):,.2f}"
    )

    print(
        f"Average sales: NGN {calculate_average(sales):,.2f}"
    )

    print(
        f"Highest sale:  NGN {find_highest_sale(sales):,.2f}"
    )

    print(
        f"Lowest sale:   NGN {find_lowest_sale(sales):,.2f}"
    )

    print("================================")


# View sales history
def view_sales_history():

    if not CSV_FILE.exists():
        print("\nNo sales history found.")
        return

    try:
        with open(
            CSV_FILE,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            # Skip heading
            next(reader, None)

            print("\n========== SALES HISTORY ==========")

            count = 0

            for row in reader:

                if not row:
                    continue

                try:
                    if len(row) >= 2:
                        sale_time = row[0]
                        amount = float(row[1])

                    else:
                        # Support older CSV records
                        sale_time = "Date unavailable"
                        amount = float(row[0])

                    count += 1

                    print(
                        f"{count}. {sale_time} | "
                        f"NGN {amount:,.2f}"
                    )

                except ValueError:
                    print(f"Skipping invalid row: {row}")

            if count == 0:
                print("No valid sales records found.")

            print("=================================")

    except OSError as error:
        print(f"\nCould not read sales history: {error}")


# Display a chart of recorded sales
def view_sales_chart():

    sales = load_sales()

    if not sales:
        print("\nNo sales records available to display.")
        return

    sale_numbers = list(range(1, len(sales) + 1))

    plt.figure(figsize=(10, 5))

    plt.bar(sale_numbers, sales)

    plt.title("Sales Performance")
    plt.xlabel("Sale Number")
    plt.ylabel("Sale Amount (NGN)")

    plt.xticks(sale_numbers)
    plt.ticklabel_format(
        axis="y",
        style="plain"
    )

    plt.tight_layout()
    plt.show()


# Main menu
def main():

    while True:

        print("\n========== SALES CALCULATOR ==========")

        print("1. Record new sales")
        print("2. View sales report")
        print("3. View sales history")
        print("4. View sales chart")
        print("5. Exit")


        print("====================================")

        choice = input("Choose an option: ")

        if choice == "1":

            record_sales()

        elif choice == "2":

            view_sales_report()

        elif choice == "3":

            view_sales_history()

        elif choice == "4":
            view_sales_chart()

        elif choice == "5":

            print("\nThank you for using the Sales Calculator!")
        
        
            break

        else:

            print("\nInvalid choice.")
            print("Please select 1, 2, 3, or 4.")


# Start the application
if __name__ == "__main__":
    main()
