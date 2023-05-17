import random

a = []
c = 0
for linha in range(5):
    b = []
    for coluna in range(5):
        # b.append(int(input(f'informe a elemento [{linha}, {coluna} = ]')))
        b.append(random.randint(1, 1))
    a.append(b)
for linha in range(5):
    for coluna in range(5):
        c = c + a[linha][coluna]
print(c)
