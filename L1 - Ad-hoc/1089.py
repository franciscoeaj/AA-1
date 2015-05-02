n = int(raw_input())
 
while (n > 0):
    raw_h = raw_input()
 
    h = raw_h.split()
 
    peaks = 0
    for i in range(len(h)):
        actual = int(h[i])
 
        if (i == 0):
            previous = int(h[len(h) - 1])
        else:
            previous = int(h[i - 1])
             
        if (i == len(h) - 1):
            next = int(h[0])
        else:
            next = int(h[i + 1])
             
        if (actual > next and actual > previous) or (actual < next and actual < previous):
            peaks += 1
             
    print peaks
 
    n = int(raw_input())