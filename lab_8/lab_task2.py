class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        # Выводит сообщение о том, что автомобиль едет
        print(f"Driving the {self.make} {self.model}")


# Создается объект my_car с маркой "Toyota" и моделью "Corolla"
my_car = Car("Toyota", "Corolla")


#Сообщение о том, что автомобиль едет
my_car.drive()