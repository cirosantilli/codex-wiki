"""Original explanatory calculation. Python 3.14, numpy and matplotlib.
Writes one literal PNG basename to cwd; no source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(9.4,4),layout='constrained');q=np.linspace(.005,1,170);X,Y=np.meshgrid(q,q)
a.streamplot(q,q,-Y,-X,color='#1766a5',density=.85,arrowsize=1.1);a.contour(X,Y,2*X*Y,levels=[.08,.25,.5,.9,1.3],colors='lightgray',linewidths=.8);a.set(xlim=(0,1),ylim=(0,1),xlabel='x (chosen units)',ylabel='y (chosen units)',title=r'Right-angle recess: $\mathbf{E}\propto(-y,-x)$');a.set_aspect('equal');a.plot([0,1],[0,0],color='black',lw=3);a.plot([0,0],[0,1],color='black',lw=3)
r=np.geomspace(.001,1,400);b.loglog(r,r,label='Vacuum angle π/2: slope +1');b.loglog(r,r**(-1/3),label='Vacuum angle 3π/2: slope −1/3');b.set(xlabel='Distance from corner (scaled)',ylabel='Field magnitude (normalized at r = 1)',title='Ideal corner asymptotics');b.legend(frameon=False,fontsize=9);b.grid(alpha=.15,which='both')
fig.savefig('paper-1-wedge-field.png',dpi=150);plt.close(fig)
