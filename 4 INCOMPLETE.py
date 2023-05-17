import random

a = []
for linha in range(5):
    b = []
    for coluna in range(5):
        # b.append(int(input(f'informe a elemento [{linha}, {coluna} = ]')))
        b.append(random.randint(1, 1))
    a.append(b)
print(a)
for linha in range(5):
    c = 0
    for coluna in range(5):
        if (linha + coluna) % 2 == 0:
            c = c + a[linha][coluna]
print(c)
for linha in range(5):
    c = 0
    for coluna in range(5):
        if (linha + coluna) % 2 != 0:
            c = c + a[linha][coluna]
print(c)
for linha in range(5):
    c = 0
    for coluna in range(5):
        if (linha + coluna) % 2 == 0:
            c += 1
print(c)
for linha in range(5):
    c = 0
    for coluna in range(5):
        if (linha + coluna) % 2 != 0:
            c += 1
print(c)
