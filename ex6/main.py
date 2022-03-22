import re

VARIABLE_EXPRESSION = re.compile(r"[a-zA-Z_$0-9]{1,}")
DATA_TYPES = ["int", "char", "float", "double", "long"]
OPERATORS = ["=", "/", "//", "*", "+", "-", "**"]

ids = {}

with open("input.c") as file:
    lines = file.readlines()

    id = 1
    # Just a flag to check if the next print statement should be on the previous line
    print_pending = False

    for line in lines:
        multiple_expression_inline = line.split(";")

        for expression_inline in multiple_expression_inline:
            expression_inline = expression_inline.strip()

            data_type = expression_inline.split(" ")
            data_type = data_type[0] if data_type[0] in DATA_TYPES else None

            if (data_type != None):
                # Remove the datatype from the line as we already extracted it
                expression_inline = expression_inline.replace(data_type, "")
                print(f"<keyword, {data_type}>", end=" ")
                print_pending = True

            if ("," in expression_inline):  # Multiple variable declared inline
                variables = expression_inline.split(",")

                for variable in variables:
                    variable = variable.strip()

                    ids[variable] = id if ids.get(
                        variable, None) is None else ids[variable]
                    id += 1

                    if (print_pending):
                        print(f"<id{ids[variable]}, {variable}>")
                        print_pending = False
                    else:
                        print(f"<punctuation, ,> <id{ids[variable]}, {variable.strip()}>")

            for operator in OPERATORS:
                if operator in expression_inline:
                    all_variables_inline = VARIABLE_EXPRESSION.findall(expression_inline)[
                        1:]
                    expression_first_variable = expression_inline.split(operator)[
                        0][-1]

                    print(
                        f"<op, {operator}> <id{ids[expression_first_variable]}, {expression_first_variable}>")

            numbers = re.findall(r"\d{0,}", expression_inline)
            for number in numbers:
                if (number == ""): continue
                print(f"<num, {number}>")
                expression_inline.replace(number, "")

            
            if (";" in line):  # Ids will be populated at this point by the above if condition
                print(
                    f"<punctuation, ;> <id{ids[multiple_expression_inline[0][-1]]}, {multiple_expression_inline[0][-1]}>")
                line = line.replace(";", "")
                # expression_inline[0].replace(";", "")
        # multiple_expression_inline[0] = ""
            # else:
            #     print(expression_inline)
print("<punctuation, ;>")