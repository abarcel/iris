from src.gaussian_kernel import gaussian_kernel
from src.circle_perimeter import circle_perimeter

import cv2
import numpy as np
from skimage.morphology import disk, opening

class DIED(): #DIED: Daugman Iris Edge Detection
    def __init__(self, image, r_min=40, r_max=62, open_=3, c_type='half'):
        if image.ndim == 3:
            self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            self.image = image
        self.r_min, self.r_max = r_min, r_max
        self.image_open = opening(self.image, disk(open_))
        self.c_type = c_type
        self.gk = gaussian_kernel(3, 1, 1)
        
    def differential(self, x, y):
        values = []
    
        for r in np.arange(self.r_min, self.r_max):
            rr, cc = circle_perimeter(x, y, r, self.c_type)
            values.append(np.sum(self.image_open[rr, cc]) / rr.shape[0])
        
        values = np.array(values)
        diff_values = np.diff(values)
        GoD = np.convolve(diff_values, self.gk) #GoD : Gaussian of Difference
        
        return np.max(GoD), np.argmax(GoD) + self.r_min
    
    def search(self, cen_x, cen_y, range_, step):
        all_values = []
        for x in np.arange(-range_, range_+1, step):
            for y in np.arange(-range_, range_+1, step):
                try:
                    value, radius = self.differential(x+cen_x, y+cen_y)
                    all_values.extend([x+cen_x, y+cen_y, np.round(value), radius])
                except:
                    pass
                
        all_values = np.array(all_values).reshape(-1, 4)
        
        return all_values[all_values[:,2].argsort()].astype(np.int16)
    
    def result(self):
        range_ = int(np.min([int(s/2) for s in self.image.shape])*0.40)
        cen_x, cen_y = [int(s/2) for s in self.image.shape]
        
        fuzzy_max = self.search(cen_x, cen_y, range_, 3)[-1]
  
        cen_x, cen_y = fuzzy_max[0], fuzzy_max[1]
    
        info = np.array([])
    
        for i in np.arange(2): 
            try:
                circle_max = self.search(cen_x, cen_y, 2+i, 1)[-1]
                circle = circle_perimeter(circle_max[0], circle_max[1], circle_max[3], 'full')
                self.image[circle] = 255
            except:
                info = np.append(info, [0,0,0,0])
                return self.image, info
            
            if i == 0:
                info = np.append(info, circle_max)
                self.r_min, self.r_max = np.ceil(0.1*circle_max[3]), np.ceil(0.8*circle_max[3])   

        return self.image, info

