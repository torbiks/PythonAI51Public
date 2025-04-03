def open_file():
    with open('input.txt', 'w') as file:
        print('Python\nRuby\nC++len08\nC\nJava\nGO', file=file)

def overkill():
    with open('input.txt', 'r') as file:
        memory = ""
        for line in file:
            if len(line) > len(memory):
                memory = line
    return memory

def main():
    while True:
        choice = input('Оберіть опцію 1-Зчитати файл, 2 - знайти найдовше слово, 0 - Закінчення роботи: ')

        if choice == '2':

            print(f'Результат пошуку: {overkill()}')
        elif choice == '1':
            open_file()
            print(f'Файл зчитано')
        elif choice == '0':
            print('Роботу завершено')
            break
        else:
            print('Некоректний вибір, спробуйте ще раз.')

main()
