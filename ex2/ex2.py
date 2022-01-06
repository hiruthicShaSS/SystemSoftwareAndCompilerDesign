import re
import copy

tokens = {
    "keywords": ["int", "float", "double", "char", "string" "class", "struct"],
    "operators": ["=", "-", "+", "*", "/"],
    "relational": ["<=", ">=", "==", "!="],
    "punctuation": [",", ";"],
}

FUNCTION_EXPRESSION = re.compile(r"\w{1,}\(.*\)")
MAGICAL_EXPRESSION = re.compile(r"[a-zA-Z_$0-9]{1,}")


class Symbol:
    def __init__(self) -> None:
        self.id = None
        self.data_type = None
        self.initial_value = 0
        self.isFunction = False
        self.return_type = None
        self.function_params = None
        self.type_of_params = None
        self.num_params = None

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def __hash__(self) -> int:
        return hash(("id", self.id))

    def __str__(self) -> str:
        return f"{self.id}\t{self.data_type}\t\t{self.return_type}\t\t{self.initial_value}\t\t{self.num_params}\t\t\t{self.type_of_params}"


def charInTokenDB(char: str):
    char = char.strip()
    return (
        char in tokens["operators"]
        or char in tokens["punctuation"]
        or char in tokens["relational"]
    )


symbol_table = []


def isSymbolAlreadyExists(symbol):
    return all(symbol.id == s.id for s in symbol_table)


def tryCast(value, expectedType):
    try:
        if expectedType == "int":
            value = int(value)
        if expectedType == "float":
            value = float(value)
        if expectedType == "double":
            value = float(value)
        if expectedType == "char":
            value = str(value)

        return type(value)
    except ValueError as e:
        return None


with open("expression.txt") as file:
    for line in file.readlines():
        all_tokens = MAGICAL_EXPRESSION.findall(line)

        lastDataType = ""
        symbol = Symbol()

        for index, token in enumerate(all_tokens):
            if token in tokens["keywords"]:
                symbol.data_type = token
                lastDataType = token

                try:
                    if lastDataType == "int" and tryCast(
                        all_tokens[index + 1], lastDataType
                    ):
                        symbol.initial_value = all_tokens[-1]
                    elif (
                        lastDataType == "double"
                        and tryCast(all_tokens[index + 1], float) != None
                    ):
                        symbol.initial_value = all_tokens[-1]
                    elif (
                        lastDataType == "float"
                        and tryCast(all_tokens[index + 1], float) != None
                    ):
                        symbol.initial_value = all_tokens[-1]
                    elif (
                        lastDataType == "char"
                        and tryCast(all_tokens[index + 1], str) != None
                    ):
                        symbol.initial_value = all_tokens[-1]
                except ValueError as e:
                    pass
            else:
                symbol.id = all_tokens[1]

            if len(FUNCTION_EXPRESSION.findall(line)) > 0:
                symbol.isFunction = True
                params = [word for word in all_tokens if word in tokens["keywords"]]
                symbol.num_params = len(params) - 1
                symbol.initial_value = None
                symbol.type_of_params = ", ".join(params[:-1])
                symbol.return_type = symbol.data_type
                symbol1 = copy.deepcopy(symbol)  # Something wired happens here!
                symbol1.data_type = None
                symbol_table.append(symbol1)
                continue

            symbol_table.append(symbol)


symbol_table = [
    symbol_table[i]
    for i in range(len(symbol_table))
    if symbol_table[i].id != symbol_table[min(i + 1, len(symbol_table) - 1)].id
    or i == len(symbol_table) - 1
]

# Remove None from the table
symbol_table = [
    symbol_table[i] for i in range(len(symbol_table)) if symbol_table[i].id != None
]

print(
    "ID\tData Type\tReturn Type\tInitial Value\tNo. of Parameters\tType of Paramameters",
    end="\n\n",
)
for symbol in symbol_table:
    print(symbol)
