"""Original schematic DLVO curves; parameters illustrative, not measured."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
x=np.linspace(.04,12,1800);fig,ax=plt.subplots(figsize=(7.2,4),layout='constrained')
for k,col,label in [(1,'#2166ac','Longer screening length'),(3,'#b2182b','Shorter screening length')]:
 ax.plot(x,45*np.exp(-k*x)-4/x,color=col,lw=2,label=label)
ax.axhline(0,color='grey',lw=.8);ax.set(xlim=(0,12),ylim=(-8,24),xlabel='Surface gap / chosen length',ylabel=r'$U/k_BT$',title='Illustrative attraction plus screened repulsion');ax.legend();ax.grid(alpha=.2)
ax.annotate('Contact attraction',xy=(.08,-5),xytext=(2,-6),arrowprops={'arrowstyle':'->'});ax.annotate('Outer attractive well',xy=(5,-.5),xytext=(6,6),arrowprops={'arrowstyle':'->'})
fig.savefig('paper-1-dlvo-landscape.png',dpi=170,facecolor='white');plt.close(fig)
