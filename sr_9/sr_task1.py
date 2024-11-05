class Tomato:
    # Статическое свойство states, содержащее стадии созревания
    states = {0: "отсутствует", 1: "цветение", 2: "зеленый", 3: "красный"}

    def __init__(self, index):
        # _index: идентификатор помидора, передается параметром
        # _state: стадия созревания, принимает первое значение из словаря states
        self._index = index
        self._state = Tomato.states[0]

    # Метод для перехода на следующую стадию созревания
    def grow(self):
        if self._state != Tomato.states[3]:  # Если помидор еще не созрел полностью
            current_stage = list(Tomato.states.values()).index(self._state)
            self._state = Tomato.states[current_stage + 1]  # Переход на следующую стадию

    # Метод для проверки зрелости помидора
    def is_ripe(self):
        return self._state == Tomato.states[3]

# Класс TomatoBush
class TomatoBush:
    def __init__(self, num_tomatoes):
        # tomatoes: список объектов Tomato
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    # Метод для роста всех томатов на следующую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Метод для проверки, что все томаты созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Метод для сбора урожая (очищение списка томатов)
    def give_away_all(self):
        self.tomatoes = []

# Класс Gardener
class Gardener:
    def __init__(self, name, plant):
        # name: имя садовника, публичное свойство
        # _plant: объект класса TomatoBush, за которым ухаживает садовник
        self.name = name
        self._plant = plant

    # Метод для ухода за растением (увеличивает стадию зрелости всех томатов)
    def work(self):
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()

    # Метод для сбора урожая, если все томаты созрели
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай...")
            self._plant.give_away_all()
        else:
            print("Еще не все томаты созрели, подождите.")

    # Статический метод, выводящий справку по садоводству
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ухаживайте за растением, чтобы оно созрело. Собирать урожай можно, только когда все плоды созрели.")


# ТЕСТИРОВАНИЕ
# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов TomatoBush и Gardener
bush = TomatoBush(5)  # куст с 5 помидорами
gardener = Gardener("Стёпка", bush)

# Уход за кустом
gardener.work()  # Ухаживаем первый раз
gardener.harvest()  # Пробуем собрать урожай, когда томаты еще не созрели

# Продолжаем ухаживать, пока все томаты не созреют
while not bush.all_are_ripe():
    gardener.work()

# Сбор урожая, когда все томаты созрели
gardener.harvest()