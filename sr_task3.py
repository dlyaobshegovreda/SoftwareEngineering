x = int(input("число:"))
if x<0 or x>10:
    print(f"Число {x} вне диапазона")
elif x<=3 and x>=0:
    print("Число в диапазоне 0-3")
elif x>3 and x<6:
    print("Число в дапазоне 3-6")
elif x>=6 and x<=10:
    print("Число в диапазоне 6-10")