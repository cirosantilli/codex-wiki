"""Original illustrative mean-field curves; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
def positive_solution(t,h):
    if t==0:return 1.
    if h==0 and t>=1:return 0.
    lo=1e-10 if h==0 else 0.
    hi=1.
    for _ in range(70):
        mid=(lo+hi)/2
        if mid-np.tanh((mid+h)/t)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

t=np.linspace(0,2,1001)
zero=np.array([positive_solution(x,0) for x in t])
field=np.array([positive_solution(x,.01) for x in t])
fig,ax=plt.subplots(figsize=(7.5,4.5),layout='constrained',facecolor='white')
ax.plot(t,zero,color='#286f48',lw=2,label=r'$H_z=0$: positive spontaneous branch')
ax.plot(t,field,color='#b94c32',lw=2,label=r'Fixed $H_z>0$: $h=0.01$')
ax.axvline(1,color='#666666',ls=':')
ax.text(1.03,.86,r'$T_c=70\ \mathrm{K}$',fontsize=11)
ax.set(xlabel=r'Temperature $T/T_c$',ylabel=r'Magnetization $M_z/M_s(0)$',xlim=(0,2),ylim=(-.025,1.08),title='Two-direction moments: illustrative mean-field equation')
ax.legend(loc='lower left',fontsize=10)
ax.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
