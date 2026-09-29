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

# Integral representation Li_3(exp(lz)) = (1/2) integral x^2/(exp(x-lz)-1) dx.
# Fixed Gauss-Legendre quadrature and bisection need only NumPy, not SciPy/mpmath.
x,w=np.polynomial.legendre.leggauss(256);xx=25*(x+1);ww=25*w
li=lambda lz:float(.5*np.sum(ww*xx**2/np.expm1(xx-lz)))
zeta3=li(0);t=np.r_[np.linspace(0,1,160),np.linspace(1.002,2.5,180)];mu=np.zeros_like(t)
for j,tr in enumerate(t):
 if tr<=1:continue
 target=zeta3/tr**3;lo=-30.;hi=0.
 for _ in range(48):
  mid=(lo+hi)/2
  if li(mid)>target:hi=mid
  else:lo=mid
 mu[j]=tr*(lo+hi)/2
frac=np.maximum(0,1-t**3);fig,(ax,bx)=plt.subplots(1,2,figsize=(8.8,3.8));ax.plot(t,mu,color='#12669b',lw=2);ax.axhline(0,color='.5',lw=.7);ax.axvline(1,color='#af701c',ls='--');ax.set(xlabel='T / T0',ylabel='Chemical potential / (kB T0)',xlim=(0,2.5),title='Ideal harmonic trap, ground energy = 0');ax.grid(alpha=.2)
bx.plot(t,frac,color='#12669b',lw=2);bx.axvline(1,color='#af701c',ls='--');bx.set(xlabel='T / T0',ylabel='Macroscopic ground-state fraction N0 / N',xlim=(0,2.5),ylim=(-.03,1.03),title='Leading large-N condensate fraction');bx.grid(alpha=.2);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
