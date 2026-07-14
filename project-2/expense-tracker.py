import os

# lists to store item names and their expenses
items = []
expenses = []

# function to clear screen (works on Windows + linux & mac)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# function to add a new expense.
def add_expense():
    item = input("Enter item name: ")
    try:
        amount = float(input("Enter amount: "))  # converting input to number
        items.append(item)       # storing item
        expenses.append(amount)  # storing amount
        print("Expense added successfully!\n")
    except:
        print("Invalid amount! Please enter a number.\n")

# function to display all expenses
def display_expenses():
    print("========= EXPENSE LIST =========\n")
    
    # using enumerate to show numbering
    for i, (item, amount) in enumerate(zip(items, expenses), start=1):
        print(f"{i}. {item} - {amount}")

# function to calculate and show total
def show_total():
    total = sum(expenses)  # built-in function to sum all values
    print(f"\nTotal Spent: {total}\n")

# function to delete an expense
def delete_expense():
    display_expenses()  # first show list to user
    
    try:
        index = int(input("\nEnter number to delete: ")) - 1
        
        # checking if index is valid
        if 0 <= index < len(items):
            items.pop(index)       # remove item
            expenses.pop(index)    # remove amount
            print("Expense deleted!\n")
        else:
            print("Invalid number!\n")
    except:
        print("Invalid input!\n")

# function to edit an existing expense
def edit_expense():
    display_expenses()  # show current list
    
    try:
        index = int(input("\nEnter number to edit: ")) - 1
        
        # check valid index
        if 0 <= index < len(items):
            new_item = input("Enter new item name: ")
            new_amount = float(input("Enter new amount: "))
            
            # updating values
            items[index] = new_item
            expenses[index] = new_amount
            
            print("Expense updated!\n")
        else:
            print("Invalid number!\n")
    except:
        print("Invalid input!\n")


# main program loop (keeps running until user exits)
while True:
    print("========= EXPENSE TRACKER =========\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit\n")

    choice = input("Option: ")

    match choice:

        # add expense
        case '1':
            clear()
            add_expense()

        # view expenses
        case '2':
            clear()
            if not items:
                print("No expenses yet!\n")
            else:
                display_expenses()
                print()

        # show total
        case '3':
            clear()
            if not items:
                print("No expenses yet!\n")
            else:
                display_expenses()
                show_total()

        # delete expense
        case '4':
            clear()
            if not items:
                print("No expenses to delete!\n")
            else:
                delete_expense()

        # edit expense
        case '5':
            clear()
            if not items:
                print("No expenses to edit!\n")
            else:
                edit_expense()

        # exit program
        case '6':
            clear()
            print("Goodbye!")
            break

        # if user enters wrong option
        case _:
            clear()
            print("Invalid option! Try again.\n")