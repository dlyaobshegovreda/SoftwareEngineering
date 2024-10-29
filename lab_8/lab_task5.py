class Shape:
    def area(self):
        # Метод для вычисления площади
        # Нужно переопределить в дочерних классах
        pass

# Класс Rectangle наследует от класса Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # устанавливает ширину прямоугольника
        self.height = height  # устанавливает высоту прямоугольника

    def area(self):
        # Метод для вычисления площади прямоугольника
        # Площадь рассчитывается как ширина * высота
        return self.width * self.height

# Класс Circle также наследует от класса Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # устанавливает радиус круга

    def area(self):
        # Метод для вычисления площади круга
        # Площадь рассчитывается как π * радиус²
        return 3.14 * self.radius * self.radius

# Создается объект my_rectangle с шириной 5 и высотой 4
my_rectangle = Rectangle(5, 4)

# Создается объект my_circle с радиусом 5
my_circle = Circle(5)

# Вывод площади прямоугольника
# Вызов метода area для my_rectangle, который вернет 20 (5 * 4)
print(my_rectangle.area())

# Вывод площади круга
# Вызов метода area для my_circle, который вернет 78.5 (3.14 * 5 * 5)
print(my_circle.area())