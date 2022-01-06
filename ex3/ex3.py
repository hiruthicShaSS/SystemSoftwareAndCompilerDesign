import re

MACRO_NAME_EXPRESSION = re.compile(r"#define .*")
MACRO_EXPRESSION = re.compile(r"\s\(.*\)")
final_code = ""
expanded_code = ""
macro_name = ""
macro_expression = ""

operators = ["+", "-", "*", "/", "//"]


def expand(var):
    code = ""
    var = var.replace("(", "")
    var = var.replace(")", "")

    code = f"{var}={var}"
    expression = MACRO_EXPRESSION.findall(macro_expression)[0]
    expression = expression.replace(" ", "")

    for operator in operators:
        if operator in expression:
            code += f"{operator}{var};  // Macro Expansion\n"

    return code


with open("expression.txt") as file:
    for line in file.readlines():
        if MACRO_NAME_EXPRESSION.match(line):
            # Always get the last index
            macro_expression = line.split("#define ")[-1]
            macro_name = macro_expression.split("(")[0]
        elif macro_name.strip() in line:
            # Extract the single macro argument from the macro call
            var = re.compile(r"\(.\)").findall(line)[0]
            final_code += expand(var)
        else:
            final_code += line

print(final_code)
