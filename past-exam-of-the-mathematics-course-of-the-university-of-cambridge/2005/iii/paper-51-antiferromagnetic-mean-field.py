"""Original mean-field bifurcation. Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7; honors caller MPLCONFIGDIR and writes PNG basename to CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def positive_root(K):
    if K<=1:return 0.
    lo,hi=1.e-12,1.
    for _ in range(65):
        m=(lo+hi)/2
        if np.tanh(K*m)>m:lo=m
        else:hi=m
    return (lo+hi)/2

fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained',facecolor='white')
x=np.linspace(-1.05,1.05,500)
axs[0].plot(x,x,color='black',ls='--',label='Diagonal M')
for K,color in [(.7,'#286c9c'),(1,'#777777'),(1.5,'#b22222')]:
    axs[0].plot(x,np.tanh(K*x),color=color,label=f'tanh(KM), K={K}')
    m=positive_root(K)
    axs[0].scatter([-m,0,m],[-m,0,m],color=color,s=23,zorder=5)
axs[0].set(xlabel='M',ylabel='M and tanh(KM)',title='Intersections at zero uniform/staggered fields')
axs[0].legend(fontsize=8);axs[0].grid(alpha=.2)
t=np.linspace(.12,1.65,350);m=np.array([positive_root(1/v) for v in t])
axs[1].plot(t,m,color='#b22222',label='Stable staggered order ±M')
axs[1].plot(t,-m,color='#b22222')
axs[1].plot([.12,1],[0,0],ls='--',color='#777777',label='Unstable M=0 below Tc')
axs[1].axvline(1,color='black',ls=':',label='Tc=qJ/kB')
axs[1].set(xlabel='Temperature T/Tc',ylabel='Staggered magnetization M−',title='Continuous mean-field ordering')
axs[1].legend(fontsize=8);axs[1].grid(alpha=.2)
fig.savefig('paper-51-antiferromagnetic-mean-field.png',dpi=100,facecolor='white',transparent=False)
