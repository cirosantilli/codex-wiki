"""Original Rossby-PV sketch. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Output basename in caller CWD; respects supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-np.pi,np.pi,360);y=np.linspace(-1.2,1.2,180)
X,Y=np.meshgrid(x,y);q=.35*np.cos(X);Q=Y+q
fig,ax=plt.subplots(figsize=(9,4.7),layout='constrained',facecolor='white')
cf=ax.contourf(X,Y,q,levels=np.linspace(-.35,.35,13),cmap='RdBu_r',alpha=.8)
cs=ax.contour(X,Y,Q,levels=np.arange(-1,1.1,.25),colors='black',linewidths=.8)
ax.clabel(cs,fontsize=8)
xx=np.linspace(-2.7,2.7,13)
ax.quiver(xx,np.zeros_like(xx),np.zeros_like(xx),.3*np.sin(xx),color='#174f2c',angles='xy',scale_units='xy',scale=1,width=.004)
ax.annotate('Westward phase propagation',xy=(-2.3,1.37),xytext=(.65,1.37),arrowprops={'arrowstyle':'->','lw':2},ha='center')
ax.text(.1,.7,'Positive PV anomaly\n(crest)',ha='center',fontsize=10)
ax.set(xlabel='Zonal coordinate kx (east →)',ylabel='Meridional coordinate (north →)',title='PV contours at fixed altitude: background gradient + wave anomaly',ylim=(-1.2,1.65))
fig.colorbar(cf,ax=ax,shrink=.8,label='PV anomaly (scaled)')
fig.savefig('paper-80-rossby-pv.png',dpi=110,facecolor='white',transparent=False)
