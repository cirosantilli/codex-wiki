"""Reaction-rate sketch; Python 3.14, NumPy and Matplotlib from root pyproject."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
k=3.0
g=np.linspace(0,3.9,800)
f=k*g*g/(1+g*g)-g
roots=sorted(v.real for v in np.roots([1,0,2,-2*k,1]) if abs(v.imag)<1e-8 and v.real>0)
gc=roots[0];sc=gc*(1-gc*gc)/2
g1=(k-np.sqrt(k*k-4))/2;g2=(k+np.sqrt(k*k-4))/2
fig,ax=plt.subplots(figsize=(8.5,4.3),dpi=120)
fig.patch.set_facecolor('white');ax.set_facecolor('white')
ax.axhline(0,color='black',lw=.9)
ax.plot(g,f,label=r'$s=0$',color='#1565c0',lw=2)
ax.plot(g,f+sc+.12,label=r'$s>s_c$',color='#ef6c00',lw=1.6)
for z,name,stable in [(0,'0',True),(g1,r'$g_1$',False),(g2,r'$g_2$',True)]:
 ax.plot(z,0,'o',ms=7,mfc='#1565c0' if stable else 'white',mec='#1565c0',clip_on=False)
 ax.annotate(name,(z,0),xytext=(4,-20),textcoords='offset points')
for lo,hi in [(g1*.8,g1*.25),((g1+g2)/2,(g1+g2)/2+.35),(3.65,3.3)]:
 ax.annotate('',xy=(hi,-.045),xytext=(lo,-.045),arrowprops={'arrowstyle':'->','color':'#1565c0'})
ax.set(xlim=(-.05,3.9),ylim=(-1.3,.95),xlabel='Concentration g',ylabel='Reaction rate f(g,s)',title='Saturating autocatalytic switch (k = 3)')
ax.legend(frameon=False);ax.grid(alpha=.15);fig.tight_layout()
fig.savefig(Path.cwd()/'paper-1-gene-switch.png',facecolor='white',transparent=False)
plt.close(fig)
