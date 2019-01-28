import random

value = random.randint(1, 100)
rnd_value_for_list = [random.randint(1, 100) for _ in range(value)]

num = 2
while num < value:	print('debug',num);	num *= 2;

rnd_value_for_list += [0] * (num - value)

print("\n",rnd_value_for_list,"\n")
print('Min/start value =', value)
print('Длина списка:', len(rnd_value_for_list))
print('Количество нулей:',rnd_value_for_list.count(0))