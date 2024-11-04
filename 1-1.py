#ymai = input("как вас зовут?")
#print("Добро пожаловать в Data Science!", ymai)

#a = 199/4111
#print('%.3f'  % a)


#print("A = {0}, B = {1}, C = {2}".format(3,2,1,))
'''
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))


maximum = max(a, b, c)
minimum = min(a, b, c)
srednia = a + b + +c -maximum - minimum

print(maximum)
print(minimum)
print(srednia)
'''




biletik = list(input("Введите число: "))

if int(biletik[0])+ int(biletik[1]) +int(biletik[2]) == int(biletik[3])+int(biletik[4])+int(biletik[5]):
    print("Билет счастливый")
else:
     print("Билет не счастливый")