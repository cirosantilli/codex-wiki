"""Python3.14, numpy2.3, matplotlib3.10; write matching PNG to output CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
phi=np.linspace(0,2*np.pi,800)
x=np.cos(phi)+np.sin(phi)/np.sqrt(3)
y=np.cos(phi)-np.sin(phi)/np.sqrt(3)
r=.4;den=r*r+r+1
p=(1,0);q=(0,r);a=((r*r-1)/den,r*(r+2)/den)
fig,ax=plt.subplots(figsize=(6.2,4.4),layout='constrained',facecolor='white')
ax.plot(x,y,color='#222222',lw=2,label='Conic')
ax.axvline(0,color='#2465a4',lw=1.6,ls='--',label='L: x = 0')
xx=np.linspace(-1.5,1.45,200);ax.plot(xx,r*(1-xx),color='#b74726',lw=1.5,label='Line through p and q')
for (xx,yy),lab,off in [(p,'p',(6,-16)),(q,'q',(7,5)),(a,r'$\alpha(q)$',(-43,8))]:
 ax.plot(xx,yy,'o',color='#b74726',ms=6);ax.annotate(lab,(xx,yy),xytext=off,textcoords='offset points',fontsize=12)
ax.set(xlim=(-1.5,1.5),ylim=(-1.35,1.35),xlabel='x',ylabel='y',title='A conic parametrized by lines through one point')
ax.set_aspect('equal');ax.set_facecolor('white');ax.spines[['top','right']].set_visible(False);ax.legend(loc='lower right',fontsize=8,framealpha=1)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
