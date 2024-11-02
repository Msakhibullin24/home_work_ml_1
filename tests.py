biletik = list(input("введите номер своего билета  "))
if int(biletik[0]) +int(biletik[1]) + int(biletik[2]) == int(biletik[3]) +int(biletik[4]) + int(biletik[5]):
    print('Счастливый')
else:
    print('Несчастливый')