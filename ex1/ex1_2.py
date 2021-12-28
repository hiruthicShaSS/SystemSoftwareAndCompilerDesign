tokens = {
    "keywords": ["int", "float", "double", "class", "struct", "end"],
    "operators": ["=", "-", "+", "*", "/"],
    "relational": ["<=", ">=", "==", "!="],
    "punctuation": [",", ";"]
}

total_tokens = 0
identifier_count = {}
all_identifier_count = 0


def parse_line(line: str):
    global identifier_count, all_identifier_count

    lineSplit = line.split(" ")
    dataType = lineSplit[0]
    expressionLine = lineSplit[1]

    if (dataType in tokens["keywords"]):
        print(f"< {dataType} , keyword > ")

    for keyword in tokens["relational"]:
        if keyword in expressionLine:
            temp = expressionLine.split(keyword)
            variable = temp[0]
            value = temp[1].split(";")[0]

            all_identifier_count += 1
            if variable in identifier_count.keys():
                identifier_count[variable] += 1
            else:
                identifier_count[variable] = all_identifier_count

            print(
                f"< {variable} , Identifier id-{identifier_count.get(variable, all_identifier_count)} >")
            print(f"< {keyword} , relational operator >")
            print(f"< {value} , Number >")

    # If multiple expression in same line
    for expression in expressionLine.split(","):
        for keyword in tokens["operators"]:
            if keyword in expression:
                variable_declaration = expression.split(keyword)

                all_identifier_count += 1
                if variable_declaration[0] in identifier_count.keys():
                    identifier_count[variable_declaration[0]] += 1
                else:
                    identifier_count[variable_declaration[0]] = all_identifier_count

                print(
                    f"< {variable_declaration[0]} , Identifier id-{identifier_count.get(variable_declaration[0], all_identifier_count)} >")

                if ";" in variable_declaration[1]:
                    print("< ; , Punctuation >")

                print(f"< {variable_declaration[1]} , Number >")

                if "end" in variable_declaration[1]:
                    print("< end , keyword >")


with open("expression2.txt") as expression:
    lines = expression.readlines()

    # Parse data
    for line in lines:
        parse_line(line)
