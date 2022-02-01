opcode = []

with open("input.txt") as file:
    input_data = file.readlines()

    program_name = input("Enter program name: ")

    for line in input_data:
        opcode.append(line.split("^"))

    print(f"Name from obj. {program_name}")
    for code in opcode[1:]:
        if code[0] == "E":
            break

        address = int(code[1])

        for elem in code[3:]:
            # print(elem)
            for i in range(0, len(elem), 2):
                if (elem[i:i+2].strip() == ""):
                    continue

                print(f"00{address} {elem[i:i+2]}")
                address += 1
