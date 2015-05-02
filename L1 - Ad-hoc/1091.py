k = int(raw_input())
center = raw_input().split()
 
center_x = int(center[0])
center_y = int(center[1])
 
while (k > 0):
    for i in range(k):
        coord = raw_input().split()
        coord_x = int(coord[0])
        coord_y = int(coord[1])
 
        if (coord_x == center_x or coord_y == center_y):
            result = "divisa"
 
        if (coord_y > center_y):
            if (coord_x > center_x):
                result = "NE"
 
            if (coord_x < center_x):
                result = "NO"
 
        if (coord_y < center_y):
            if (coord_x > center_x):
                result = "SE"
 
            if (coord_x < center_x):
                result = "SO"
 
        print result
 
    k = int(raw_input())
    if (k > 0):
        center = raw_input().split()
 
        center_x = int(center[0])
        center_y = int(center[1])