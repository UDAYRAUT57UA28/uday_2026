def input_data(filename):
    income = int(input("Enter your total income: "))
    expenses = int(input("Enter your total expenses: "))
    with open(filename, 'w') as file:
        file.write(f"Income: {income}\n")
        file.write(f"Expenses: {expenses}\n")
    print(f"\nData successfully written to {filename}")

def read_balance(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        read_income = int(lines[0].split(': ')[1].strip())
        read_expenses = int(lines[1].split(': ')[1].strip())
        balance = read_income-read_expenses
    print("The balance is : ",balance)

def main():
    filename = str(input("Enter the file name: "))
    filename =  filename +".txt"
    while True:
        print('''Chose the Operation:
              1. Input the income and expense.
              2. Read balance
              3. Exit''')
        ch = int(input("Enter your choice(1-3): "))
        if  ch == 1:
            input_data(filename)
        elif ch ==2:
            read_balance(filename)
        elif ch == 3:
            print("You have exited the program.")
            return
        else:
            print("invalid choice! please enter a number 1 to 3.")

main()
