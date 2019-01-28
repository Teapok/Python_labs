def frange(start,stop=None,step=None):
 if stop == None:
        stop = start + 0.0
        start = 0.0
 if step == None:
        step = 1.0
 while True:
  if step > 0 and start >= stop:
            break
  elif step < 0 and start <= stop:
            break
  yield ("%g" % start) # return float number
  start = start + step



for i in frange(-0.1, -0.5, -0.1):
    print (i, end=", ")