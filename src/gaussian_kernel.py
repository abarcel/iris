import numpy as np

def gaussian_kernel(size, sigma, dimension):
    gk = np.empty([size])
    resizer = np.array([size])
    
    for i in range(size):
        gk[i] = (1/(((2*np.pi)**0.5)*sigma))*np.exp(-((i-(size-1)/2)**2/(2*sigma**2)))
        
    for x in range(dimension-1):
        resizer = np.insert(resizer,0,1)
        gk_d = gk.reshape(resizer)
        gk = np.outer(gk_d, gk)

    return gk / np.sum(gk)

