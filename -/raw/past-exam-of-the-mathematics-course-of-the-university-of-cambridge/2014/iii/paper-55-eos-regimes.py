"""EOS crossover diagram for illustrative fully ionized carbon composition.
Only PNG basename output in cwd. Supply an owned MPLCONFIGDIR.
"""
import os
from pathlib import Path
if not os.environ.get('MPLCONFIGDIR'):
    raise RuntimeError('Supply an owned MPLCONFIGDIR before generating the figure')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
# Fixed cgs physical constants; labels use asymptotic ideal-matter comparisons.
k=1.380649e-16;mu0=1.66053906660e-24;me=9.1093837015e-28
c=2.99792458e10;hb=1.054571817e-27;arad=7.56573325e-15
mue=2.;mu=12/7
rho=np.logspace(-8,11,900);ne=rho/(mue*mu0)
x=hb*(3*np.pi**2*ne)**(1/3)/(me*c)
trel=me*c*c/k
# Rationalized difference avoids cancellation in the nonrelativistic Fermi energy.
tf=trel*x*x/(np.sqrt(1+x*x)+1)
pnr=hb*hb*(3*np.pi**2)**(2/3)*ne**(5/3)/(5*me)
pzero=np.empty_like(x);small=x<.03
pzero[small]=pnr[small]*(1-5*x[small]**2/14+5*x[small]**4/24)
z=x[~small]
pzero[~small]=me**4*c**5/(24*np.pi**2*hb**3)*(z*(2*z*z-3)*np.sqrt(1+z*z)+3*np.arcsinh(z))
tgas=(3*rho*k/(arad*mu*mu0))**(1/3)
tdeg=(3*pzero/arad)**.25
rrel=mue*mu0*(me*c/hb)**3/(3*np.pi**2)
fig,ax=plt.subplots(figsize=(8.6,6.4),dpi=100,facecolor='white');ax.set_facecolor('white')
ax.plot(np.log10(rho),np.log10(tf),color='#2463a2',lw=2,label=r'Electron degeneracy: $T=T_F$')
ax.plot(np.log10(rho),np.log10(tgas),color='#ad682a',lw=1.8,label=r'Radiation / classical gas: $P_\gamma=P_g$')
ax.plot(np.log10(rho),np.log10(tdeg),color='#9b3e85',lw=1.8,ls='--',label=r'Radiation / cold electrons: $P_\gamma=P_e(0)$')
ax.axvline(np.log10(rrel),color='#555555',lw=1.4,ls=':',label=r'Degenerate relativity: $p_F=m_ec$')
ax.axhline(np.log10(trel),color='#444444',lw=1.2,ls='-.',label=r'Thermal relativity scale: $k_BT=m_ec^2$')
ax.text(-5.7,8.4,'Radiation pressure',fontsize=12,color='#8b501f')
ax.text(-5.8,4.55,'Classical gas',fontsize=12,color='#34733e')
ax.text(1.5,5.15,'Nonrelativistic\ndegenerate electrons',fontsize=10.5,color='#245990')
ax.text(7.3,6.2,'Relativistic\ndegenerate electrons',fontsize=10.5,color='#245990')
ax.text(-7.6,3.35,'Ionization / molecules\n(composition dependent)',fontsize=9,color='#555555')
ax.text(5.8,3.4,'Coulomb corrections grow\n(not modeled by these curves)',fontsize=9,color='#555555')
ax.text(-1.4,10.25,'Thermal pairs can matter here;\nabundance depends on density',fontsize=9,color='#555555')
ax.set_xlim(-8,11);ax.set_ylim(3,11.15);ax.set_xlabel(r'$\log_{10}(\rho/[{\rm g\,cm^{-3}}])$');ax.set_ylabel(r'$\log_{10}(T/{\rm K})$')
ax.set_title('Stellar EOS crossovers: illustrative ionized carbon',fontsize=13,pad=12)
ax.grid(alpha=.18);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.14),ncol=2,fontsize=8.4,frameon=False)
fig.subplots_adjust(left=.09,right=.97,top=.90,bottom=.25)
fig.text(.5,.018,'Curves are comparisons of limiting models, not sharp phase boundaries or a complete EOS.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False);plt.close(fig)
