"""Original generic-physics figure; Python 3.14, numpy and matplotlib.
PNG basename output to cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(9,3.7),layout='constrained');x=np.linspace(0,2.5,400)
for drive in [1,2,4]:a.plot(x,x-drive*x*x/2,label='Scaled qE = '+str(drive))
a.set(xlabel='Inserted contour (chosen units)',ylabel='Free energy (chosen units)',title='Entropic entry barriers; chosen f = 1',ylim=(-2,1));a.legend(frameon=False,fontsize=8)
L=np.linspace(0,3,300);b.plot(L,L,label='Entry ∝ L');b.plot(L,.5*L*L,label='Recoil ∝ L²');b.set(xlabel='Contour length (scaled)',ylabel='Time (separately chosen units)',title='Ideal local-drag scaling after capture');b.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-polymer-channel.png',dpi=150);plt.close(fig)
