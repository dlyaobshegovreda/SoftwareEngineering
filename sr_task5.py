from sr_task5_1 import square

def main():
    print("Введите длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    area = square(a, b, c)
    print(f"Площадь треугольника: {area:.2f} кв. ед.")

if __name__ == '__main__':
    main()
