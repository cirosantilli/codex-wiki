"""Original stellar EOS sketch. Python3.14/matplotlib3.10.7/numpy2.3.5.
Publication basename paper-317-eos-regimes.py; PNG written only to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k=1.380649e-16
hbar=6.62607015e-27/(2*np.pi)
c=2.99792458e10
me=9.1093837139e-28
mu=1.66053906892e-24
mu_e=2.0
mu_mol=4/3
a=np.pi**2*k**4/(15*hbar**3*c**3)
rho_star=mu_e*mu/(3*np.pi**2)*(me*c/hbar)**3
T_star=me*c*c/k
rho=np.logspace(-8,10,600)
x=(rho/rho_star)**(1/3)
TF=T_star*x*x/(np.sqrt(1+x*x)+1)
Tgas=(3*k*rho/(a*mu_mol*mu))**(1/3)
# Direct cold-pressure quadrature, stable at small Fermi momentum.
pu,pw=np.polynomial.legendre.leggauss(128)
pu=(pu+1)/2;pw=pw/2
pressure=me**4*c**5/(3*np.pi**2*hbar**3)*x**5*np.sum(pw[None,:]*pu[None,:]**4/np.sqrt(1+x[:,None]**2*pu[None,:]**2),axis=1)
Tdeg=(3*pressure/a)**.25
T=np.logspace(8,10.6,240)
node,weight=np.polynomial.legendre.leggauss(256)
y=80*(node+1)
weight=80*weight
energy=np.sqrt(y[None,:]**2+(T_star/T[:,None])**2)
e=np.exp(-energy)
integral=np.sum(weight[None,:]*y[None,:]**2*e/(1+e),axis=1)
n0=(k*T/(hbar*c))**3*integral/np.pi**2
rhopair=mu_e*mu*n0
fig,ax=plt.subplots(figsize=(10,6.5),dpi=100,facecolor='white')
ax.set_xscale('log');ax.set_yscale('log')
ax.set_xlim(1e-8,1e10);ax.set_ylim(1e4,10**10.6)
ax.fill_between(rho,1e4,TF,color='#245b93',alpha=.09)
ax.plot(rho,TF,color='#245b93',lw=2.2,label='T = kinetic electron Fermi temperature')
ax.axvline(rho_star,color='#245b93',ls=':',lw=1.5,label='Degenerate-electron relativity: pF = mec')
ax.axhline(T_star,color='#8060a0',ls='--',lw=1.4,label='Thermal electron relativity: kT = mec²')
ax.plot(rho,Tgas,color='#887634',ls='-.',lw=1.5,label='Photon pressure = classical gas pressure')
ax.plot(rho,Tdeg,color='#438089',ls='--',lw=1.4,label='Photon pressure = cold electron pressure')
ax.plot(rhopair,T,color='#ba512e',lw=2,label='Pairs become abundant: n₀(T) ≈ net ne')
box={'facecolor':'white','edgecolor':'none','alpha':.85,'pad':3}
ax.text(2e2,2e5,'Degenerate electrons\nnonrelativistic',fontsize=11,ha='center',bbox=box)
ax.text(7e7,3e6,'Degenerate electrons\nrelativistic',fontsize=11,ha='center',bbox=box)
ax.text(5e-6,8e4,'Classical ion/electron gas\nnonrelativistic',fontsize=11,ha='center',bbox=box)
ax.text(6e-3,1.2e10,'Thermal relativistic region\nincluding abundant pairs',fontsize=11,ha='center',bbox=box)
ax.text(2e-4,8e8,'Photon pressure can dominate',fontsize=10,color='#78662c',ha='center',bbox=box)
ax.set_xlabel('Mass density ρ [g cm⁻³]');ax.set_ylabel('Temperature T [K]')
ax.set_title('Approximate stellar EOS regimes: fully ionized helium (μe=2, μ=4/3)')
ax.grid(which='major',alpha=.16)
ax.legend(loc='lower right',fontsize=8.5,framealpha=1)
fig.text(.5,.025,'Crossovers are approximate; net-electron degeneracy curve excludes thermal pairs. Nuclear matter is outside this ideal model.',ha='center',fontsize=8.5)
fig.tight_layout(rect=(0,.055,1,1))
fig.savefig(Path.cwd()/'paper-317-eos-regimes.png',facecolor='white',transparent=False)
plt.close(fig)
