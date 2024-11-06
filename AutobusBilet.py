biletik = list(input("введите номер своего билета  ")) #тут вводим сразу 6цифр билета без пробела
if int(biletik[0]) +int(biletik[1]) + int(biletik[2]) == int(biletik[3]) +int(biletik[4]) + int(biletik[5]):  #задаем условие дл того чтобы понять счастливый билет или же нет
    print('Счастливый')
else:
    print('Обычный')




