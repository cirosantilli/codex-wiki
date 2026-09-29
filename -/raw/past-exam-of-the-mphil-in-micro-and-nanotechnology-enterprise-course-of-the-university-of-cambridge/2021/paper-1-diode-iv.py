"""Ideal diode curve, deliberately scaled to show reverse saturation."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
v=np.linspace(-5,3.5,1000);i=np.expm1(v)
fig,ax=plt.subplots(figsize=(7,4.5),layout='constrained')
ax.plot(v,i,color='#245c9f',lw=2);ax.axhline(0,color='.35',lw=.8);ax.axvline(0,color='.35',lw=.8)
ax.axhline(-1,color='.55',ls='--',lw=1);ax.annotate(r'Reverse saturation: $-I_0$',(-3.1,-1),(-4.85,4),fontsize=10,arrowprops={'arrowstyle':'->'})
ax.annotate('LED on: quadrant I\nelectrical power absorbed',(3.1,np.expm1(3.1)),(.2,27),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlabel=r'$V/(nV_T)$',ylabel=r'$I/I_0$',ylim=(-2,35),title='Ideal p–n junction (reverse breakdown omitted)');ax.grid(alpha=.16)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white');plt.close(fig)
