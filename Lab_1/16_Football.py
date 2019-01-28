import datetime
import itertools
Teams = list(set(['Team1','Team2','Team3','Team4','Team5','Team6','Team7','Team8',
'Team9','Team10','Team11','Team12','Team13','Team14','Team15','Team16',]))
#print(Teams)
Groups = [Teams[0: 4], Teams[4: 8], Teams[8: 12], Teams[12: 16]]
print(Groups,'\n')
print ('Состав группы 1:',Groups[0])
print ('Состав группы 2:',Groups[1])
print ('Состав группы 3:',Groups[2])
print ('Состав группы 4:',Groups[3],'\n')

a = datetime.datetime(2019, 9, 20)
b = datetime.timedelta(days=14)
TeamA=0; TeamB=0;

while a<=datetime.datetime(2020, 4, 14):
    a=a+b
    if (TeamB<15):
        print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(Teams[TeamA]) +'  &  '+ str(Teams[TeamB+1] ) )
        TeamA+=1
        TeamB+=1
    else:
        print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ')