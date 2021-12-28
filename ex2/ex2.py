import re

tokens = {
    "keywords": ["int", "float", "double", "char", "string" "class", "struct"],
    "operators": ["=", "-", "+", "*", "/"],
    "relational": ["<=", ">=", "==", "!="],
    "punctuation": [",", ";"]
}

FUNCTION_EXPRESSION = re.compile(r"\w{1,}\(.*\)")
MAGIC_EXPRESSION = re.compile(r"[a-zA-Z_$0-9]{1,}")


class Symbol:
    def __init__(self) -> None:
        self.id = None
        self.data_type = None
        self.return_type = None
        self.initial_value = 0
        self.num_params = None
        self.type_of_params = None
        self.isFunction = False
        self.functionParams = None

    # def __eq__(self, __o: object) -> bool:
    #     return self.id == __o.id

    # def __hash__(self) -> int:
    #     return hash(("id", self.id))

    def __str__(self) -> str:
        return f"{self.id}\t{self.data_type}\t\t{self.return_type}\t\t{self.initial_value}\t\t{self.num_params}\t\t\t{self.type_of_params}"


def charInTokenDB(char: str) -> bool:
    return char.strip() in tokens["operators"] or char in tokens["relational"] or char in tokens["punctuation"]


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
        all_tokens = MAGIC_EXPRESSION.findall(line)

        lastDataType = ""
        symbol = Symbol()

        for index, token in enumerate(all_tokens):
            if token in tokens["keywords"]:
                symbol.data_type = token
                lastDataType = token

                # Verify if initial value matches the declared datatype
                try:
                    if (
                        lastDataType == "int"
                        and tryCast(all_tokens[index + 1], lastDataType)
                        != None
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
                # Datatype verification end ==============================
            else:
                symbol.id = all_tokens[1]
                # print(all_tokens[index])

            if len(FUNCTION_EXPRESSION.findall(line)) > 0:
                symbol.isFunction = True
                params = [
                    word for word in all_tokens if word in tokens["keywords"]]

                # -1 for compensating return type
                symbol.num_params = len(params) - 1
                symbol.type_of_params = params[:-1]
                symbol.initial_value = None
                symbol.return_type = symbol.data_type
                # symbol.data_type = None  # Uncommenting this line updates return_type for some reasons, uncomment and get wrkt

            # symbol.initial_value = all_tokens[-1]
            symbol_table.append(symbol)


symbol_table.reverse()
symbol_table = [
    symbol_table[i]
    for i in range(len(symbol_table))
    if symbol_table[i].id != None
]

symbol_table = [
    symbol_table[i]
    for i in range(len(symbol_table))
    if symbol_table[i].id != symbol_table[min(i+1, len(symbol_table)-1)].id
    or
    i == len(symbol_table)-1
]

print("ID\tData Type\tReturn Type\tInitial Value\tNo. of Parameters\tType of Paramameters", end="\n\n")
for symbol in symbol_table:
    print(symbol)
