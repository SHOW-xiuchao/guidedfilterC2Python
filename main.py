import cv2 
import numpy as np 
import guidedfilter

def guidedFilter(I,p,r,eps,depth=-1):
    I = np.array(I)
    p = np.array(p)
    data,h,w,c = guidedfilter.guidedFilter(I.shape[0],I.shape[1],I.shape[2],I.tostring(),p.shape[0],p.shape[1],p.shape[2],p.tostring(),r,eps,depth)
    out = np.array(list(data)).reshape((h,w,c))
    return out

I = np.array(cv2.imread("../resource/cave-flash.png"))

p = np.array(cv2.imread("../resource/cave-noflash.png"))

# r = 8
# eps = 0.02 * 0.02 * 255 * 255
# depth = -1

# data = guidedfilter.guidedFilter(I.shape[0],I.shape[1],I.shape[2],
# I.tostring(),p.shape[0],p.shape[1],p.shape[2],p.tostring(),r,eps,depth)

# out = np.array(list(data)).reshape(I.shape)

out = guidedFilter(I,p,r=8,eps=0.02*0.02*255*255)

cv2.imwrite('out.png',out)