class Car:
    def __init__(self, make, model):

        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# Создаем новый класс ElectricCar, который наследует класс Car
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  # инициализирует атрибуты родительского класса
        self.battery_capacity = battery_capacity  # устанавливает емкость батареи

    def charge(self):
        # Выводит сообщение о том, что электромобиль заряжается
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")


# Создается объект my_electric_car с маркой "Tesla", моделью "Model S" и емкостью батареи 75 кВт-ч
my_electric_car = ElectricCar("Tesla", "Model S", 75)


# Этот метод выведет сообщение о том, что электромобиль едет
my_electric_car.drive()


# Этот метод выведет сообщение о процессе зарядки электромобиля
my_electric_car.charge()