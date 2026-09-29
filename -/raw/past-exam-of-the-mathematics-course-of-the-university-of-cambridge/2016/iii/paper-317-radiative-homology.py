"""Formal HR slopes, Python 3.14 and root Matplotlib/NumPy dependencies.
Writes one opaque basename PNG to cwd; Make chooses the final _media cwd.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-.16,.16,200)
fig,ax=plt.subplots(figsize=(8.4,4.2),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,(284/69)*x,lw=2.5,color='#2069a0',label=r'pp burning + Kramers opacity: slope $284/69$')
ax.plot(x,(76/9)*x,lw=2.5,color='#bb5920',label=r'CNO burning + electron scattering: slope $76/9$')
ax.axhline(0,lw=.8,color='#b0b0b0');ax.axvline(0,lw=.8,color='#b0b0b0')
ax.scatter([0],[0],s=30,color='#444444',zorder=4)
ax.set(xlim=(.165,-.165),ylim=(-1.45,1.45),xlabel=r'$\log_{10}(T_{\rm eff}/T_{\rm eff,ref})$',ylabel=r'$\log_{10}(L/L_{\rm ref})$')
ax.set_title('Idealized radiative homology sequences',fontsize=12)
ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=9,framealpha=1)
ax.text(.015,.035,'Separate reference normalizations; the intersection is not a physical mass crossover.',transform=ax.transAxes,fontsize=8,bbox=dict(facecolor='white',edgecolor='none',pad=3))
ax.annotate('hotter',xy=(.105,-1.22),xytext=(.045,-1.22),ha='center',va='center',fontsize=9,arrowprops=dict(arrowstyle='->',color='#444444'))
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.1,right=.98,bottom=.17,top=.88)
fig.savefig('paper-317-radiative-homology.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
