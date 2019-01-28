#--------copy for explain: проба,Текста для, Теста

import re

Vstr = (str(input('Введите строку: \n')))
Buff = (re.sub('\W', ' ', Vstr).split())
for i in range(len(Buff)):
    if ((Buff[i])[0]).isupper():
        Buff[i] = Buff[i].upper()
print(' '.join(Buff))