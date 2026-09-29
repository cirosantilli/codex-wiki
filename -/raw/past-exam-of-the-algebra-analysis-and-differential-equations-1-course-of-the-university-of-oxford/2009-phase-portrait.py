"""Python 3.14; root Matplotlib/NumPy versions. Write PNG into CWD."""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1.2,1.2,350);y=np.linspace(-1.2,1.2,350);X,Y=np.meshgrid(x,y)
H=X**2+X*Y+Y**2+X**4/8
fig,ax=plt.subplots(figsize=(5,4.6),layout='constrained',facecolor='white')
ax.contour(X,Y,H,levels=[.04,.12,.25,.45,.7,1],colors='#1c73a4',linewidths=1.2)
for xx in [-.75,-.4,.4,.75]:
 yy=0;u=xx+2*yy;v=-2*xx-yy-xx**3/2;norm=np.hypot(u,v)
 ax.annotate('',xy=(xx+.12*u/norm,yy+.12*v/norm),xytext=(xx,yy),arrowprops={'arrowstyle':'->','color':'#bd4d26','lw':1.7})
ax.scatter([0],[0],s=22,color='black');ax.axhline(0,color='#777',lw=.4);ax.axvline(0,color='#777',lw=.4)
ax.set(xlabel='x',ylabel='y',title='Conserved levels around a nonlinear centre',xlim=(-1.15,1.15),ylim=(-1.15,1.15));ax.set_aspect('equal')
fig.savefig('2009-phase-portrait.png',dpi=155,facecolor='white')
