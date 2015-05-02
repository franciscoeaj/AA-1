cards = raw_input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())
 
while (cards != "0 0"):
    sub1 = len(set(a) - set(b))
    sub2 = len(set(b) - set(a))
 
    if (sub1 >= sub2):
        print sub2
    else:
        print sub1
         
    cards = raw_input()
    if (cards != "0 0"):
        a = map(int, raw_input().split())
        b = map(int, raw_input().split())