import random

a = []
for linha in range(10):
    b = []
    for coluna in range(10):
        # b.append(int(input(f'informe a elemento [{linha}, {coluna} = ]')))
        b.append(random.randint(1, 1))
    a.append(b)
c = 0
for linha in range(10):
    for coluna in range(10):
        if (linha + coluna) % 2 == 0:
            c = c + a[linha][coluna]
print(c)
c = 0
for linha in range(10):
    for coluna in range(10):
        if (linha + coluna) % 2 != 0:
            c = c + a[linha][coluna]
print(c)
c = 0
for linha in range(10):
    for coluna in range(10):
        if a[linha][coluna] % 2 == 0:
            c += 1
print(c)
c = 0
for linha in range(10):
    for coluna in range(10):
        if a[linha][coluna] % 2 != 0:
            c += 1
print(c)