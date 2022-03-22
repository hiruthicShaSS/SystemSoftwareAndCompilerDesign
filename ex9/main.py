stack = []
table = open("table.txt", "r").readlines()
b = table[2].split(" ")
l = 0

st = list(table[0].split())
ky = list(table[1].split())
k = [0 for _ in range(len(st))]

for i in range(len(st)):
    k[i] = [0 for _ in range(len(ky))]

    for j in range(len(ky)):
        k[i][j] = b[l]
        l += 1


def display() -> None:
    s = "".join(stack)
    v = "".join(x)
    print(s.ljust(10)+v.ljust(10))


stack.append("$")
stack.append(st[0])

x = input("Enter the string: ")+" $"

for i in x:
    if i in ky:
        continue
    if i == " ":
        continue
    x = x.replace(i, "id")

x = x.split()

try:
    while True:
        while x[0] != stack[-1]:
            display()

            m = ""
            m = k[st.index(stack[-1])][ky.index(x[0])]

            if m == "e":
                print(f'{stack[-1]}------>{m}')
                stack.pop()
                continue

            print(f'{stack[-1]}------>{m}')
            stack.pop()

            if m == x[0]:
                stack.append(m)
            else:
                for j in m[::-1]:
                    stack.append(j)

        if x[0] == stack[-1]:
            display()

            if x[0] == "$" and stack[-1] == "$":
                print("Expression accepted by Grammar!")
                break

            stack.pop()
            x.pop(0)

except ValueError:
    print("Expression is not accepted by Grammar!")
