"""Original calculated illustration; Python3.14,NumPy,Matplotlib; PNG output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
g=9.8;rho=1000.;sig=.072;B=1e-10;c=8e-5;L=.06;k11=np.sqrt(2)*np.pi/L
ratio=lambda k:np.sqrt((1+B*k**4/(rho*g+sig*k*k))/(1+c*k))
fig,axs=plt.subplots(1,2,figsize=(10,4),facecolor='white',layout='constrained')
k=np.geomspace(1,1e7,1500);axs[0].plot(k,ratio(k),color='#296c9e');axs[0].set_xscale('log');axs[0].set_yscale('log')
axs[0].axhline(1,color='.5',ls=':');axs[0].axvline(1e4,color='#ad5932',ls='--',label='ka = 1; thin-sheet caution')
axs[0].set(xlabel=r'Wavenumber k / m$^{-1}$',ylabel=r'Frequency ratio $\omega_s/\omega_0$',title='Formal continuation of the supplied model');axs[0].legend(fontsize=8)
k=np.linspace(0,300,500);axs[1].plot(k,ratio(k),color='#296c9e');axs[1].plot(k11,ratio(k11),'o',color='#ad5932');axs[1].annotate('Pinned square fundamental\nk = 74.05 / m',xy=(k11,ratio(k11)),xytext=(110,.9985),arrowprops=dict(arrowstyle='->'),fontsize=9)
axs[1].set(xlabel=r'Wavenumber k / m$^{-1}$',ylabel='Frequency ratio',title='Small-k mass loading lowers frequency')
for ax in axs:ax.grid(alpha=.2)
fig.savefig('paper-2-covered-water-dispersion.png',dpi=150,facecolor='white');plt.close(fig)
