try:
 Money = float(input('введите не целое число: '))
 
 if Money < 0:
  raise TypeError
 print(int(Money),'руб.',int((Money - int(Money))*100),'коп.')
except TypeError:
 print('Некорректный формат!')
except:
 print('Вводите только числа! Или используйте точку вместо запятой')
# rub = int(Money)
# kop = int((Money - int(Money))*100)
#print(rub, 'руб.', kop, 'коп.')