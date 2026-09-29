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

fig,axes=plt.subplots(1,3,figsize=(11.4,4.4),dpi=100)
theta=np.linspace(0,2*np.pi,600)
ax=axes[0];zf=.14;ep=.075;ang=1.05;z=zf+ep*np.exp(1j*ang)
ax.plot(zf+ep*np.cos(theta),ep*np.sin(theta),color=blue)
ax.annotate('',(zf,0),(0,0),arrowprops={'arrowstyle':'->','color':green,'lw':2})
ax.annotate('',(z.real,z.imag),(zf,0),arrowprops={'arrowstyle':'->','color':orange,'lw':2})
ax.plot(z.real,z.imag,'o',color=blue);ax.text(.055,-.018,r'$z_f$',color=green);ax.text(.18,.025,r'$z_p$',color=orange)
ax.text(z.real+.005,z.imag,r'$z$');ax.set(xlim=(-.035,.25),ylim=(-.11,.11),xlabel='Re z',ylabel='Im z',title='Proper + forced eccentricity');ax.axhline(0,color=gray,lw=.5);ax.axvline(0,color=gray,lw=.5);ax.set_aspect('equal')
ax=axes[1];ef=.12;ep=.065
outer=np.c_[np.cos(theta)*(1+ep)-ef,np.sin(theta)*(1+ep)]
inner=np.c_[np.cos(theta)*(1-ep)-ef,np.sin(theta)*(1-ep)]
ax.fill(np.r_[outer[:,0],inner[::-1,0]],np.r_[outer[:,1],inner[::-1,1]],color='#d4e2ec')
for phi in np.linspace(0,2*np.pi,12,endpoint=False):
    center=np.array([-ef-ep*np.cos(phi),-ep*np.sin(phi)])
    ax.plot(np.cos(theta)+center[0],np.sin(theta)+center[1],color=blue,alpha=.27,lw=.8)
ax.plot(-ef,0,'+',color=green,ms=8);ax.plot(0,0,'*',color='#bb921d',ms=11)
ax.set(title='Common a; random proper phases');ax.text(-.17,-1.25,'Constant width 2 a e_p',ha='center',fontsize=9)
ax=axes[2]
for a in np.linspace(.92,1.08,9):ax.plot(a*(np.cos(theta)-ef),a*np.sin(theta),color=orange,alpha=.65,lw=1)
ax.plot(0,0,'*',color='#bb921d',ms=11);ax.set(title='Range of a; constant forced e')
ax.text(-.17,-1.25,'Wider at apocentre (left)',ha='center',fontsize=9)
for ax in axes[1:]:
    ax.set_aspect('equal');ax.set(xlim=(-1.48,1.3),ylim=(-1.37,1.3),xlabel='x / a',ylabel='y / a')
fig.suptitle('First-order secular geometry; forced pericentre points right',fontsize=11)
fig.tight_layout(rect=(0,0,1,.94));finish(fig)
