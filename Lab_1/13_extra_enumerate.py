def extra_enumerate(InputArr, start=0, sum=0): #elem, sum, frac
    for elem in InputArr:
        yield start, elem
        start += 1
        sum = sum + elem
        print('(',start,', ',elem,', ',sum,', ',sum/10,')')# wut?


Arr  = [1,3,4,2]
print ('( id, num, sum, sum/10 )')
for i in extra_enumerate(Arr):
    print() # wut? x2