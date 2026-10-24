#!/usr/bin/env python3
"""Python 3.14, matplotlib/numpy from root pyproject.toml. Output PNG in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig,ax=plt.subplots(figsize=(7.5,5.5),facecolor='white')
x=np.linspace(-1.72,1.72,650);y=np.linspace(-1.3,1.3,600);X,Y=np.meshgrid(x,y);H=Y**2/2-X**2/2+X**4/4
ax.contour(X,Y,H,levels=[-.235,-.18,-.10,.07,.23],colors=['#377fa5'],linewidths=1.05)
tau=np.linspace(-9,9,1200);xx=np.sqrt(2)/np.cosh(tau);yy=-xx*np.tanh(tau)
for sign in [1,-1]:
 ax.plot(sign*xx,sign*yy,color='#222222',lw=2)
 for tt in [-1.3,1.3]:
  t1,t2=tt-.08,tt+.08
  r=lambda t: (sign*np.sqrt(2)/np.cosh(t),-sign*np.sqrt(2)/np.cosh(t)*np.tanh(t))
  ax.annotate('',r(t2),r(t1),arrowprops=dict(arrowstyle='->',color='#222222',lw=1.8))
t=np.linspace(-.28,.28,100);ax.plot(t,t,'--',color='#b15928',lw=1.3);ax.plot(t,-t,':',color='#6a3d9a',lw=1.6)
ax.scatter([-1,1],[0,0],s=45,color='#b52929',zorder=5);ax.scatter([0],[0],s=38,marker='x',color='black',zorder=5)
ax.text(-1,-.15,'centre',ha='center',fontsize=10);ax.text(1,-.15,'centre',ha='center',fontsize=10)
ax.annotate('outgoing: y = x',(.23,.23),(.32,1.04),arrowprops=dict(arrowstyle='-',color='#b15928'),fontsize=10,color='#9b4d22')
ax.annotate('incoming: y = -x',(.23,-.23),(.32,-1.07),arrowprops=dict(arrowstyle='-',color='#6a3d9a'),fontsize=10,color='#6a3d9a')
ax.set(xlim=(-1.72,1.72),ylim=(-1.3,1.3),xlabel='x',ylabel='y',title="x' = y,  y' = x - x³")
ax.set_aspect('equal');ax.grid(alpha=.16);ax.legend(handles=[Line2D([0],[0],color='#377fa5',label='Periodic energy curves'),Line2D([0],[0],color='#222222',lw=2,label='Homoclinic loops: H = 0')],loc='upper left',fontsize=9,framealpha=1)
fig.tight_layout();fig.savefig(Path.cwd()/'2004-double-well-phase-portrait.png',dpi=160,facecolor='white');plt.close(fig)
