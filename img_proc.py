import numpy as np
import cv2

def segment_avg_rgb(r,g,b, left_top_idx, right_bottom_idx):

    seg = r[left_top_idx[0] : right_bottom_idx[0], left_top_idx[1] : right_bottom_idx[1]]
    r_avg = np.average( r[left_top_idx[0] : right_bottom_idx[0], left_top_idx[1] : right_bottom_idx[1]] )
    g_avg = np.average( g[left_top_idx[0] : right_bottom_idx[0], left_top_idx[1] : right_bottom_idx[1]] )
    b_avg = np.average( b[left_top_idx[0] : right_bottom_idx[0], left_top_idx[1] : right_bottom_idx[1]] )
    
    return r_avg, g_avg, b_avg


def point_avg_rgb(r,g,b, point, seg_range):
    return segment_avg_rgb(r,g,b,[point[0]-seg_range,point[1]-seg_range],[point[0]+seg_range,point[1]+seg_range])

def get_picture(img):
    img_color = cv2.imread(img)
    b, g, r = cv2.split(img_color)
    return r,g,b