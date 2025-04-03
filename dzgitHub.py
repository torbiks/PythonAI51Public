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

