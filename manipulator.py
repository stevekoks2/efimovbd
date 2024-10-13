print("░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓██████████████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░  ")
print("░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ")
print("░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒")
print("░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")
print("░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓██▓▒░  ░▒▓███████▓▒░░▒▓███████▓▒░ ")                                                                                                     

def create_table(name, *poles):
    open(f'{name}.efimov', 'w')
    with open(f'{name}.efimov', 'r') as file:
        lines = file.readlines()
    lines.insert(1 ,f'NAME:{name}\n')
    with open(f'{name}.efimov', 'w') as file:
        file.writelines(lines)
    i = 3
    for pole in poles:
        with open(f'{name}.efimov', 'r') as file:
            lines = file.readlines()
        lines.insert(i ,f'{pole}:\n')
        with open(f'{name}.efimov', 'w') as file:
            file.writelines(lines)
        i+=1
    print(f"Base {name} created!")

def insert_data(basa ,pole, data):
    with open(f'{basa}.efimov', 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(f"{pole}:"):
            lines[i] = line.rstrip() + " " + data + "," + '\n'
            break
    
    with open(f'{basa}.efimov', 'w') as file:
        file.writelines(lines)
    print(f"Information added in {basa} {pole}")