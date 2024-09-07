x,y,z = input("enter an arthimetic expression: ").split(" ")

if y == "+":
    solution = float (x) + float (z)
elif y == "-":
    solution = float (x) - float (z)
elif y == "*":
    solution = float (x) * float (z)
elif y == "/":
    solution = float (x) / float (z)

print(solution)
