def remove_element(tup, value):
    new_list = []

    for x in tup:
        if x != value:
            new_list.append(x)

    return tuple(new_list)


my_tuple = (1, 2, 3, 4, 5)
element_to_remove = 3

new_tuple = remove_element(my_tuple, element_to_remove)
print("Новый кортеж:", new_tuple)