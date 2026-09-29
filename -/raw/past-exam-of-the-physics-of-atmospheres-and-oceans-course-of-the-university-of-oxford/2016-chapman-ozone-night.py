"""Original explanatory figure. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

kb=1.380649e-23;temperature=230.;j2=1e-9;j3=.003;k1=1e-45;b=9.9e-22
p_hpa=np.geomspace(.001,1,600)
n=p_hpa*100/(kb*temperature);n2=.2*n
a=k1*n2*n
x=(j2+np.sqrt(j2*j2+4*k1*n*j2*j3/b))/(2*k1*n)
y=j2*n2/(b*x)
n0=1/(kb*temperature);a0=k1*.2*n0*n0
x0=(j2+np.sqrt(j2*j2+4*k1*n0*j2*j3/b))/(2*k1*n0);y0=j2*.2*n0/(b*x0)
def night(duration_h=16.,dt=5.):
    steps=round(duration_h*3600/dt)
    t=np.arange(steps+1)*dt
    vals=np.empty((steps+1,2));vals[0]=[x0,y0]
    def rhs(z):
        xx,yy=z
        return np.array([-xx*(a0+b*yy),xx*(a0-b*yy)])
    for i in range(steps):
        z=vals[i];v1=rhs(z);v2=rhs(z+dt*v1/2);v3=rhs(z+dt*v2/2);v4=rhs(z+dt*v3)
        vals[i+1]=z+dt*(v1+2*v2+2*v3+v4)/6
    return t/3600,vals/n0*1e6
hours,vmr=night()
fig,axs=plt.subplots(1,2,figsize=(10,4.6),layout='constrained')
axs[0].loglog(x/n*1e6,p_hpa,color='#126782',lw=2.3,label='Atomic oxygen')
axs[0].loglog(y/n*1e6,p_hpa,color='#a44418',lw=2.3,label='Ozone')
axs[0].axhline(.01,color='#666666',lw=1,ls='--')
axs[0].invert_yaxis();axs[0].set(xlabel='Daytime mixing ratio (ppm)',ylabel='Pressure (hPa)',title='Exact daytime equilibrium')
axs[0].legend(fontsize=10);axs[0].grid(alpha=.22,which='both')
axs[1].plot(hours,vmr[:,0],color='#126782',lw=2.3,label='Atomic oxygen')
axs[1].plot(hours,vmr[:,1],color='#a44418',lw=2.3,label='Ozone')
axs[1].axhline(a0/b/n0*1e6,color='#555555',ls='--',lw=1.4,label=r'Night balance $a/(b n_M)$')
axs[1].set(xlabel='Duration after sunset (hours)',ylabel='Mixing ratio (ppm)',title='Night at 0.01 hPa; duration is a free input',xlim=(0,16),ylim=(0,330))
axs[1].legend(fontsize=10);axs[1].grid(alpha=.22)
fig.suptitle('Chapman oxygen chemistry with the supplied fixed-temperature rates',fontsize=15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
