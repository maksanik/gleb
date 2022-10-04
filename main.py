a, b, c = float(input()), float(input()), float(input())

D1 = b**2 - 4 * a * c

if D1 < 0:
    print("Нет решения")
elif D1 == 0:
    result = -b / (2*a)
    print(result)
else:
    D2 = D1 ** (1/2)
    x1 = (-b + D2)/(2*a)
    x2 = (-b - D2)/(2*a)
    print(x1, x2)