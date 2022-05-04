alfavit_eu =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = int(input('Введите число для шифрования в диапазоне [0,25) -> '))
assert key in range(0, 25), ('Число находится вне диапазона')
lang = input('Выберите язык RU/EU: ')
message = input("Сообщение для шифровки: ").upper()
itog = ''
if lang == 'ru':
    for i in message:
        mesto = alfavit_ru.find(i)
        new_mesto = mesto + key
        if i in alfavit_ru:
            itog += alfavit_ru[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_eu.find(i)
        new_mesto = mesto + key
        if i in alfavit_eu:
            itog += alfavit_eu[new_mesto]
        else:
            itog += i
print (itog)