"""Original illustrative Franck-Condon progression, not source data.
Python3.14/NumPy2.3/Matplotlib3.10. PNG basename output in cwd.
"""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
S=0.85;width=.08
x=np.linspace(-.4,6,1800);n=np.arange(7)
w=np.array([np.exp(-S)*S**int(j)/math.factorial(int(j)) for j in n])
y=sum(v*np.exp(-.5*((x-j)/width)**2)/(np.sqrt(2*np.pi)*width) for j,v in zip(n,w))
fig,ax=plt.subplots(figsize=(7.5,3.4),layout="constrained")
ax.plot(x,y,color="#155d82",lw=2,label="Broadened illustrative lines")
ax.vlines(n,0,w/(np.sqrt(2*np.pi)*width),color="#b56c1b",alpha=.7,lw=1.4)
for j,v in zip(n[:4],w[:4]):ax.text(j+.10,v/(np.sqrt(2*np.pi)*width)+.07,r"$\nu=%d$"%j,fontsize=10)
ax.set(xlabel=r"$(\hbar\omega-E_{00})/(\hbar\omega_v)$",ylabel="Illustrative absorption (arbitrary units)",title=r"Single displaced vibration: $S=0.85$, Gaussian width $0.08\,\hbar\omega_v$")
ax.set_ylim(0,max(y)*1.16)
fig.savefig("paper-1-aqc2013-vibronic-absorption.png",dpi=140,facecolor="white",bbox_inches="tight")
