import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
B=C=A=1.;My=3**.75/4
x=np.geomspace(1e-5,1e5,1000);ty=x+1/x
fig,ax=plt.subplots(figsize=(8,3.6),dpi=100)
ax.loglog(x,ty,lw=2,color='black',label=r'$t_y=D+D^{-1}$')
for ratio,color in [(10,'tab:red'),(.1,'tab:blue')]:
 M=ratio*My;tc=np.sqrt(x)/M
 ax.loglog(x,tc,lw=2,color=color,label=fr'Collision-only $t_c$: $M/M_y={ratio:g}$')
 if ratio<1:
  diff=ty-tc;idx=np.where(diff[:-1]*diff[1:]<0)[0]
  for j,label in zip(idx,[r'$D_{-,0}$',r'$D_+$']):ax.axvline(x[j],color=color,ls=':',alpha=.5);ax.text(x[j]*1.15,ty[j]*1.3,label,color=color)
ax.axvline(1,color='gray',ls='--',alpha=.5);ax.text(1.15,.03,r'$D_0$')
ax.axvline(np.sqrt(3),color='gray',ls=':',alpha=.5);ax.text(2,.065,r'$D_*$',fontsize=9)
ax.set(xlabel=r'Diameter / $\sqrt{C/B}$',ylabel='Time (scaled units)',ylim=(.01,1e6),xlim=(1e-5,1e5))
ax.legend(fontsize=9,loc='upper left');fig.tight_layout();fig.savefig('paper-316-timescales.png',facecolor='white',transparent=False)
