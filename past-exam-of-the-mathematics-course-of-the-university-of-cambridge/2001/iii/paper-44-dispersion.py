"""Thermocapillary film dispersion. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory; emits only the PNG basename there.
Uses the caller's MPLCONFIGDIR unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

k=np.linspace(0,1.3,601);s=k*k-k**4
fig,ax=plt.subplots(figsize=(7,4.4),dpi=140)
fig.patch.set_facecolor('white');ax.set_facecolor('white')
ax.axhline(0,color='#6d7781',lw=1)
ax.plot(k,s,color='#225c8c',lw=2.5,label=r'$s(k)=k^2-k^4$')
ax.fill_between(k,0,s,where=(k<1),color='#d6e8d8',alpha=1)
km=1/np.sqrt(2)
ax.plot([km],[.25],'o',color='#b05330')
ax.annotate(r'$k=1/\sqrt{2},\quad s=1/4$',xy=(km,.25),xytext=(.07,.31),arrowprops={'arrowstyle':'->','color':'#b05330'},fontsize=11)
ax.axvline(1,color='#6d7781',lw=1,ls=':')
ax.text(.28,.045,'unstable',fontsize=11,color='#3f7250')
ax.text(1.07,-.25,'stable',fontsize=11,color='#555555')
ax.set(xlim=(0,1.3),ylim=(-1.2,.38),xlabel=r'Wavenumber $k$',ylabel=r'Growth rate $s$')
ax.set_title('Thermocapillary growth competing with capillary damping')
ax.legend(loc='lower left');ax.grid(alpha=.18)
fig.tight_layout()
fig.savefig('paper-44-dispersion.png',facecolor='white',transparent=False)
plt.close(fig)
