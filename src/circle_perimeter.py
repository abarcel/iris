import numpy as np

def circle_perimeter(X, Y, R, c_type='half'): #Bresenham Method
    aa, bb = [], []
    dp = 3-(2*R)
    a, b = 0, R

    while a <= b:
        if c_type == 'half':
            aa.extend([a, a, -a, -a])
            bb.extend([b, -b, b, -b])
        else:
            aa.extend([a, -a, a, -a, b, -b, b, -b])
            bb.extend([b, b, -b, -b, a, a, -a, -a])

        if dp > 0:
            b -= 1
            dp += 4*(a-b)+10         
        else:
            dp += 4*a+6
        a += 1
   
    return X+np.array(aa, dtype=np.int16), Y+np.array(bb, dtype=np.int16)

