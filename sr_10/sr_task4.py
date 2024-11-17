class RepeatDecorator:
    def __init__(self, times):
        # количество повторений функции
        self.times = times

    def __call__(self, func):
        # позволяет экземплярам класса использоваться как декораторы
        def wrapper(*args, **kwargs):
            # внутренняя функция, которая будет выполнять декорируемую функцию
            for i in range(self.times):
                # цикл для выполнения функции заданное количество раз
                print(f"Выполнение {i + 1} из {self.times}")
                func(*args, **kwargs)  # вызов декорируемой функции с аргументами
        return wrapper  # возвращаем обертку в качестве декорированной функции

# используем декоратор для функции print_hello
@RepeatDecorator(times=3)
def print_hello():
    # функция, которая печатает приветствие
    print("Привет!")

# переменная для счетчика
counter = 0

# используем декоратор для функции increment_counter
@RepeatDecorator(times=5)
def increment_counter():
    # функция, которая инкрементирует версию счетчика и выводит его значение
    global counter  # используем переменную счетчика
    counter += 1  # увеличиваем значение счетчика на 1
    print(f"Текущее значение счетчика: {counter}")

# запуск функции print_hello
print("Запуск функции print_hello:")
print_hello()

# запуск функции increment_counter
print("\nЗапуск функции increment_counter:")
increment_counter()
