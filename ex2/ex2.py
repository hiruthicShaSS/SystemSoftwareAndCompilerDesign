import re

tokens = {
    "keywords": ["int", "float", "double", "char", "string" "class", "struct"],
    "operators": ["=", "-", "+", "*", "/"],
    "relational": ["<=", ">=", "==", "!="],
    "punctuation": [",", ";"]
}

FUNCTION_EXPRESSION = re.compile(r"\w*. \w*.\(.*\)")
VARIABLE_EXPRESSION = re.compile(r"[a-zA-Z_$0-9]{1,}")


class Symbol:
    def __init__(self) -> None:
        self.id = None
        self.data_type = None
        self.return_type = None
        self.initial_value = 0
        self.num_params = 0
        self.type_of_params = None
        self.isFunction = False
        self.functionParams = None

    def __str__(self) -> str:
        return f"{self.id}\t{self.data_type}\t\t{self.return_type}\t\t{self.initial_value}\t\t{self.num_params}\t\t\t{self.type_of_params}"


def charInTokenDB(char: str) -> bool:
    return char.strip() in tokens["operators"] or char in tokens["relational"] or char in tokens["punctuation"]


symbol_table = []


def isSymbolAlreadyExists(symbol):
    return all(symbol.id == s.id for s in symbol_table)


with open("expression.txt") as file:
    for line in file.readlines():
        print(VARIABLE_EXPRESSION.findall(line))
        
        expression = ""
        lastDataType = ""
        symbol = Symbol()
        for i, char in enumerate(line):
            # print(f"{i} - {char}")

            if not charInTokenDB(char):
                expression += char

            if char == " ":
                if expression.strip() in tokens["keywords"]:
                    symbol.data_type = expression
                    lastDataType = expression
                else:
                    symbol.id = expression.strip()
                expression = ""

            if char.strip() == "=":
                symbol1 = Symbol()
                symbol1.data_type = lastDataType
                # Characters before the current (current is '=')
                symbol1.id = line[:i].split(" ")[-1]
                # Characters after the current (current is '=')
                symbol1.initial_value = line[i+1:].split(";")[0]

                # if isSymbolAlreadyExists(symbol1):
                symbol_table.append(symbol1)

        symbol_table.append(symbol)


symbol_table.reverse()
print("ID\tData Type\tReturn Value\tInitial Value\tNo. of Parameters\tType of Paramameters", end="\n\n")
for symbol in symbol_table:
    print(symbol)
