n = int(input('Введите число от 3 до 20 '))

cipher = ''
for i in range(1,n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            cipher += str(i)
            cipher += str(j)

print(n,' - ',cipher)
