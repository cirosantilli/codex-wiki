"""Original generic-physics figure; Python 3.14, numpy and matplotlib.
PNG basename output to cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(8.5,3.5),layout='constrained');x=np.linspace(0,1,300)
for amp,lab in [(0,'straight'),(.1,'first trial mode'),(-.16,'opposite trial amplitude')]:a.plot(x,amp*np.sin(np.pi*x),label=lab)
a.set(xlabel='s/L',ylabel='y/L (chosen amplitude)',title='Pinned-filament trial deformations',ylim=(-.25,.25));a.legend(frameon=False,fontsize=8)
q=np.linspace(0,2,400)
for sig,lab in [(1,'tension'),(0,'zero tension'),(-1,'compression')]:b.plot(q,q**4+sig*q*q,label=lab)
b.axhline(0,color='gray',ls=':');b.set(xlabel='Scaled wave number',ylabel='Scaled modal stiffness',title='Generic film: bending + in-plane stress',ylim=(-.5,5));b.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-buckling.png',dpi=150);plt.close(fig)
