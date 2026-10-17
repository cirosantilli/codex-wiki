"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Writes one PNG basename to cwd; no source-image pixels or hardcoded media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(10.5,7),layout='constrained');a,b,c,d=axs.flat
t=np.linspace(0,1.4,400);therm=np.minimum(t**1.5,1);a.plot(t,therm,label=r"$N'/N$",lw=2);a.plot(t,1-therm,label=r'$N_0/N$',lw=2);a.axvline(1,color='gray',ls=':');a.set(xlabel=r'$T/T_c$',ylabel='Particle fraction',title='Fixed total particle number');a.legend(frameon=False)
n=np.linspace(0,2.5,400);b.plot(n,np.minimum(n,1),label=r"$N'/N_c$",lw=2);b.plot(n,np.maximum(n-1,0),label=r'$N_0/N_c$',lw=2);b.axvline(1,color='gray',ls=':');b.set(xlabel=r'$N/N_c(T)$',ylabel='Scaled particle count',title='Fixed temperature');b.legend(frameon=False)
# Dimensionless fixed-mu Bogoliubov interpolation, not a finite-T critical theory.
zeta3=2.612375348685488;zeta5=1.341487257250917;norm=np.sqrt(np.pi)/2*zeta3;mu_ratio=.04
x=np.geomspace(1e-9,70,6000);tt=np.geomspace(.0005,1,350);CC=[]
for r in tt:
 q=np.sqrt(x*(x+2*mu_ratio/r));integrand=np.sqrt(x)*q*q*np.exp(-q)/np.expm1(-q)**2;CC.append(r**1.5*np.trapezoid(integrand,x)/norm)
CC=np.array(CC);ideal=15/4*zeta5/zeta3*tt**1.5
for ax in [c,d]:
 ax.plot(tt,ideal,color='#1766a5',lw=2,label=r'Ideal: $T^{3/2}$');ax.plot(tt[tt<.5],CC[tt<.5],color='#c33c29',lw=2,label='Bogoliubov illustration');ax.plot(tt[tt>=.5],CC[tt>=.5],'--',color='#c33c29',lw=2);ax.axvline(mu_ratio,color='gray',ls=':');ax.set(xlabel=r'$T/T_c$',ylabel=r'$C_V/(Nk_B)$')
c.set(title='Crossover; dashed near-transition extrapolation',xlim=(0,1),ylim=(0,2.05));c.text(.42,.18,r'Illustration: $\mu/(k_BT_c)=0.04$',fontsize=8);c.legend(frameon=False,fontsize=8)
d.set(xscale='log',yscale='log',title='Bulk low-temperature power laws');d.text(.001,1e-7,r'Phonons: $T^3$',color='#c33c29');d.text(.002,4e-4,r'Free particles: $T^{3/2}$',color='#1766a5')
fig.savefig('paper-1-bose-gas.png',dpi=165);plt.close(fig)
