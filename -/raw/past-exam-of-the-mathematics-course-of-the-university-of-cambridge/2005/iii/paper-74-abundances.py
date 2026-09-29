"""Original qualitative BBN sketch, NOT a numerical nuclear-network prediction.
Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7; opaque basename to CWD.
Caller MPLCONFIGDIR is respected.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

eta=np.linspace(1,10,600)
d=2.6e-5*(6/eta)**1.6
he3=1.05e-5*(6/eta)**.6
li7=.75e-10*((2.5/eta)**2+(eta/2.5)**2)
y=.232+.0025*eta
fig,ax=plt.subplots(figsize=(8.2,5.7),constrained_layout=True)
bx=ax.twinx()
ax.semilogy(eta,d,label='Deuterium / H',lw=2,color='#176580')
ax.semilogy(eta,he3,label='Helium-3 / H',lw=2,color='#a05c22')
ax.semilogy(eta,li7,label='Lithium-7 / H (including late Be-7 decay)',lw=2,color='#6956a5')
bx.plot(eta,y,label='Helium-4 mass fraction (right axis)',lw=2,color='#2b8b57')
ax.set(xlim=(1,10),ylim=(5e-11,4e-4),xlabel=r'Baryon-to-photon ratio $\eta_{10}=10^{10} n_B/n_\gamma$',ylabel='Number ratio to hydrogen (logarithmic)',title='Schematic primordial abundance trends\nIllustrative curves; not reaction-network calculations')
bx.set(ylim=(.21,.28),ylabel='Helium-4 mass fraction (linear)')
top=ax.secondary_xaxis('top',functions=(lambda x:x/274,lambda x:x*274))
top.set_xlabel(r'Equivalent baryon density $\Omega_b h^2$')
lines1,labels1=ax.get_legend_handles_labels();lines2,labels2=bx.get_legend_handles_labels()
ax.legend(lines1+lines2,labels1+labels2,loc='center right',fontsize=8)
ax.axvline(6,color='0.5',ls='--',lw=1)
ax.text(6.08,1e-8,'Representative density',fontsize=8,rotation=90)
ax.grid(alpha=.15)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white',transparent=False)
