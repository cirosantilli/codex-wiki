import numpy as np
import matplotlib.pyplot as plt
s=np.geomspace(.015,65,1800)
fig,axes=plt.subplots(2,1,figsize=(7.2,6.0),sharex=True,layout='constrained')
for Q,color in [(0.5,'#dd8a20'),(1,'#2475aa'),(3,'#8f59a4')]:
 H=1/(1+1j*Q*(s-1/s))
 axes[0].semilogx(s,np.abs(H),color=color,label=rf'$Q=R\sqrt{{C/L}}={Q:g}$')
 axes[1].semilogx(s,np.angle(H)*180/np.pi,color=color)
for ax in axes:
 ax.axvline(1,color='#777',ls=':',lw=1);ax.grid(alpha=.2)
axes[0].set(ylabel=r'$|V_2/V_1|/(R/R_1)$',ylim=(0,1.07),title=r'$V_1$ is across the series resistor $R_1$')
axes[0].legend(frameon=False);axes[0].annotate('peak = 1',xy=(1,1),xytext=(2.3,.91),arrowprops=dict(arrowstyle='->',color='#555'))
axes[1].set(xlabel=r'Angular frequency $\omega/\omega_0$,  $\omega_0=1/\sqrt{LC}$',ylabel='Phase (degrees)',ylim=(-97,97),yticks=[-90,-45,0,45,90])
axes[1].axhline(0,color='#aaa',lw=.8)
fig.savefig('paper-1-ia2012-parallel-response.png',dpi=160,facecolor='white')
