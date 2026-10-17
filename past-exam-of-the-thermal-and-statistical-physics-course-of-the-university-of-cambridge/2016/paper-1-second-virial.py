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

r=np.geomspace(.012,90,36000);u=4*(r**-12-r**-6)
def virial(t):return float(2*np.pi*np.trapezoid(-np.expm1(-u/t)*r*r,r)+2*np.pi*.012**3/3-8*np.pi/(3*t*90**3))
temp=np.geomspace(.62,2000,240);b2=np.array([virial(t) for t in temp]);lo=2.;hi=5.
for _ in range(50):
 mid=(lo+hi)/2
 if virial(mid)>0:hi=mid
 else:lo=mid
boyle=(lo+hi)/2
fig,ax=plt.subplots(figsize=(7,4));ax.plot(temp,b2,color='#12669b',lw=2);ax.axhline(0,color='.4',lw=1);ax.axvline(boyle,color='#af701c',ls='--');ax.text(boyle*1.12,-3,'Boyle zero\nT* ~ %.3f'%boyle,color='#9c6115');ax.set(xscale='log',xlabel='Reduced temperature T* = kBT / epsilon',ylabel='B2 / sigma^3',ylim=(-8,1.6),xlim=(.62,2000),title='Classical Lennard-Jones pair-potential example');ax.grid(alpha=.2);ax.text(25,-5.5,'Positive repulsive contribution\neventually falls toward zero',fontsize=10);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
