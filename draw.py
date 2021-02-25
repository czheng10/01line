from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #direction of line
    if x0 <= x1:
        x = int(x0)
        y = int(y0)
        xe = int(x1)
        ye = int(y1)
    else:
        x = int(x1)
        y = int(y1)
        xe = int(x0)
        ye = int(y0)
        
    #changes in x and y
    dx = xe - x
    dy = ye - y
   
    #Vertical line
    if (dx == 0):
        for y in range(y, ye+1):
            plot(screen, color, x, y)
            y+= 1
            
    #Horizontal line
    elif (dy == 0):
        for x in range(x, xe+1):
            plot(screen, color, x, y)
            x+= 1
            
    #Octant I and V
    elif (dy/dx <= 1 and dy/dx > 0):
        A = dy
        B = -dx
        d= 2*A + B
        while (x <= xe):
            plot(screen, color, x, y)
            if (d > 0):
                y+= 1
                d+= 2*B
            x+= 1
            d+= 2*A
            
    #Octant II and VI
    elif (dy/dx > 1):
        A = -dy
        B = dx
        d = 2*B + A
        while (y <= ye):
            plot(screen, color, x, y)
            if (d > 0):
                x+= 1
                d+= 2*A
            y+= 1
            d+= 2*B

    #Octant III and VII
    elif (-(dy/dx) > 1):
        A = -dy
        B = dx
        d = 2*B -A
        while (y >= ye):
            plot(screen, color, x, y)
            if (d > 0):
                x+= 1
                d+= -2*A
            y+= -1
            d+= 2*B
        
    #Octant IV and VIII
    else:
        A = dy
        B = -dx
        d = 2*A - B
        while (x <= xe):
            plot(screen, color, x, y)
            if (d < 0):
                y+= -1
                d+= -2*B
            x+=1
            d+= 2*A
            
