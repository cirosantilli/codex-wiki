"""Original sketch. Python 3.14, numpy 2.3, matplotlib 3.10.
Output is a basename in caller CWD; caller MPLCONFIGDIR is preserved.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
F=1.4
hf=4/(F+2)**2
uf=2*F/(F+2)
xs=2*(F-1)/(F+2)
x=np.linspace(-1.6,1.2,900)
h=np.where(x<-1,1,np.where(x<xs,(2-x)**2/9,np.where(x<uf,hf,0)))
u=np.where(x<-1,0,np.where(x<xs,2*(1+x)/3,np.where(x<uf,uf,np.nan)))
fig,ax=plt.subplots(1,3,figsize=(12,3.5),layout='constrained',facecolor='white')
for a,y,label in zip(ax[:2],[h,u],[r'$h/H$',r'$u/c_0$']):
    a.plot(x,y,lw=2)
    a.axvline(-1,color='gray',ls=':')
    a.axvline(xs,color='gray',ls=':')
    a.axvline(uf,color='gray',ls='--')
    a.set(xlabel=r'$x/(c_0t)$',ylabel=label,title='No-settling lock release')
    a.text(.58,.91,'Uniform shelf',transform=a.transAxes,fontsize=9)
t=np.linspace(0,6,400);v=.25
xr=-2/v*(1-np.exp(-v*t/2))
xf=2*hf*uf/v*(1-np.exp(-v*t/(2*hf)))
ax[2].plot(t,xr,label='reservoir disturbance')
ax[2].plot(t,xf,label='approximate front')
ax[2].plot(t,-t,':',color='gray',label='no settling')
ax[2].plot(t,uf*t,':',color='gray')
ax[2].set(xlabel=r'$c_0t/H$',ylabel=r'$x/H$',title=r'Settling: $V_s/c_0=0.25$')
ax[2].legend(fontsize=8)
fig.savefig('paper-75-current-profiles.png',dpi=120,facecolor='white',transparent=False)
