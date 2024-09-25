numbers = [5, 10, 15, 20, 25, 100, 111]
x = int(input("num: "))
if x in numbers:
    if x % 2 == 0:
        print("в массиве, четное")
    else:
        print("в массиве, нечетное")
else:
    print(f"переменной {x} нет в массиве")