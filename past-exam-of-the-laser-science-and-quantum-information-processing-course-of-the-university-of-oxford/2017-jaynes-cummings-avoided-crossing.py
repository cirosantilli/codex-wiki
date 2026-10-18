"""Original specified-bare-level diagram and its complete central doublet."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
x=np.linspace(0,2,801);n=3;ratio=.08
fig,ax=plt.subplots(figsize=(9.5,5.7),layout='constrained',facecolor='white')
for y,lab,col in [((x-1)/2,r'$|e,n-1\rangle$','#708090'),((1-x)/2,r'$|g,n\rangle$','#a0a0a0'),(-(1+x)/2,r'$|g,n-1\rangle$','#668b67'),((1+x)/2,r'$|e,n\rangle$','#ab8680')]:ax.plot(x,y,ls='--',lw=1.6,label=lab,color=col)
dress=.5*np.sqrt((1-x)**2+4*ratio**2*n)
ax.plot(x,dress,lw=2.6,color='#126782',label=r'$E_{+,n-1}$')
ax.plot(x,-dress,lw=2.6,color='#a34a32',label=r'$E_{-,n-1}$')
ax.axvline(1,ls=':',lw=1,color='gray');ax.annotate('',xy=(1,ratio*np.sqrt(n)),xytext=(1,-ratio*np.sqrt(n)),arrowprops={'arrowstyle':'<->','lw':1.3});ax.text(1.04,0,r'$2g\sqrt{n}/\omega$',va='center',fontsize=11)
ax.set(xlim=(0,2),ylim=(-1.65,1.65),xticks=[0,1,2],xlabel=r'Atomic frequency $\omega_0/\omega$',ylabel=r'$[E-\hbar\omega(n-1/2)]/(\hbar\omega)$',title='Bare-level crossing becomes a dressed-state avoided crossing\nIllustrative n = 3 and g/ω = 0.08')
ax.grid(alpha=.18);ax.legend(loc='upper center',ncol=3,fontsize=10,framealpha=.96)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
