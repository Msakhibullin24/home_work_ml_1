################### задание 1

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

maximum = max(a, b, c)
minimum = min(a, b, c)
seredina = a + b + c - maximum - minimum


print(maximum)
print(minimum)
print(seredina)
################### задание 2
biletik = list(input("введите номер своего билета  "))
if int(biletik[0]) +int(biletik[1]) + int(biletik[2]) == int(biletik[3]) +int(biletik[4]) + int(biletik[5]):
    print('Счастливый')
else:
    print('Обычный')