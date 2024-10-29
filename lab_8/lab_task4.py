class Car:
    def __init__(self, make, model):
        self._make = make  # устанавливает марку автомобиля (защищенный)
        self.__model = model  # устанавливает модель автомобиля (частный)

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")

# Вывод защищенного атрибута _make
# Доступ к этому атрибуту возможен, так как он является защищенным
print(my_car._make)

my_car.drive()