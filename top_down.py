"""
Created on Fri Mar  8 18:43:17 2019

@author: Shashwat
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
threshold = 6
class topdown_segmentation:
    def __init__(self):
        datafile=pd.read_csv("ParadeToHomeLabelled.csv",header=0)
        index=datafile['index']
        speed=datafile['speed (m/s)']
        long=datafile['longitude']
        lat=datafile['latitude']
        print(np.var(speed))
        anchor_pts=list()
        self.topdown_seg(speed,anchor_pts,index,0,len(speed))
        anchor_pts=sorted(anchor_pts)
        print(len(anchor_pts))
        self.plot(anchor_pts,index,speed)
    def topdown_seg(self,speed,anchor_pts,index,lower_limit,upper_limit):
        final_anchor=0
        final_var_diff=0
        if (upper_limit-lower_limit)>3:
            for i in range(lower_limit+2,upper_limit-1):
                init_seg1_var=np.var(speed[lower_limit:i])
                init_seg2_var=np.var(speed[i:upper_limit])
                initial_var_diff=abs(init_seg1_var - init_seg2_var)
                if initial_var_diff > final_var_diff:
                    final_anchor=index[i]
                    final_var_diff=initial_var_diff
            if(final_var_diff > threshold):
                anchor_pts.append(final_anchor)
                self.topdown_seg(speed,anchor_pts,index,lower_limit,(final_anchor-1))
                self.topdown_seg(speed,anchor_pts,index,(final_anchor-1),upper_limit)
    def plot(self,anchor_pts,index,speed):
            for j in range(len(anchor_pts)+1):
                if (j==0)or(j==len(anchor_pts)):
                    if (j==0):
                        plt.plot(index[0:(anchor_pts[j]+2)],speed[0:(anchor_pts[j]+2)],linewidth=2)
                    else:
                        if(len(anchor_pts))%2==0:
                            plt.plot(index[(anchor_pts[j-1]+1):len(index)],speed[(anchor_pts[j-1]+1):len(speed)],linewidth=2)
                        else:
                            plt.plot(index[(anchor_pts[j-1]+1):len(index)],speed[(anchor_pts[j-1]+1):len(speed)],linewidth=2)
                elif (j%2)!=0:
                    plt.plot(index[(anchor_pts[j-1]+1):(anchor_pts[j]+2)],speed[(anchor_pts[j-1]+1):(anchor_pts[j]+2)],linewidth=2)
                else:
                    plt.plot(index[(anchor_pts[j-1]+1):(anchor_pts[j]+2)],speed[(anchor_pts[j-1]+1):(anchor_pts[j]+2)],linewidth=2)
            plt.title("Segmented Data Graph")
            plt.xlabel("Length of list (number)")
            plt.ylabel("Speed (meter/seconds)")
            plt.show()
ts=topdown_segmentation()       



