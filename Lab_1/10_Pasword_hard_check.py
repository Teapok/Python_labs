import time
import collections

Password = str(input("Введите пароль: "))
Qual = {-2:'Awful',-1:'Bad',0:'Easy', 1:'Regular', 2:'Medium', 3:'Hard',4:'Excelent'}; Strenght = 1; Num = set('0123456789'); Spec = set('#@.,-_=+!')

def Dupe_check(item):
    return [item for item, count in collections.Counter(Password).items() if count > 1]

if Password.isupper() == True: Strenght+=1
if len(Password) >11: Strenght+=2
elif len(Password)<6: Strenght -=1
if any((c in Spec) for c in Password): Strenght+=1
if Password.isdigit() == True: Strenght-=1
if len(str(Dupe_check(Password))) >2 and len(str(Dupe_check(Password))) <6 : Strenght-=1
print(Qual.get(Strenght))
time.sleep(2)