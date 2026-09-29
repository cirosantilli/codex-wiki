"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,ax=plt.subplots(figsize=(8.1,3.8),layout='constrained');a=.5e-9;v=2000;mn=1.67e-27;hb=1.054571817e-34
s=np.linspace(0,2.5,1600);q=s*np.pi/a;phon=2*v/a*abs(np.sin(q*a/2));recoil=hb*q*q/(2*mn)
ax.plot(s,phon/1e12,c='#176493',lw=2,label='Acoustic branch (extended zone)');ax.plot(s,recoil/1e12,c='#b64b24',lw=2,label='Perpendicular neutron recoil')
s2=np.linspace(1,2,200);ax.plot(s2,(4*v/a-2*v*(s2*np.pi/a)/np.pi)/1e12,'--',c='0.45',label='Linear chord')
qr=1.0693440843e10;wr=hb*qr*qr/(2*mn);ax.plot(qr*a/np.pi,wr/1e12,'ko');ax.annotate('Nonzero intersection',xy=(qr*a/np.pi,wr/1e12),xytext=(1.45,8.3),arrowprops={'arrowstyle':'->'},ha='center')
for x in [1,2]:ax.axvline(x,c='0.8',ls=':',lw=.9)
ax.set(xlabel=r'Extended transfer $Qa/\pi$',ylabel=r'Angular frequency ($10^{12}$ rad/s)',xlim=(0,2.5),ylim=(0,10));ax.legend(loc='upper left',fontsize=8)
fig.savefig("paper-1-phonon-transfer.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
