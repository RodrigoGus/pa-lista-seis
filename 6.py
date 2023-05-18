import random

a = []
for linha in range(10):
    b = []
    for coluna in range(5):
        # b.append(int(input(f'informe a elemento [{linha}, {coluna} = ]')))
        b.append(random.randint(0,10))
    a.append(b)
for linha in range(10):
    for coluna in range(5):
        print(a[linha][coluna], end=', ')
    print()
for linha in range(10):
    b = []
    for coluna in range (5):
