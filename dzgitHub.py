def open_file():
    with open('input.txt', 'w') as file:
        print('Python\nRuby\nC++\nC\nJava\nGO', file=file)


open_file()