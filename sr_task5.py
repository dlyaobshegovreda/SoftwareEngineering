def process_list(numbers):
    unique_numbers = list(set(numbers))  # Удаляем дубликаты, преобразуя список во множество, затем обратно в список
    unique_numbers.sort()  # Сортируем список
    return tuple(unique_numbers)  # Преобразуем результат в кортеж

# Тест 1: Список с дубликатами и разными числами
test1 = [5, 3, 8, 3, 1, 5, 9, 2]
result1 = process_list(test1)
print(result1)  # Ожидаемый результат: (1, 2, 3, 5, 8, 9)

# Тест 2: Список с одинаковыми элементами
test2 = [4, 4, 4, 4]
result2 = process_list(test2)
print(result2)  # Ожидаемый результат: (4,)

# Тест 3: Список с отрицательными числами
test3 = [-1, -5, -3, -5, 0, 2, -1]
result3 = process_list(test3)
print(result3)  # Ожидаемый результат: (-5, -3, -1, 0, 2)
