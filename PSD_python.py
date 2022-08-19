# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 09:25:12 2022

@author: robin
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy
import math

U_flc_filt=np.loadtxt('10.72_mpersec_spro.txt')
U_flc_filt=U_flc_filt-np.mean(U_flc_filt)
SR=20000
temp=len(U_flc_filt)
pow2=np.fix(math.log2(temp))
n_fft=2**(pow2-5)
PSD=scipy.signal.welch(U_flc_filt, fs=SR, window='hann', nperseg=n_fft/8, noverlap=None, nfft=n_fft)
      
f=PSD[0][:]            
p=PSD[1][:]
plt.loglog(f,p)                   
