import random

a = []
c = []
for linha in range(3):
    b = []
    for coluna in range(4):
        # b.append(int(input(f'informe a elemento [{linha}, {coluna} = ]')))
        b.append(random.randint(1,1))
    a.append(b)
for linha in range(3):
    b = []
    for coluna in range(4):
        b.append(a[linha][coluna] * 3)
    c.append(b)
print(a)
print(c)