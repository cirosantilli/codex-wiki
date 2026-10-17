"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
d=np.linspace(2,30,600)
fig,ax=plt.subplots(figsize=(7,4.1),layout='constrained')
ax.plot(d,1337*(1-.96/d),color='#2479ad',lw=2,label=r'$T_m(d)=1337(1-0.96\,\mathrm{nm}/d)\ \mathrm{K}$')
ax.axhline(1337,color='#555555',ls='--',label='Bulk limit: 1337 K')
ax.plot(3,909.16,'o',color='#bb5029')
ax.annotate('3 nm, 909 K',(3,909.16),(8,900),arrowprops=dict(arrowstyle='->'),color='#bb5029')
ax.set(xlabel='Particle diameter (nm)',ylabel='Model melting temperature (K)',ylim=(600,1410),xlim=(1.5,30),title='Capillarity estimate, not an atomistic extrapolation')
ax.legend(loc='lower right',fontsize=9)
fig.savefig('paper-2-gold-melting.png',dpi=170,facecolor='white')
