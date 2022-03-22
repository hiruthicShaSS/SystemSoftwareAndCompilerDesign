OPERATORS = {'+', '-', '*', '/', '(', ')'}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


def decorator(callback):

    def call(*args):
        print("=" * 11, "Code Generation", "=" * 11)
        callback(*args)
        print("=" * 39, end="\n\n")

    return call


def infix_to_postfix(expression) -> str:
    stack = []
    output = ""

    for char in expression:
        if char not in OPERATORS:
            output += char
        elif char in ["(", ")"]:
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()  # Pop opening paranthesis
        else:
            while stack and stack[-1] != "(" and PRIORITY[char] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output


@decorator
def generateAC():
    # Generate the postfix equivelent expression for the input expression
    postfix_expression = infix_to_postfix(expression)

    expression_stack = []
    t = 1

    for char in postfix_expression:
        if char not in OPERATORS:
            expression_stack.append(char)
        else:
            print(f't{t} = {expression_stack[-2]} {char} {expression_stack[-1]}')
            expression_stack = expression_stack[:-2]
            expression_stack.append(f't{t}')
            t += 1


expressions = open("input.txt", "r").readlines()

for expression in expressions:
    expression = expression.strip()

    print(f"Expression: {expression}")
    generateAC()
