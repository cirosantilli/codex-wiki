"""Positive-flux phase portrait; Python 3.14, root numpy/matplotlib; cwd PNG only."""
from pathlib import Path
import os
if not os.environ.get('MPLCONFIGDIR'):raise RuntimeError('Supply an owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(.045,2,200);y=np.linspace(.08,4.3,220);C,H=np.meshgrid(x,y)
f=6/H**2-4/(H*C);h=(6/(H*C)-12/H**2)/H
speed=np.hypot(f,h);f/=speed;h/=speed
fig,ax=plt.subplots(figsize=(7.8,5.2),dpi=100,facecolor='white');ax.set_facecolor('white')
ax.streamplot(x,y,f,h,density=1.0,color='#788792',linewidth=.7,arrowsize=.9)
ax.plot(x,1.5*x,lw=2,color='#a94b34',label=r'$\Gamma_X=0:\ H=3\Gamma/2$')
ax.plot(x,2*x,lw=2,color='#286890',label=r'$H_X=0:\ H=2\Gamma$')
ax.text(.16,3.65,r'$\Gamma_X<0,\ H_X>0$',color='#286890',fontsize=11)
ax.text(1.04,2.04,r'$\Gamma_X<0,\ H_X<0$',fontsize=10,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
ax.text(1.07,.62,r'$\Gamma_X>0,\ H_X<0$',color='#a94b34',fontsize=11)
ax.set_xlim(0,2);ax.set_ylim(0,4.3);ax.set_xlabel(r'Surfactant concentration $\Gamma$');ax.set_ylabel(r'Film height $H$')
ax.set_title('Steady surfactant-film trajectories: Q = J = 1',fontsize=13,pad=12)
ax.legend(loc='upper right',fontsize=9,framealpha=1);ax.grid(alpha=.15)
fig.subplots_adjust(left=.11,right=.97,top=.88,bottom=.16)
fig.text(.5,.035,'Axes are singular boundaries. Arrow normalization changes speed, not trajectories.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False);plt.close(fig)
