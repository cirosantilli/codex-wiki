from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 10, "savefig.facecolor": "white"})

def sensitivity(j,beta,mu):
 q=np.sqrt(1-beta);eps=(q*(1+1/j))**(2/3)-1
 h=1-q*(1-eps/2);d=1-q*(1+eps)**(-1.5)
 return 6*mu**2/(q*eps**2*h**3*d**2*(1+eps)**2.5)
def critical(beta,mu):
 q=np.sqrt(1-beta);lo=1.;hi=q/(1-q)*(1-1e-9) if beta else 1e5
 for _ in range(85):
  mid=(lo+hi)/2
  if sensitivity(mid,beta,mu)>1:hi=mid
  else:lo=mid
 return (lo+hi)/2
beta=np.linspace(0,.15,241)
fig,ax=plt.subplots(figsize=(7.,4.3),dpi=100,facecolor='white')
for mu,col in [(1e-5,'#b52b35'),(1e-6,'#1269a8'),(1e-7,'#308341')]:
 ax.plot(beta,[critical(b,mu) for b in beta],color=col,label=rf'$M_p/M_\star={mu:.0e}$')
b=np.linspace(.03,.15,241);q=np.sqrt(1-b)
ax.plot(b,q/(1-q),color='gray',ls='--',label='Largest geometrically exterior index')
ax.set(xlabel=r'Radiation-pressure coefficient $\beta$',ylabel='Critical first-order resonance index j',title='Local encounter estimate: stronger planets destabilize lower indices',xlim=(0,.15),ylim=(0,55))
ax.grid(alpha=.18);ax.legend(fontsize=9);fig.tight_layout()
fig.savefig(Path.cwd()/'paper-63-radiative-resonance-boundary.png',dpi=100,facecolor='white')
