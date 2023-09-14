operation = int(input(f"1) Сложение \n2) Вычитание \n3) Умножение \n4) Деление \nВыберите операцию:" ))
fn = int(input("Введите первое число: "))
sn = int(input("Введите первое число: "))
if (operation == 1):
    res = fn + sn
    print(f"Результат: {res}")
elif (operation == 2):
    res = fn - sn
    print(f"Результат: {res}")
elif (operation == 3):
    res = fn * sn
    print(f"Результат: {res}")
elif (operation == 4):
    if(sn == 0):
        print("На ноль делить нельзя!")
    else:
        res = fn / sn
        print(f"Результат: {res}")
