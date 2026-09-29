"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig=plt.figure(figsize=(10,6.3),layout="constrained")
gs=fig.add_gridspec(2,2)
a=fig.add_subplot(gs[0,0]);bax=fig.add_subplot(gs[0,1]);s=fig.add_subplot(gs[1,:])
k=4e4;F=5.;drive=2*np.pi*10;m=F/(drive**2*1e-6);b=500.;Q=np.sqrt(m*k)/b
r=np.linspace(0,3,2500);H=1/(1-r*r+1j*r/Q)
a.plot(r,abs(H),color="#1565a8",lw=1.7)
bax.plot(r,np.angle(H)/np.pi,color="#ca6720",lw=1.7)
for ax in [a,bax]:
 ax.axvline(1,color=".5",ls="--",lw=1);ax.set_xlim(0,3);ax.set_xlabel(r"$\omega/\omega_0$");ax.grid(alpha=.15)
a.set(ylabel=r"$k|R|$",title=f"Light damping: Q = {Q:.1f}")
bax.set(ylabel=r"$\phi/\pi$",title="Displacement phase relative to force")
bax.set_yticks([0,-.5,-1],["0","−1/2","−1"])
M=m+20;beta=b/(2*M);w0=np.sqrt(k/M);wd=np.sqrt(w0*w0-beta*beta);delta=20*9.81/k
t=np.linspace(0,17,5000)
y=delta*(1-np.exp(-beta*t)*(np.cos(wd*t)+beta/wd*np.sin(wd*t)))
yc=delta*(1-(1+w0*t)*np.exp(-w0*t))
s.plot(t,1000*y,color="#1565a8",lw=1.25,label="b = 500 N s/m")
s.plot(t,1000*yc,color="#ca6720",lw=1.8,label="critical damping (comparison)")
s.axhline(1000*delta,color=".4",ls="--",lw=1)
s.text(12,1000*delta+.35,"new equilibrium: 4.905 mm",fontsize=9)
s.set(xlim=(0,17),ylim=(0,10),xlabel="Time after gentle load placement (s)",ylabel="Downward displacement (mm)",title="20 kg load step; small pre-existing 10 Hz vibration omitted")
s.legend(frameon=False,fontsize=9,loc="upper right");s.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
