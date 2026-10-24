# Original figure. Tested Python3.14, NumPy2.3.5, Matplotlib3.10.7.
# Run from the desired output directory; writes one same-basename PNG to CWD.
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

K=1.;Kd=.5;si=1.;kp=1.;c0=1.
se=np.linspace(0,25,1000);J=.5*Kd*K*kp*c0*(se-si)/((si+K+Kd)*(se+K+Kd)-Kd**2);plateau=.5*Kd*K*kp*c0/(si+K+Kd)
fig,ax=plt.subplots(figsize=(8,4.4),layout='constrained');ax.plot(se,J,lw=2,label='Net inward flux');ax.axhline(0,color='grey',lw=.8);ax.axhline(plateau,color='tab:orange',ls='--',label='Finite carrier-limited plateau');ax.plot(si,0,'ko');ax.annotate('Reversal at $s_e=s_i$',xy=(si,0),xytext=(5,-.045),arrowprops=dict(arrowstyle='->'));ax.set(xlabel='Exterior free substrate $s_e$ (concentration units)',ylabel='Inward transport $J$ (flux units)',title='Passive carrier transport reverses and saturates');ax.legend(loc='lower right');ax.grid(alpha=.2)

fig.savefig(Path.cwd()/"2009-carrier-flux.png",dpi=150)
