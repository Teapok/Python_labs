def pre_process(a):
 def real_decor(fn):
  def wrap(*args):
   s = args[0]
   for i in range(len(s)):
    s[i] = s[i]-a * s[i - 1]
   fn(s)
  return wrap
 return real_decor



@pre_process(a=0.93) 
def plot_signal(s):
 for sample in s:
  print(sample)
   
Arr = [1.0, 2.0, 3.0, 4.0 , 5.0] 
print(Arr,'\n')
plot_signal(Arr)	