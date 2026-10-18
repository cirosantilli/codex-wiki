"""Original recoil and scattering estimates; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,2,figsize=(12.3,4.8),layout='constrained',facecolor='white');x=np.linspace(0,2,500)
a=axs[0];a.plot(x,x*x,lw=2.5,label='Free-electron recoil',color='#2563eb');a.plot(x,x,lw=2.2,label='Acoustic quantum',color='#dc2626');a.scatter([1],[1],color='#7c3aed',zorder=4);a.annotate(r'$q=1/\lambda$',xy=(1,1),xytext=(.25,2.2),arrowprops=dict(arrowstyle='->'),fontsize=12);a.set(xlabel=r'Transferred wave number $q\lambda$',ylabel=r'Energy in units of $\hbar c_s/\lambda$',title='Electronic and acoustic recoil scales',xlim=(0,2),ylim=(0,4));a.legend(fontsize=10);a.grid(alpha=.2)
b=axs[1];eta=np.linspace(0,.02,500);exact=1-np.sqrt(1-eta);linear=eta/2;b.plot(eta,exact,lw=2.5,label=r'Exact $1-\sqrt{1-\eta}$',color='#2563eb');b.plot(eta,linear,lw=2,ls='--',label=r'Linear $\eta/2$',color='#dc2626');ed=1/240;dd=1-np.sqrt(1-ed);b.scatter([ed],[dd],color='#7c3aed',zorder=5);b.annotate('Debye-cutoff example\nη = 1/240, δ ≈ 0.00209',xy=(ed,dd),xytext=(.0009,.0065),arrowprops=dict(arrowstyle='->'),fontsize=10);b.set(xlabel=r'Lost energy fraction $\eta=\epsilon/E_F$',ylabel=r'Fractional radial loss $\delta$',title='Nearly elastic at the Fermi surface',xlim=(0,.02),ylim=(0,.0108));b.ticklabel_format(axis='x',style='plain');b.legend(loc='lower right',fontsize=10);b.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
