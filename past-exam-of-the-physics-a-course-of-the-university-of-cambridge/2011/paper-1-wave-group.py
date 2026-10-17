"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(1,2,figsize=(9.3,3.9),layout='constrained')
x=np.linspace(-1,7,3000);env=np.where((x>=0)&(x<=6),np.minimum(1,np.minimum(x/.35,(6-x)/.35)),0);env=np.maximum(env,0)
y=env*np.cos(2*np.pi*(x-.25))
axs[0].plot(x,y,c='#176493');axs[0].plot(x,env,'k--',lw=.8);axs[0].plot(x,-env,'k--',lw=.8)
axs[0].annotate('Crests: 2 units/s',xy=(4,1.4),xytext=(1,1.4),arrowprops={'arrowstyle':'->'})
axs[0].annotate('Envelope: 1 unit/s',xy=(4,-1.45),xytext=(1,-1.45),arrowprops={'arrowstyle':'->'})
axs[0].set(xlim=(-1,7),ylim=(-1.8,1.8),xlabel='Position / wavelength',ylabel='Surface elevation (arbitrary)',title='Instantaneous packet: six crests')
ax=axs[1];tt=np.linspace(0,6,1000)
for j in range(-6,6):
 xp=j+.25+tt;mask=(xp>=0)&(xp<=6);ax.plot(xp[mask],tt[mask],c='#176493',lw=.85)
 hit=(6-j-.25)/2;ax.plot(6-hit,hit,'o',ms=3,c='#b64b24')
ax.plot(6-tt,tt,c='#b64b24',lw=2,label='Ship')
ax.axvline(0,c='0.3',ls='--');ax.axvline(6,c='0.3',ls='--')
ax.set(xlim=(-.4,6.4),ylim=(0,6),xlabel='Position in envelope frame / wavelength',ylabel='Time (chosen units)',title='Envelope frame: twelve crossings')
ax.text(.2,5.5,'Crests →',color='#176493');ax.text(3.9,4.7,'← Ship',color='#b64b24')
fig.savefig("paper-1-wave-group.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
