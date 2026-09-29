import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,1.4,600)
fig,ax=plt.subplots(figsize=(6.5,4),layout='constrained')
ax.plot(t,np.maximum(1-t**1.5,0),color='#2475aa',lw=2.4,label=r'Condensate $N_0/N$')
ax.plot(t,np.minimum(t**1.5,1),color='#c94a39',lw=2.4,label=r'Actual thermal fraction $N_{\rm ex}/N$')
ax.plot(t,t**1.5,color='#c94a39',ls=':',label='Excited-state capacity at zero chemical potential')
ax.axvline(1,color='#888',ls=':');ax.set(xlim=(0,1.4),ylim=(0,1.7),xlabel=r'$T/T_c$',ylabel='Particle fraction / capacity',title='Homogeneous 3D ideal gas; conserved particle number')
ax.legend(frameon=False,fontsize=9);ax.grid(alpha=.2)
fig.savefig('paper-1-tsp2012-condensation.png',dpi=150,facecolor='white')
