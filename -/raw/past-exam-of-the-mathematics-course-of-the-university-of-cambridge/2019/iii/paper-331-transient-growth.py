"""Visualize the solved triangular non-normal system; write PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
lam1,lam2=-1.,-.05
fig,axes=plt.subplots(1,2,figsize=(10,4.8),dpi=100)
ax=axes[0]
angle=np.linspace(0,2*np.pi,1000);x=np.cos(angle);y=np.sin(angle)
derivative=2*(lam1*x*x+x*y+lam2*y*y)
ax.scatter(x,y,c=np.where(derivative>0,'#b03d34','#b6bdc4'),s=8)
ax.axhline(0,color='#b6bdc4',lw=.6);ax.axvline(0,color='#b6bdc4',lw=.6)
for v,label,offset in [(np.array([lam1-lam2,1]),'$v_1$',(-.12,.06)),(np.array([0.,1.]),'$v_2$',(.10,.05))]:
    v=v/np.linalg.norm(v)
    ax.annotate('',xy=v,xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#376b95'})
    ax.text(v[0]+offset[0],v[1]+offset[1],label,color='#376b95')
ax.text(.10,-.11,r'$x_1$',color='#5e656b');ax.text(-.14,1.17,r'$x_2$',color='#5e656b')
ax.set(xlim=(-1.25,1.25),ylim=(-1.22,1.30),title='Red initial directions have rising energy')
ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
for spine in ax.spines.values():spine.set_visible(False)
ax.text(0,-1.35,'blue: nonorthogonal eigenvectors',ha='center',fontsize=10,color='#376b95')
ax=axes[1]
t=np.linspace(0,16,800);a=np.exp(lam1*t);d=np.exp(lam2*t);b=(a-d)/(lam1-lam2)
tau=a*a+b*b+d*d
G=(tau+np.sqrt(np.maximum(tau*tau-4*a*a*d*d,0)))/2
ax.plot(t,G,lw=2,color='#b03d34',label=r'optimal $G(t)$')
ax.fill_between(t,1,G,where=G>1,color='#f0b3ae',alpha=.45)
ax.plot(t,np.exp(2*lam2*t),color='#376b95',label=r'slow eigenmode $e^{2\lambda_2t}$')
ax.plot(t,np.exp(2*lam1*t),color='#818181',ls='--',label='fast eigenmode')
ax.axhline(1,color='black',lw=.8,ls=':')
ax.set(xlim=(0,16),ylim=(0,max(G)*1.12),xlabel='time',ylabel='energy / initial energy',title=r'$\lambda_1=-1,\quad\lambda_2=-0.05$')
ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=9)
fig.subplots_adjust(left=.05,right=.985,bottom=.16,top=.88,wspace=.25)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100)
plt.close(fig)
