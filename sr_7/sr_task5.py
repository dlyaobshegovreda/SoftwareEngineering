def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            names = file.readlines()
        print("Имена из файла:")
        for name in names:
            print(name.strip())
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")

def main():
    file_path = 'names.txt'
    read_file(file_path)

if __name__ == '__main__':
    main()
