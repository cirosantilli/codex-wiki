"""Original educational diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Save the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
t=np.linspace(.015,2.7,500)
fig,ax=plt.subplots(figsize=(7.4,4.4),layout='constrained')
ax.plot(t,np.sqrt(t),label=r'Radiation: $a/a_0=(t/t_0)^{1/2}$',lw=2)
ax.plot(t,t**(2/3),label=r'Matter: $a/a_0=(t/t_0)^{2/3}$',lw=2)
ax.plot(t,np.exp(t-1),label=r'Vacuum: $a/a_0=e^{H(t-t_0)}$, $Ht_0=1$',lw=2)
ax.scatter([1],[1],s=22,color='black',zorder=5)
ax.set(xlabel=r'Cosmic time $t/t_0$',ylabel=r'Scale factor $a/a_0$',xlim=(0,2.7),ylim=(0,5.6),title='Flat expanding models, normalized at a common event')
ax.legend(loc='upper left',fontsize=9);ax.grid(alpha=.2)
fig.savefig('paper-1-flrw-expansion.png',dpi=160)
