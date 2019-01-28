def non_empty(func,buff=[]):
 def wrapper():
  buff.clear()
  # print(len(func()))
  for i in range(len(func())):
   if ((func()[i])) == "":
    pass
    # print(i)
   else:
    buff.insert(i,func()[i])
    # print(buff)
  return buff
 return wrapper



@non_empty
def get_page():
 return ['chapter1', '', 'contents', '' , 'line1']

print(get_page())
