
Input = int(input('введите пароль (16 цифр): '))

def separate(x):
    r=[x%10]
    while x>10:
        x=int(x/10)   
        r.insert(0,x%10)        
    return r

Pass=[]
Pass.extend(separate(Input))
i=0
while i<16:
	if i>3 and i<12:
	 Pass.pop(i)
	 Pass.insert(i,"*")
	 i+=1
	 continue
	i+=1
print(''.join(map(str,Pass)))

# number = input('Write number: ')
# print(number[:4] + ' **** **** ' + number[-4:]) ------------------------ Сделал а потом увидел "Краткая теоретическая справка", пусть тут будет, чтобы не потерять