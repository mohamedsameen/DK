import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pymatreader import read_mat


#import matlab vectors
#FV
dict1=read_mat('C:\\Users\\b1044271\\Desktop\\Sodium\\Projects\\Paper\\2021\\Results\\ERPs\\FV_EDF_KClocked.mat')
cond1=dict1['FV_KCl_EDF']
mean1=np.mean(cond1,0)
sem1=stats.sem(cond1,0)
cond1_ar=np.asarray(cond1)
#UFV
dict2=read_mat('C:\\Users\\b1044271\\Desktop\\Sodium\\Projects\\Paper\\2021\\Results\\ERPs\\UFV_EDF_KClocked.mat')
cond2=dict2['UFV_KCl_EDF']
mean2=np.mean(cond2,0)
sem2=stats.sem(cond2,0)
cond2_ar=np.asarray(cond2)
