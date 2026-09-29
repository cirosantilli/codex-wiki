"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

y=np.linspace(-3.5,3.5,1000);U=.9*np.maximum(abs(y)-1.9,0)**2
fig,ax=plt.subplots(figsize=(7.5,4),layout='constrained')
for E,label,c in [(1/3,r'$0,-$','#2166ac'),(2/3,r'$0,+$','#b2182b'),(4/3,r'$1,-$','#4393c3'),(5/3,r'$1,+$','#ef8a62'),(7/3,r'$2,-$','#777777')]:ax.plot(y,E+U,label=label,color=c,lw=2,ls='--' if E>2 else '-')
ax.axhline(2,color='black',ls=':',label=r'$E_F$ (chosen)');ax.set(xlabel='Transverse coordinate (chosen units)',ylabel=r'$E/(\hbar\omega_c)$',ylim=(0,3.6),xlim=(-3.5,3.5),title=r'Smooth-edge spectrum; $E_Z=\hbar\omega_c/3$');ax.legend(ncol=3,loc='upper center',fontsize=8);ax.text(-.8,.08,'Bulk');ax.grid(alpha=.15)
fig.savefig('paper-1-edge-spectrum.png',dpi=170,facecolor='white');plt.close(fig)
