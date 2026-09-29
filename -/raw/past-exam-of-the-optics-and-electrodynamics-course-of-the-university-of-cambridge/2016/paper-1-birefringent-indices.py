#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from the corresponding mirrored _media directory; writes a PNG basename to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

theta=np.linspace(0,np.pi/2,301);no=1.5;ne=1.7;nex=1/np.sqrt(np.cos(theta)**2/no**2+np.sin(theta)**2/ne**2)
fig,ax=plt.subplots(figsize=(6.5,3.8));ax.plot(np.rad2deg(theta),theta*0+no,label='Ordinary n = 1.5');ax.plot(np.rad2deg(theta),nex,label='Extraordinary phase index')
ax.set(xlabel='Wave-vector angle to optic axis (degrees)',ylabel='Phase refractive index',xlim=(0,90),ylim=(1.47,1.73),title='Illustrative positive uniaxial dielectric');ax.grid(alpha=.2);ax.legend(loc='upper left');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
