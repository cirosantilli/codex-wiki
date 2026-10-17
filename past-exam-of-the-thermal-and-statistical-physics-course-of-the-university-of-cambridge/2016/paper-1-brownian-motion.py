#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Run from mirrored _media directory; PNG basename goes to cwd.
All plotted parameter choices are illustrative and do not assert provided exam data.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

rng=np.random.default_rng(2016);path=np.vstack([np.zeros((1,2)),np.cumsum(rng.normal(size=(1500,2)),axis=0)])
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.7,3.8));ax.plot(path[:,0],path[:,1],color='#12669b',lw=.7);ax.plot(0,0,'o',color='#af701c',label='Start');ax.set(xlabel='x (arbitrary units)',ylabel='y (arbitrary units)',title='Illustrative diffusion trajectory');ax.set_aspect('equal',adjustable='datalim');ax.legend(fontsize=8)
t=np.geomspace(1e-3,1e2,700);msd=t+np.expm1(-t);bx.loglog(t,msd,lw=2,label='Equilibrium inertial model');bx.loglog(t,t*t/2,'--',color='#af701c',label='Ballistic: t^2 / 2');bx.loglog(t,t,':',color='.4',label='Diffusive: t');bx.set(xlabel='Time / relaxation time',ylabel='1D mean-square displacement / (2 D tau)',ylim=(1e-7,3e2),title='Thermal initial velocities');bx.legend(fontsize=8);bx.grid(alpha=.2);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
