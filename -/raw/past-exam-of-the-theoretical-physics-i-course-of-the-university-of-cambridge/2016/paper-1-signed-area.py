"""Original explanatory plot. Tested with Python 3.14, NumPy and Matplotlib.
Write the PNG basename into the current working directory (Make mirrors it).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
t=np.linspace(0,2*np.pi,1500); r=.5; x=1.5+r*np.cos(t); y=r*np.sin(t)
integrand=x*r*np.cos(t)+y*r*np.sin(t)
z=-np.concatenate(([0.],np.cumsum((integrand[1:]+integrand[:-1])*.5*np.diff(t))))
fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
a=axs[0];a.fill(x,y,color='#d9ecfc');a.plot(x,y,color='#245d91',lw=2)
for j in [300,1000]:a.annotate('',xy=(x[j+40],y[j+40]),xytext=(x[j],y[j]),arrowprops={'arrowstyle':'->','color':'#245d91','lw':2})
a.scatter(x[0],y[0],color='#b23a32',zorder=3);a.text(1.5,0,r'$A=\pi/4$',ha='center');a.set(xlabel='x',ylabel='y',title='Closed transverse projection',aspect='equal',xlim=(0,2.2),ylim=(-.8,.8));a.axhline(0,color='.8',lw=.6)
a=axs[1];a.plot(t/(2*np.pi),z,color='#7c3f8c',lw=2);a.axhline(-np.pi/2,color='.6',ls='--',lw=1);a.text(.37,-.15,r'$\Delta z=-2A/b=-\pi/2$',fontsize=11);a.set(xlabel='Fraction of counterclockwise circuit',ylabel='Axial displacement z',title='Geometric integral, illustrative b = 1');a.grid(alpha=.2)
fig.savefig('paper-1-signed-area.png',dpi=150,facecolor='white');plt.close(fig)
