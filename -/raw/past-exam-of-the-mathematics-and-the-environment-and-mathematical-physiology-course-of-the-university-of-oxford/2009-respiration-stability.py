# Original figure. Tested Python3.14, NumPy2.3.5, Matplotlib3.10.7.
# Run from the desired output directory; writes one same-basename PNG to CWD.
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axes=plt.subplots(1,2,figsize=(10,4.3),layout='constrained');z=np.linspace(0,3,500);axes[0].plot(z,z+.2,label='$\\lambda+\\beta$, $\\beta=0.2$');axes[0].plot(z,-2*np.exp(-z),label='$-\\gamma e^{-\\lambda}$, $\\gamma=2$');axes[0].axhline(0,color='grey',lw=.8);axes[0].set(xlabel='Real candidate growth rate $\\lambda\\geq0$',ylabel='Characteristic-equation sides',title='No nonnegative real intersection');axes[0].legend(fontsize=8);axes[0].grid(alpha=.2)
w=np.linspace(np.pi/2,2.65,1000);beta=-w/np.tan(w);gain=w/np.sin(w);axes[1].plot(beta,gain,lw=2,label='Exact first Hopf boundary');axes[1].fill_between(beta,0,gain,color='tab:blue',alpha=.08);axes[1].plot(0,np.pi/2,'ko');axes[1].axhline(np.pi/2,color='grey',ls='--',label='$\\pi/2$: only the $\\beta=0$ limit');axes[1].text(.65,1,'Stable');axes[1].text(.35,2.8,'Oscillatory instability');axes[1].set(xlim=(0,3),ylim=(0,4),xlabel='Instantaneous feedback $\\beta$',ylabel='Delayed gain $\\gamma$',title='First imaginary-root crossing');axes[1].legend(fontsize=8,loc='lower right');axes[1].grid(alpha=.2)

fig.savefig(Path.cwd()/"2009-respiration-stability.png",dpi=150)
