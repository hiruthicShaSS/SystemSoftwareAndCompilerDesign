tokens = {
    "keywords": ["int", "float", "double", "class", "struct"],
    "operators": ["=", "-", "+", "*", "/"],
    "relational": ["<=", ">=", "==", "!="],
    "punctuation": [",", ";"]
}

totalTokens = 0


with open("expression1.txt") as expression:
    lines = expression.readlines()

    # Parse data
    for line in lines:
        for i, word in enumerate(line.split()):
            if word in tokens["keywords"]:
                print(f"< {word} , keyword >")
            elif word in tokens["operators"]:
                print(f"< {word} , operator >")
            elif word.isnumeric():
                print(f"< {word} , Number >")
            elif word in tokens["punctuation"]:
                print(f"< {word} , Punctuation >")
            elif word in tokens["relational"]:
                print(f"< {word} , Relational >")
            else:
                print(f"< {word} , Identifier id-{i + 1} >")

            totalTokens += 1

print(f"TOTAL NUMBER OF TOKEN: {totalTokens}")
