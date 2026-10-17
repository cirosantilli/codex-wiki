"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Output is a PNG basename in cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(8.5,3.8),layout='constrained');a.add_patch(Circle((0,0),1.7,fill=False,lw=2));a.add_patch(Circle((0,0),1,facecolor='#dedede',edgecolor='black'));a.annotate('',(1,0),(0,0),arrowprops=dict(arrowstyle='->'));a.text(.5,.1,'Ri');a.text(1.4,.85,'Ro');a.text(0,-.5,'rotating bob',ha='center');a.text(0,1.9,'stationary cup',ha='center');a.set(xlim=(-2.1,2.1),ylim=(-2.1,2.3),title='Coaxial-cylinder cross section');a.set_aspect('equal');a.axis('off')
r=np.linspace(1,1.7,300);v=(1.7**2/r-r)/(1.7**2-1);g=2*1.7**2/((1.7**2-1)*r*r);b.plot(r,v,label='vθ/(ΩRi)');b.plot(r,g/g[0],label='Shear rate / inner-wall rate');b.set(xlabel='r/Ri',ylabel='Scaled profile',title='Illustration: Ro/Ri = 1.7');b.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-couette.png',dpi=150);plt.close(fig)
