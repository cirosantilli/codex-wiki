"""Original parabolic 2D gas occupations. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(9,4),layout='constrained',facecolor='white')
z=np.linspace(-1.25,1.25,31);xx,yy=np.meshgrid(z,z);inside=xx*xx+yy*yy<=1
ax[0].scatter(xx[~inside],yy[~inside],s=9,color='.82');ax[0].scatter(xx[inside],yy[inside],s=12,color='#176c9d');p=np.linspace(0,2*np.pi,400);ax[0].plot(np.cos(p),np.sin(p),color='black',lw=1)
ax[0].set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),aspect='equal',xlabel=r'$k_x/k_F$',ylabel=r'$k_y/k_F$',title='Filled disk; two spin states per k')
e=np.linspace(0,2,600);ax[1].step([0,1,2],[1,0,0],where='post',color='black',label='T = 0')
for t in [.08,.2]:
 mu=1+t*np.log1p(-np.exp(-1/t));prob=1/(np.exp((e-mu)/t)+1);ax[1].plot(e,prob,label=fr'$k_BT/\epsilon_F={t}$')
ax[1].set(xlim=(0,2),ylim=(-.04,1.04),xlabel=r'Energy / $\epsilon_F$',ylabel='Occupation probability per spin state',title='Fixed number, constant density of states');ax[1].legend(fontsize=8);ax[1].grid(alpha=.18)
fig.savefig('paper-2-two-dimensional-fermi-gas.png',dpi=150,facecolor='white')
