a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

maximalka = max(a, b, c)#максимальное значение тут считаем в общем
minimalka = min(a, b, c)#минимальное значение тут ищем из всех
seredina = a + b + c - maximalka - minimalka #тут уже ищем оставшееся число чтобы его напечатать

print(maximalka)
print(minimalka)
print(seredina)
