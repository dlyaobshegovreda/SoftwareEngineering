# Реализовать ввод данных в программу через консоль в виде трех целых чисел.
# Необходимо найти наибольшее и наименьшее из них.

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

print(f"Наибольшее число: {max(a,b,c)} \nНаименьшее число: {min(a,b,c)}")