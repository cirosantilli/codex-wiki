#!/usr/bin/env python3
"""Original planetary-dynamics figure; outputs its same-basename PNG to CWD.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Dependencies match the repository pyproject; no external visual assets.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
blue='#22577a'; orange='#c66a24'; green='#387c58'; gray='#666666'
def finish(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(10.8,4.7),dpi=100)
ax=axes[0];f=np.linspace(-np.pi,np.pi,1800)
for beta,color in [(0,gray),(.1,green),(.3,blue),(.45,orange)]:
    e=beta/(1-beta);p=1/(1-beta);r=p/(1+e*np.cos(f))
    ax.plot(r*np.cos(f),r*np.sin(f),color=color,label=fr'$\beta={beta:g}$')
f=np.linspace(-2.45,2.45,1000);r=2/(1+np.cos(f))
ax.plot(r*np.cos(f),r*np.sin(f),'--',color='#8c568b',label=r'$\beta=1/2$: parabolic')
ax.plot(0,0,'*',ms=12,color='#bb921d');ax.plot(1,0,'o',ms=5,color='black')
ax.annotate('Release point',(1,0),(-.2,-4.3),arrowprops={'arrowstyle':'->','color':gray})
ax.set(xlim=(-10.8,2.1),ylim=(-5.6,5.6),xlabel=r'$x/r_b$',ylabel=r'$y/r_b$',title='One longitude of the dust birth ring');ax.set_aspect('equal')
ax.legend(loc='upper left',fontsize=8)
# u = e/sqrt(1-e^2) removes the upper-end singularity of the lifetime integral.
nodes,weights=np.polynomial.legendre.leggauss(300)
beta=np.linspace(.002,.4993,600);e0=beta/(1-beta);upper=e0/np.sqrt(1-e0*e0)
u=upper[:,None]*(nodes[None,:]+1)/2
J=upper/2*((u/np.sqrt(1+u*u))**.6 @ weights)
t=(2/5)*beta**(-2.6)*(1-beta)**(-.4)*J
ax=axes[1];ax.semilogy(beta,t,color=blue,lw=2)
i=np.argmin(t);ax.plot(beta[i],t[i],'o',color=orange)
ax.annotate(fr'Minimum near $\beta={beta[i]:.2f}$',(beta[i],t[i]),(.12,8),arrowprops={'arrowstyle':'->','color':orange})
ax.axvline(.5,color=gray,ls='--');ax.axvspan(.5,.65,color='#e8e8e8')
ax.text(.575,15,'Initially\nunbound\n\nEscape time\nneeds a radius',ha='center',fontsize=9)
ax.set(xlim=(0,.65),ylim=(1,160),xlabel=r'$\beta$',ylabel=r'$t_{\rm PR}/[c r_b^2/(G M_\star)]$',title='Formal bound-orbit inspiral time')
ax.grid(alpha=.15);fig.tight_layout();finish(fig)
