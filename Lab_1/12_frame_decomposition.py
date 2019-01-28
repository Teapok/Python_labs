def get_frames(signal,size,overlap):

    x = signal
    step = size * overlap
    print ('Step:',step,'  Size:',size,'   Signal lenght:',len(signal))
    i = 0
    while i<len(signal):
        print (signal[i:i+size]) #[--]----- => --[--]---
        i = i + int(step)


size = 10
signal = [i for i in range(0,1024)]
overlap = 0.5

get_frames(signal,size,overlap)