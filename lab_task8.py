x = 0
while x < 100:
    print(x)
    if x % 10 == 0:
        x += 15
    elif x % 2 == 0:
        x += 1
    else:
        x += 2