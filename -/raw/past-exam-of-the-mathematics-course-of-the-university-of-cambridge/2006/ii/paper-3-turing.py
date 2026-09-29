"""Original stability diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-3-turing.png to caller CWD; honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax=plt.subplots(figsize=(9,6),dpi=140,facecolor='white')
u=np.linspace(.500001,2,500);dc=2+np.sqrt(4-2/u)
ax.axhspan(0,.5,color='#f3d6bb');ax.axhspan(2,2.6,color='#f3d6bb')
ax.fill_betweenx(u,0,dc,color='#cce9d2');ax.fill_betweenx(u,dc,5,color='#d6ddf5')
ax.plot(dc,u,color='#23306c',lw=2,label='Neutral spatial mode')
for y in [.5,2]:ax.axhline(y,color='#444',ls='--',lw=1)
ax.text(.18,.23,'Positive lower branch: unstable',fontsize=10)
ax.text(.18,2.3,'Upper branch: homogeneously unstable',fontsize=10)
ax.text(.6,1.15,'All modes\ndecay',ha='center',fontsize=13)
ax.text(4.3,1.15,'Turing\ninstability',ha='center',fontsize=13)
ax.text(2.18,.65,r'$d_c=2+\sqrt{4-2/u_0}$',rotation=37,fontsize=11)
ax.set(xlim=(0,5),ylim=(0,2.6),xlabel=r'$d=\sqrt{\kappa_2/\kappa_1}$',ylabel=r'$u_0$',title='Positive homogeneous equilibria, s = 2')
ax.grid(alpha=.15);fig.tight_layout();fig.savefig('paper-3-turing.png',facecolor='white',transparent=False)
