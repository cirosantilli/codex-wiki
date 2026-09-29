"""Python 3.14; numpy 2.3; matplotlib 3.10. Output is written to the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.8,5),layout='constrained',facecolor='white')
t=np.linspace(.001,3,1500)
xb=2*t-3*np.cbrt(t)
ax.fill_betweenx(t,-1,xb,where=t>=1,color='#d6d6d6',label='wall-affected region')
for j,speed in enumerate(np.linspace(-.9,1.8,9)):
    x=speed*t;valid=(x>=-1)&((t<=1)|(x>=xb))
    ax.plot(np.where(valid,x,np.nan),t,color='#6eafaa',lw=1,label='minus characteristics' if j==0 else None)
for j,tau in enumerate([.06,.16,.32,.52,.75]):
    tt=np.linspace(tau,3,500);xx=2*tt-3*tau**(2/3)*tt**(1/3)
    ax.plot(xx,tt,color='#1767a3',lw=1.2,label='plus characteristics' if j==0 else None)
ax.plot(xb[t>=1],t[t>=1],color='#ad3329',lw=2.3,label='first changed plus characteristic')
ax.plot(2*t,t,color='black',lw=1.6,label='dry front')
ax.plot([-1,0],[1,0],color='black',ls='--',lw=1,label='rarefaction head')
ax.axvline(-1,color='black',lw=2)
ax.plot(-1,1,'o',color='#ad3329');ax.annotate('first wall arrival',(-1,1),xytext=(.05,.8),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlabel=r'$x/a$',ylabel=r'$c_0t/a$',xlim=(-1.25,6.2),ylim=(0,3))
ax.grid(alpha=.15);ax.legend(frameon=False,fontsize=8,loc='upper left')
fig.savefig(Path.cwd()/'2010-dam-break-characteristics.png',dpi=150,facecolor='white')
