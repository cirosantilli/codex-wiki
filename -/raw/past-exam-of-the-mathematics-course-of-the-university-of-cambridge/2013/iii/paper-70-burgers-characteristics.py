"""Negative-flux Burgers characteristics. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.
Run in the desired output directory. Preserve any caller-supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':9,'axes.titlesize':11,'axes.labelsize':10})
fig,axes=plt.subplots(1,2,figsize=(8.4,4.2),dpi=100,facecolor='white')
z=np.linspace(0,2.4,241)
for ax in axes:
    ax.set_facecolor('white')
    ax.set_xlim(-1.8,3.1)
    ax.set_ylim(0,2.4)
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel(r'$z$')
    ax.grid(alpha=.17)
    ax.axhline(0,color='black',lw=.7)
left,right=axes
for t0 in np.linspace(-1.6,-.12,10):
    zz=z[z<=min(2.4,-2*t0)]
    left.plot(np.full_like(zz,t0),zz,color='#277da8',lw=.9)
for t0 in np.linspace(.12,2.9,16):
    zz=z[z<=min(2.4,2*t0)]
    left.plot(t0-zz,zz,color='#ba5c27',lw=.9)
left.plot(-z/2,z,color='#222222',lw=2.4,label=r'shock $\theta=-z/2$')
left.set_title(r'$U=1$: characteristics enter a shock')
left.legend(loc='upper right',framealpha=1,facecolor='white',fontsize=8)
left.text(-1.65,2.22,r'$f=0$',color='#277da8')
left.text(.45,1.75,r'$f=1$',color='#ba5c27')
for t0 in np.linspace(-1.6,-.12,10):right.plot(np.full_like(z,t0),z,color='#277da8',lw=.9)
for t0 in np.linspace(.12,2.9,16):right.plot(t0+z,z,color='#ba5c27',lw=.9)
for speed in np.linspace(0,1,13):right.plot(speed*z,z,color='#40834c',lw=.85)
right.plot(np.zeros_like(z),z,color='#222222',lw=1.5)
right.plot(z,z,color='#222222',lw=1.5)
right.set_title(r'$U=-1$: separating characteristics form a fan')
right.text(-1.6,2.2,r'$f=0$',color='#277da8')
right.text(.44,1.25,r'$f=-\theta/z$',color='#286038',rotation=29,
           bbox={'facecolor':'white','edgecolor':'none','alpha':1,'pad':2})
right.text(2.35,1.55,r'$f=-1$',color='#ba5c27')
fig.subplots_adjust(left=.07,right=.985,bottom=.14,top=.88,wspace=.22)
fig.savefig('paper-70-burgers-characteristics.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
