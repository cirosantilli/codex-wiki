"""Original one-radius virial-cloud curve. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
f=lambda x:4/x**3-3/x**4
fig,ax=plt.subplots(figsize=(7.1,4.2),layout='constrained',facecolor='white')
for lo,hi,color,label in [(.6,.75,'.5','Negative external pressure'),(.75,1,'#bd542c','Unstable equilibrium'),(1,4,'#196b9a','Stable radial equilibrium')]:
 x=np.linspace(lo,hi,300);ax.plot(x,f(x),lw=2.4,color=color,label=label)
ax.axhline(0,color='.4',lw=.8);ax.axhline(1,color='.6',ls='--',lw=.8);ax.axvline(1,color='.6',ls=':',lw=1)
ax.scatter([.75,1],[0,1],color='black',s=20,zorder=5)
ax.annotate('Maximum pressure; marginal radius',xy=(1,1),xytext=(1.55,.93),arrowprops=dict(arrowstyle='->'),fontsize=9)
ax.text(.76,-.18,r'$r_z=3r_c/4$',fontsize=10);ax.legend(loc='upper right',bbox_to_anchor=(1,.82),fontsize=9)
ax.set(xlim=(.6,4),ylim=(-.45,1.15),xlabel=r'Cloud radius $r/r_c$',ylabel=r'Required external pressure $p/p_{\max}$',title=r'Virial cloud model: $p/p_{\max}=4(r_c/r)^3-3(r_c/r)^4$')
ax.grid(alpha=.16);fig.savefig('paper-1-virial-pressure.png',dpi=150,facecolor='white')
