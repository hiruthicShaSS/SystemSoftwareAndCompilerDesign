op_table = {}

labels = []
commands = []
values = []
memory_locations = []

op_code = []
object_code = []

sym_table = {sym.split()[0]: sym.split()[1] for sym in open("symtab.txt").readlines()}
print(sym_table)

with open("optab.txt") as optab:  # Populate OP table
    optable = optab.readlines()
    for line in optable:
        op_table[line.split()[0]] = line.split()[1]

with open("input.txt") as input_:
    input_data = input_.readlines()
    for line in input_data:
        if "START" in line:  # Detect starting point of the program
            start = line.split()[2]
            memory_locations.append("")
            x = int(start, 16)
        else:
            if len(line.split()) == 3:
                memory_locations.append((sym_table.get(line.split()[0])))
            else:
                memory_locations.append(str(hex(x)[2:]))
            x += 3

    for line in input_data:
        line = line.split()
        if len(line) == 3:
            labels.append(line[0])
            commands.append(line[1])
            values.append(line[2])
        elif len(line) == 2:
            labels.append("")
            commands.append(line[0])
            values.append(line[1])
        else:
            commands.append(line[0])

for command in commands:
    if command == "START":
        continue
    if command in op_table:
        x = str(op_table[command])
        y = str(memory_locations[labels.index(values[commands.index(command)])])
        object_code.append(f"^{x + y}")

ob = "".join(object_code)
x = str(hex(len(object_code) * 3)[1:])

if "x" in x:
    x = x.replace("x", "0")

with open("result.txt", "w+") as result:
    result.write(f"H^{labels[0]}^{memory_locations[1]}^{memory_locations[-1][2:]}\n")
    result.write(f"T^{memory_locations[1]}^{x}{ob}\n")
    result.write(f"E^00{memory_locations[1]}\n")
