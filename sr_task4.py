def extract_subtuple(tup, element):
    if element not in tup:
        return ()

    first_index = tup.index(element)

    try:
        second_index = tup.index(element, first_index + 1)
        return tup[first_index:second_index + 1]
    except ValueError:
        return tup[first_index:]

my_tuple = (1, 2, 3, 4, 5, 3, 6, 7, 3, 8, 9)
element_to_find = 3

result = extract_subtuple(my_tuple, element_to_find)
print("Результат:", result)