"""Original explanatory figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

h=6.62607015e-34;kb=1.380649e-23;nu1=115.3e9;nu3=345.8e9;A1=7.2e-8;A3=2.5e-6;L1=1.33e24
T=np.geomspace(5,400,500);J=np.arange(180);Tr=h*nu1/(2*kb)
weights=(2*J[:,None]+1)*np.exp(-Tr*J[:,None]*(J[:,None]+1)/T)
f1=weights[1]/weights.sum(axis=0)
N1=L1/(A1*h*nu1);mass=N1/f1*28*1.66053906660e-27/1.98847e30
C=7/3*A3/A1*nu3/nu1;E31=h*(230.5e9+nu3)/kb;ratio=C*np.exp(-E31/T);observed=2.46e26/L1;Tobs=E31/np.log(C/observed)
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
axs[0].semilogx(T,ratio,color='#126782',lw=2.5);axs[0].axhline(observed,color='#a44418',ls='--',label='Observed luminosity ratio');axs[0].axhline(C,color='#777777',ls=':',label='High-temperature limit')
axs[0].plot(Tobs,observed,'o',color='#a44418');axs[0].set(xlabel='Excitation temperature (K)',ylabel=r'$L_{32}/L_{10}$',title='Optically thin LTE line ratio',ylim=(0,265));axs[0].legend(fontsize=10)
axs[1].loglog(T,mass,color='#126782',lw=2.5)
axs[1].plot([20,Tobs],[.01881654426,.07358530412],'o',color='#a44418')
axs[1].annotate('20 K: 0.019 solar masses',xy=(20,.01881654426),xytext=(7,.04),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=10)
axs[1].annotate('101 K: 0.074 solar masses',xy=(Tobs,.07358530412),xytext=(37,.18),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=10)
axs[1].set(xlabel='Excitation temperature (K)',ylabel='Inferred CO mass (solar masses)',title='CO mass at fixed 1–0 luminosity')
for ax in axs:ax.grid(alpha=.22,which='both')

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
