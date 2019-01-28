Dosh = {5000: 5, 1000: 20, 500: 20, 100: 80} #63000
client = int(input("Введите желаемую сумму для выдачи: "))
_5k = 0;_1k=0;_500=0;_100=0;

while client>=1:
 # print(client)
 if client >= 5000 and Dosh.get(5000)>0:
  Dosh[5000] -= 1
  _5k += 1
  client -= 5000
 elif client >= 1000 and Dosh.get(1000)>0:
   Dosh[1000] -= 1
   _1k += 1
   client -= 1000
 elif client >= 500 and Dosh.get(500)>0:
   Dosh[500] -= 1
   _500 += 1
   client -= 500
 elif client >= 100 and Dosh.get(100)>0:
   Dosh[100] -= 1
   _100 += 1
   client -= 100
 else: print("Операция не может быть выполнена!"); raise SystemExit(1);
print('{0}*5000 + {1}*1000 + {2}*500 + {3}*100'.format(_5k,_1k,_500,_100))