"""Original explanatory figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

lam=np.geomspace(.05,300,2200)
def thermal(T):
 x=14387.76877/(lam*T)
 shape=x**4/np.expm1(np.minimum(x,700))
 return shape/shape.max()
star=thermal(80000);dust=.85*thermal(150)
x=14387.76877/(lam*1e4);gas=.3*x*np.exp(-x);gas/=gas.max();gas*=.20
# Schematic Balmer discontinuity and broad two-photon contribution; no fitted object is represented.
gas*=np.where(lam<.3646,1.25,1.)
twoph=.11*np.exp(-.5*(np.log(lam/.24)/.42)**2);twoph*=np.maximum(0,1-.1216/lam);twoph[lam<.1216]=0
lines=np.zeros_like(lam)
for centre,height in [(.1909,.22),(.4861,.14),(.5007,.60),(.6563,.35),(2.12,.1),(12.8,.25)]:lines+=height*np.exp(-.5*(np.log(lam/centre)/.009)**2)
fig,ax=plt.subplots(figsize=(10,4.7),layout='constrained')
ax.semilogx(lam,star,lw=2.2,color='#68468c',label='Hot central-star continuum')
ax.semilogx(lam,gas+twoph,lw=2.2,color='#126782',label='Nebular continua')
ax.semilogx(lam,dust,lw=2.2,color='#a44418',label='Warm-dust continuum')
ax.semilogx(lam,lines,lw=1.1,color='#5d8062',label='Representative emission lines')
for ll,name,where in [(.1909,'C III]',(.105,.72)),(.5007,'[O III]',(.65,.8)),(12.8,'[Ne II]',(3.7,.51))]:
 index=np.argmin(abs(lam-ll));ax.annotate(name,xy=(ll,lines[index]),xytext=where,arrowprops={'arrowstyle':'->','color':'#5d8062'},fontsize=11,color='#4a6950')
ax.axvline(.3646,lw=.8,ls=':',color='#888888');ax.text(.36,.43,'Balmer edge',rotation=90,ha='right',fontsize=10)
ax.set(xlim=(.05,300),ylim=(0,1.13),xlabel='Rest wavelength (micrometres)',ylabel=r'Schematic $\nu F_\nu$ (arbitrary units)',title='A planetary-nebula spectrum contains several physical emitters')
ax.legend(loc='upper right',fontsize=10);ax.grid(alpha=.18)
fig.suptitle('Illustrative component shapes and line positions; relative amplitudes are deliberately arbitrary',fontsize=12)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
