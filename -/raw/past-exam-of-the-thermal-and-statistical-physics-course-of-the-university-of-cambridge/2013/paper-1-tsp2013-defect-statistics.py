"""Original four-microstate defect statistics; Python 3.14, NumPy, Matplotlib.
Chosen beta*U=12 illustrates the low-temperature regime. PNG basename to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-6,18,3001);gap=12;z=np.exp(x);q=np.exp(-gap);Z=1+2*z+q*z*z;n=(2*z+2*q*z*z)/Z;var=2*z*(1+2*q*z+q*z*z)/Z**2
fig=plt.figure(figsize=(9.0,5.8),layout='constrained');gs=fig.add_gridspec(2,2);a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[0,1]);d=fig.add_subplot(gs[1,:])
a.plot(x,2*z/(1+z),color='#2a719d',lw=2);a.axvline(0,color='0.6',ls=':');a.set(xlim=(-6,6),ylim=(-.05,2.08),title='U = 0: a single two-electron step',ylabel=r'$\bar n$',xlabel=r'$(\mu-\epsilon)/(k_BT)$')
b.plot(x,n,color='#a84d35',lw=2);b.axvline(0,color='0.6',ls=':');b.axvline(gap,color='0.6',ls=':');b.set(xlim=(-6,18),ylim=(-.05,2.08),title=r'$U/(k_BT)=12$: one-electron plateau',ylabel=r'$\bar n$',xlabel=r'$(\mu-\epsilon)/(k_BT)$')
d.plot(x,var,color='#3b8066',lw=2);d.axhline(.25,color='0.6',ls='--');d.plot([0,gap],[2/9,2/9],'o',color='#a84d35',ms=5)
for xp in [-np.log(2),gap+np.log(2)]:d.axvline(xp,color='0.6',ls=':',lw=.8)
d.annotate('Bare crossings: variance → 2/9',xy=(0,2/9),xytext=(3,.19),arrowprops={'arrowstyle':'->'},fontsize=10)
d.text(6,.262,'Peaks → 1/4, shifted by ∓ kBT ln 2',ha='center',fontsize=10)
d.set(xlim=(-6,18),ylim=(-.01,.29),ylabel=r'$\mathrm{Var}\,n$',xlabel=r'$(\mu-\epsilon)/(k_BT)$',title='Charge fluctuations concentrate at the two thermally broadened steps')
fig.savefig('paper-1-tsp2013-defect-statistics.png',dpi=140,facecolor='white')
