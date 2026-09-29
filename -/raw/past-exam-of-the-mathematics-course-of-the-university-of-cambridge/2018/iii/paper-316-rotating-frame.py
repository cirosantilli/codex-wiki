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

fig,ax=plt.subplots(figsize=(7.5,4.7),dpi=100)
e=.13;omega=.58;f=.72;lam=omega+f;lamG=.99;ag=.97
rot=lambda xy:np.array([[np.cos(omega),-np.sin(omega)],[np.sin(omega),np.cos(omega)]])@xy
E=np.linspace(0,2*np.pi,700);curve=rot(np.array([np.cos(E)-e,np.sqrt(1-e*e)*np.sin(E)]))
ax.plot(*curve,color=blue,alpha=.6)
r=(1-e*e)/(1+e*np.cos(f));P=r*np.array([np.cos(lam),np.sin(lam)]);G=ag*np.array([np.cos(lamG),np.sin(lamG)])
u=np.array([np.cos(lamG),np.sin(lamG)]);v=np.array([-u[1],u[0]])
ax.plot([0,P[0]],[0,P[1]],color=blue);ax.plot([0,G[0]],[0,G[1]],'--',color=gray)
peri=(1-e)*np.array([np.cos(omega),np.sin(omega)]);ax.plot([0,peri[0]],[0,peri[1]],color=green)
ax.plot(0,0,'*',ms=13,color='#bb921d');ax.plot(*G,'o',color=gray);ax.plot(*P,'o',color=blue)
ax.annotate('',G+.48*u,G,arrowprops={'arrowstyle':'->','color':gray});ax.text(*(G+.53*u),'x',color=gray,fontsize=12)
ax.annotate('',G+.48*v,G,arrowprops={'arrowstyle':'->','color':gray});ax.text(*(G+.53*v),'y',color=gray,fontsize=12)
for rad,start,end,col,label in [(.23,0,omega,green,r'$\varpi$'),(.40,omega,lam,blue,'f'),(.58,lamG,lam,orange,r'$\delta\lambda$')]:
    ax.add_patch(Arc((0,0),2*rad,2*rad,theta1=np.degrees(start),theta2=np.degrees(end),color=col,lw=1.5))
    mid=(start+end)/2;ax.text((rad+.04)*np.cos(mid),(rad+.04)*np.sin(mid),label,color=col,fontsize=11)
ax.text(G[0]+.08,G[1]-.05,'G');ax.text(P[0]-.18,P[1]+.04,'Particle');ax.text(peri[0]+.03,peri[1]-.03,'Pericentre',color=green)
ax.plot([0,1.3],[0,0],':',color=gray);ax.text(.68,-.15,'Initial common longitude')
ax.text(-1.17,-.85,r'$M=nt+M_0$ advances uniformly',fontsize=10)
ax.text(-1.17,-1.02,r'$\lambda=\varpi+f,\quad \lambda_G=n_g t$',fontsize=10)
ax.set_aspect('equal');ax.set(xlim=(-1.35,1.35),ylim=(-1.15,1.43));ax.axis('off')
ax.set_title('Rotating radial and along-track axes at a later instant');fig.tight_layout();finish(fig)
