import random

a = []
for linha in range(8):
    b = []
    for coluna in range(8):
        # b.append(int(input(f'informe a elemento [{linha}, {coluna} = ]')))
        b.append(random.randint(1,1))
    a.append(b)
print(a[linha][coluna])
for linha in range(8):
    c = 0
    for coluna in range(8):
        c = c + a[linha][coluna]
print(c)
for linha in range(8):
    c = 0
    for coluna in range(8):
        if a[linha][coluna] % 2 == 0:
            c = c + a[linha][coluna]
print(c)
for linha in range(8):
    c = 0
    for coluna in range(8):
        if a[linha][coluna] % 2 != 0:
            c = c + a[linha][coluna]
print(c)
