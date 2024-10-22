def add_expense(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        expense = input("Введите описание расхода и сумму: ")
        file.write(expense + "\n")

def show_expenses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        expenses = file.readlines()
        if expenses:
            print("Ваши расходы:")
            for expense in expenses:
                print(expense.strip())
        else:
            print("Расходов нет.")

add_expense("exp.txt")
add_expense("exp.txt")
add_expense("exp.txt")
show_expenses("exp.txt")