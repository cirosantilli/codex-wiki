"""Representative matched bound state: ka=2, kappa*a=-2*cot(2)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
z=2.;decay=-z/np.tan(z)
x=np.linspace(0,4,600)
wave=np.where(x<1,np.sin(z*x),np.sin(z)*np.exp(-decay*(x-1)))
fig,ax=plt.subplots(figsize=(6.5,3.8),layout='constrained')
ax.plot(x,wave,lw=2.5,color='#17609c')
ax.axvspan(-.15,0,color='#c8c8c8');ax.axvline(1,color='#555555',ls='--',lw=1)
ax.axhline(0,color='#555555',lw=.8)
ax.text(.05,.14,'Hard wall');ax.text(1.65,.75,'Exponential tail')
ax.annotate('Smooth matching',xy=(1,np.sin(z)),xytext=(1.65,1.02),arrowprops={'arrowstyle':'->'})
ax.set_xlim(-.15,4);ax.set_ylim(-.06,1.12)
ax.set_xticks([0,1,2,3,4],['0','a','2a','3a','4a'])
ax.set_yticks([0,1],['0','arbitrary amplitude'])
ax.set_xlabel('$x$');ax.set_ylabel(r'$\chi(x)$')
ax.set_title('Nodeless half-line bound state (representative depth)')
fig.savefig(Path('paper-1-half-line-ground-state.png'),dpi=135,facecolor='white')
