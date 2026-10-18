"""Original cloud-growth trajectories; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
t=np.linspace(0,2000,1001);D=2.5e-13;kr=1.2e8;U=1.;alpha=.0016;kR=8000.;R0=20e-6
hr=U*t-kr*D*t*t
hR=U*t-kR*R0/alpha*np.expm1(alpha*t)
lo,hi=1800.,2000.
for _ in range(60):
 mid=(lo+hi)/2
 if U*mid-kR*R0/alpha*np.expm1(alpha*mid)>0:lo=mid
 else:hi=mid
exit_time=(lo+hi)/2
turn=np.log(U/(kR*R0))/alpha
hmax=U*turn-kR*R0/alpha*np.expm1(alpha*turn)
fig,(a,b)=plt.subplots(1,2,figsize=(11.7,4.9),layout='constrained')
a.plot(t,t,label='No settling',lw=2);a.plot(t,hr,label='Condensation + settling',lw=2)
a.axhline(2000,color='0.5',ls='--',label='Cloud top')
a.plot([2000,2000],[1880,2000],color='black',lw=2)
a.annotate('120 m lag',(2000,1940),(1350,1520),arrowprops={'arrowstyle':'->'})
a.set(xlabel='Time (s)',ylabel='Height above cloud base (m)',title='Small droplets: condensation alone',xlim=(0,2050),ylim=(0,2200));a.legend(loc='upper left',fontsize=9)
inside=t<=exit_time
b.plot(t[inside],hR[inside],lw=2,color='#c96d24',label='Collector within cloud')
b.plot(t[~inside],hR[~inside],'--',lw=2,color='#c96d24',label='Formal extrapolation')
b.axhline(0,color='black',lw=1);b.fill_between([0,2050],0,950,color='#4477aa',alpha=.06)
b.plot(turn,hmax,'ko');b.annotate(f'Turns at {turn:.0f} s\nheight {hmax:.0f} m',(turn,hmax),(1050,830),arrowprops={'arrowstyle':'->'},ha='center')
b.plot(exit_time,0,'ko');b.annotate(f'Cloud-base exit\n{exit_time:.0f} s',(exit_time,0),(1200,-200),arrowprops={'arrowstyle':'->'},ha='center')
b.set(xlabel='Time (s)',ylabel='Height above cloud base (m)',title='Collector: exponential growth and rain-out',xlim=(0,2050),ylim=(-450,1000));b.legend(loc='upper left',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
