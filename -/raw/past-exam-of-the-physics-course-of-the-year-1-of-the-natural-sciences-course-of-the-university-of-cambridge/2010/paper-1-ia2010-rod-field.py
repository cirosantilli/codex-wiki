"""Ampere-law magnetic field, originally plotted from analytic solution."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7,4.4),facecolor='white',layout='constrained')
x=np.linspace(0,1,251);xx=np.linspace(1,5,501)
ax.plot(x,x,lw=2,color='#235c87',label=r'Inside: $B/B(a)=r/a$')
ax.plot(xx,1/xx,lw=2,color='#b5671a',label=r'Outside: $B/B(a)=a/r$')
ax.axvline(1,color='.5',lw=1,ls='--');ax.scatter([1],[1],color='#333333',s=30)
ax.set(xlim=(0,5),ylim=(0,1.15),xlabel=r'$r/a$',ylabel=r'$B(r)/B(a)$',title='Uniform-current nonmagnetic rod; end effects neglected')
ax.legend();ax.grid(alpha=.15)
fig.savefig('paper-1-ia2010-rod-field.png',dpi=165,facecolor='white');plt.close(fig)
