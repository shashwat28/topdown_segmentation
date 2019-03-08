"""
Created on Fri Mar  8 18:43:17 2019

@author: Shashwat
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
class topdown_segmentation:
    def __init__(self):
        datafile=pd.read_csv("ParadeToHomeLabelled.csv",header=0)
        index=datafile['index']
        speed=datafile['speed (m/s)']
        print(np.var(speed))
        anchor_pts=list()
        self.topdown_seg(speed,anchor_pts)
        anchor_pts=sorted(set(anchor_pts))
        self.plot(anchor_pts,index,speed)
        print(anchor_pts)
    def topdown_seg(self,speed,anchor_pts):
        data_length=len(speed)
        final_anchor=0
        final_var_diff=0
        if data_length>3:
            for i in range(2,data_length-1):
                init_seg1_var=np.var(speed[0:i])
                init_seg2_var=np.var(speed[i:data_length])
                initial_var_diff=abs(init_seg1_var-init_seg2_var)
                if initial_var_diff>final_var_diff:
                    final_anchor=i
                    final_var_diff=initial_var_diff
            if(final_var_diff>2):
                anchor_pts.append(final_anchor)
                self.topdown_seg(speed[0:final_anchor+1],anchor_pts)
                self.topdown_seg(speed[final_anchor+1:data_length],anchor_pts)
    def plot(self,anchor_pts,index,speed):
        for j in range(len(anchor_pts)+1):
            if (j==0)or(j==len(anchor_pts)):
                if (j==0):
                    plt.plot(index[0:(anchor_pts[j]+1)],speed[0:(anchor_pts[j]+1)],'g')
                else:
                    if(len(anchor_pts))%2==0:
                        plt.plot(index[(anchor_pts[j-1]+1):len(index)],speed[(anchor_pts[j-1]+1):len(speed)],'g')
                    else:
                        plt.plot(index[(anchor_pts[j-1]+1):len(index)],speed[(anchor_pts[j-1]+1):len(speed)],'y')
            elif (j%2)!=0:
                plt.plot(index[(anchor_pts[j-1]+1):(anchor_pts[j]+1)],speed[(anchor_pts[j-1]+1):(anchor_pts[j]+1)],'y')
            else:
                plt.plot(index[(anchor_pts[j-1]+1):(anchor_pts[j]+1)],speed[(anchor_pts[j-1]+1):(anchor_pts[j]+1)],'g')
        plt.show()
ts=topdown_segmentation()    

    


