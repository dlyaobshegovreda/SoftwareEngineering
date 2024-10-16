request = int(input('Введите № кабинета: '))

dictionary = {
    101: {'key': 123, 'access': True},
    201: {'key': 456, 'access': True},
    301: {'key': 789, 'access': True},
    401: {'key': 000, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)

if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, "/", access)