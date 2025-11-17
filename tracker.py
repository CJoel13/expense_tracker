import os
import datetime

def clear_screen():
    os.system('clear')

def validate_numeric_input(message, number_of_options=1, retries=3):
    while True:
        try:
            response = int(input(message))
            if response < 1 or response > number_of_options:
                raise ValueError("Value error, select an option between 1 and ", number_of_options)
            return response
        except ValueError as e:
            retries -= 1
            print(e, " -- Retries: ", retries)
        if (retries <= 0):
            exit("Retries exceeded, quiting...")

def display_menu():
    prompt = """Select action:
1) Register expense
2) Summary
3) Delete expense
4) Exit
"""
    return validate_numeric_input(prompt, 4)

category_set = set()

def read_category(retries=3):
    while True:
        category = input("Enter category: ")
        if category == "":
            # TODO: validate other invalid expressions
            clear_screen()
            print("Invalid input!")
        else:
            category = category.lower()
            category = category[0].upper() + category[1:]
            category_set.add(category)
            return
        retries -= 1
        if retries <= 0:
            exit("Retries exceeded, quiting")

def read_amount(retries=3):
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount == 0.0:
                raise ValueError("Invalid input, it's 0.0")
            else:
                return amount
        except ValueError as e:
            retries -= 1

            print(e, "Retries: ", retries)
        if retries <= 0:
            exit("Retries exceeded, quiting")


def read_date(retries=3):
    """
    Read and validate a date.

    Parameters:
    -----
    retries : int
        The number of input retries before exit()
    """
    expected_format = "%Y-%m-%d"
    while True:
        try:
            date = input("Enter a date (YYYY-MM-DD) --- Enter to use today: ")
            if date == "":
                return str(datetime.date.today())
            validDate = datetime.datetime.strptime(date, expected_format)
            if validDate > datetime.datetime.today():
                raise ValueError("ValueError: The date is a future date...")
            return str(validDate)
        except ValueError as e:
            clear_screen()
            print(e)
            retries -= 1
        if retries <= 0:
            exit()

category = ""
amount = 0
date = ""

list_of_expenses = []

def register_expense():
    print("Registering expense:\n------")
    category = read_category()
    amount = read_amount()
    date = read_date()
    
    list_of_expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense registered!\n")

def print_expenses_indiv(expenses):
    print("Printing list of expenses:\n------")
    for exp in expenses:
        print("Category: ", exp['category'])
        print("Amount: ", exp['amount'])
        print("Date: ", exp['date'])
        print('----')

def print_expense_single_line(expenses):
    for i, exp in enumerate(expenses):
        print(i+1, ". ", sep='', end='')
        print("$", exp['amount'], " - ", end='')
        print(exp['category'], " ", end='')
        print("(", exp['date'], ")")

def print_summary():
    print("Summary:\n---------")
    print("Unique categories: ", category_set)
    total_amount = 0
    for expense in list_of_expenses:
        # print("Category: ", expense['category'])
        total_amount += expense['amount']
    
    print("----")
    print("Total amount: $", f"{total_amount:.2f}")
    expenses_length = len(list_of_expenses)
    average_amount = total_amount / expenses_length
    print("Average expense: $", f"{average_amount:.2f}")
    print("-----")

    sorted_list_of_expenses = sorted(list_of_expenses, key=lambda x: x['amount'], reverse=True)
    # print_expenses_indiv(sorted_list_of_expenses)

    if expenses_length >= 3:
        print("Top 3 expenses:")
        # Print top 3 expenses
        print_expense_single_line(sorted_list_of_expenses[:3])
        print("")

    else:
        print("Top ", expenses_length, " expenses")
        print_expense_single_line(sorted_list_of_expenses)




def test_register_expense():
    category = "Health"
    amount = 100.92
    date = str(datetime.date.today())

    category2 = "Food"
    amount2 = 23.11
    date2 = str(datetime.date.today())

    category_set.add(category)
    category_set.add(category2)


def test_list_of_expenses():
    list_of_expenses.append({"category": "Health", "amount": 123.2, "date": "2021-11-11"})
    list_of_expenses.append({"category": "Food", "amount": 5.23, "date": "2021-12-12"})
    list_of_expenses.append({"category": "Services", "amount": 20, "date": "2025-11-16"})


def remove_expense(retries=3):
    clear_screen()
    option = 0
    if len(list_of_expenses) > 0:
        print("Removing expense:")
        print_expense_single_line(list_of_expenses)
        print("----")
        option_range = "(1 - " + str(len(list_of_expenses)) + ")"
        while True:
            try:
                print(f"Select expense to delete {option_range}: ", sep='', end='')
                option = int(input())
                if option < 1 or option > len(list_of_expenses):
                    raise ValueError(f"Invalid option, select an option between {option_range}")
                break
            except ValueError as e:
                print(e)
                retries -= 1
                if retries <= 0:
                    exit("Retries exceeded, quiting...")
        print("Option selected: ", option)
        del list_of_expenses[option - 1]
        print("Updated list: ")
        print_expense_single_line(list_of_expenses)

    else:
        print("Empty expense list, first add an expense")

option = display_menu()

while option != 4:
    match option:
        case 1:
            register_expense()
        case 2:
            print_summary()
        case 3:
            remove_expense()
    
    option = display_menu()