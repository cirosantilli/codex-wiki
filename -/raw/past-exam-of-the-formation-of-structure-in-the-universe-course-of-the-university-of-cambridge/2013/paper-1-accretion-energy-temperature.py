"""Original ideal constant-radius accretion scalings; Python3.14,NumPy,Matplotlib; output cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(.002,1,500)
fig,axs=plt.subplots(1,2,figsize=(10,4.1),facecolor='white',layout='constrained')
a=axs[0]
a.plot(x,x*x/2,label=r'Radiated $E_{acc}$',color='#b3542c')
a.plot(x,-x*x,label=r'Potential energy $\Omega$',color='#2567a5')
a.plot(x,-x*x/2,label=r'Total energy $E=\Omega/2$',color='#28694b')
a.set(xlabel=r'Mass fraction $M/M_f=t/t_f$',ylabel=r'Energy / $(GM_f^2/r_0)$',title='Zero seed; constant radius; binding coefficient q = 1')
a.axhline(0,color='.4',lw=.8);a.legend(fontsize=9);a.grid(alpha=.2)
b=axs[1];b.plot(x,x**.25,color='#b3542c',label=r'Surface effective $T_{eff}/T_{eff,f}$')
b.plot(x,x,color='#2567a5',label=r'Homologous interior $T_{vir}/T_{vir,f}$')
b.set(xlabel=r'Elapsed accretion time $t/t_f$',ylabel='Temperature relative to its own final value',title='Different meanings of temperature')
b.legend(fontsize=8,loc='lower right');b.grid(alpha=.2)
b.text(.04,.86,r'$T_{eff}\propto t^{1/4}$',transform=b.transAxes,color='#b3542c')
b.text(.12,.2,r'$T_{vir}\propto t$',transform=b.transAxes,color='#2567a5')
fig.savefig('paper-1-accretion-energy-temperature.png',dpi=150,facecolor='white');plt.close(fig)
