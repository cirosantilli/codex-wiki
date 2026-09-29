"""Original qualitative graphene plots. Plateau widths are illustrative only."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(2,2,figsize=(10,7.1),layout='constrained')
k=np.linspace(-1,1,500)
axes[0,0].plot(k,abs(k),color='#126782',label='Conduction')
axes[0,0].plot(k,-abs(k),color='#b3561b',label='Valence')
axes[0,0].set(xlabel='Wavevector through K (scaled)',ylabel='Energy (scaled)',title='Section through two touching Dirac cones')
axes[0,0].legend(fontsize=10,frameon=False)
v=np.linspace(-3,3,600)
axes[0,1].plot(v,1/np.sqrt(v*v+.12),color='#126782',lw=2.3)
axes[0,1].set(xlabel=r'$V_g-V_D$ (scaled)',ylabel='Resistance (arbitrary units)',title='Rounded neutrality peak: illustrative')
axes[0,1].text(.12,.8,'Holes',transform=axes[0,1].transAxes)
axes[0,1].text(.7,.8,'Electrons',transform=axes[0,1].transAxes)
B=np.linspace(.08,30,4000)
C=41.35667697
# Smooth steps centred at half-filled extended levels. The smoothing and
# amplitudes are chosen to show the sequence, not to fit a disorder model.
x=C/(4*B)
j=np.arange(1,201)[:,None]
steps=.5*(1+np.tanh((x[None,:]-j)/.065))
filled=steps.sum(axis=0)
nu=2+4*filled
rxy=25.81280745/nu
rxx=np.sum(np.exp(-((x[None,:]-j)/.09)**2),axis=0)*np.exp(-.8/B)
axes[1,0].plot(B,rxy,color='#126782',lw=2)
axes[1,0].set(xlabel='B (T)',ylabel=r'$|\rho_{xy}|$ (k$\Omega$)',title='Fourfold Hall sequence, schematic',xlim=(0,30),ylim=(0,14))
for nu0 in [2,6,10]:
    b=C/nu0
    axes[1,0].scatter([b],[25.81280745/nu0],s=20,color='#b3561b',zorder=4)
    axes[1,0].annotate(rf'$\nu={nu0}$',(b,25.81280745/nu0),xytext=(5,-18),textcoords='offset points',fontsize=10)
axes[1,1].plot(B,rxx,color='#126782',lw=1.6)
axes[1,1].set(xlabel='B (T)',ylabel=r'$\rho_{xx}$ (arbitrary units)',title='Extended-level peaks: schematic widths',xlim=(0,30),ylim=(0,1.1))
for n in [1,2,3]:
    b=C/(4*n)
    axes[1,1].axvline(b,color='.7',ls=':',lw=1)
    axes[1,1].text(b+.15,.82,f'{b:.2f} T',rotation=90,fontsize=9)
fig.suptitle(r'$n=10^{16}\ \mathrm{m}^{-2}$; no spin or valley splitting',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
