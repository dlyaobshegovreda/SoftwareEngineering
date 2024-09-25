string = "a b c d e f g f k"
value = input("буква: ")
for i in string:
    if i == value:
        index = string.find(value)
        print(f"буква  {value}  есть в строке под индексом {index}")
        break
else:
    print(f"буквы {value} нет в строке")