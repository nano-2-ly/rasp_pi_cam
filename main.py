import cv2
import numpy as np 
from matplotlib import pyplot as plt 
from img_proc import *

seg_range = 5

r,g,b = get_picture('pic2.jpg')
point1 = [1869,313] # [세로, 가로]
point2 = [1818,2232]
point3 = [1828,2242]

r1, g1, b1 = point_avg_rgb(r,g,b, point1, seg_range)
r2, g2, b2 = segment_avg_rgb(r,g,b, point2, point3)
print(r1, g1, b1)
print(r2, g2, b2)