from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axs=plt.subplots(1,2,figsize=(11.5,4.9),layout='constrained')
beta=.8;theta=np.linspace(0,np.pi,500);mu=np.cos(theta);muprime=(mu-beta)/(1-beta*mu);frac=(1-muprime)/2;half=np.degrees(np.arccos(beta))
axs[0].plot(np.degrees(theta),frac,color='#174c75',lw=2,label='boosted photon count');axs[0].plot(np.degrees(theta),(1-mu)/2,color='gray',ls='--',label='rest-frame isotropic count')
axs[0].axhline(.5,color='#b35b15',ls=':');axs[0].scatter([half],[.5],color='#b35b15',zorder=4);axs[0].annotate(r'$\cos\theta_{1/2}=\beta$',xy=(half,.5),xytext=(65,.3),arrowprops=dict(arrowstyle='->'),fontsize=12)
axs[0].set(xlabel='Cone half-angle (degrees)',ylabel='Fraction of photons inside cone',title='Illustrative boost: beta = 0.8',xlim=(0,180),ylim=(0,1));axs[0].legend(frameon=False,loc='lower right',fontsize=9)
u=np.linspace(-2,2,500);arrival=u/2+u**3/6
axs[1].plot(u,arrival,color='#174c75',lw=2);axs[1].scatter([-1,1],[-2/3,2/3],color='#b35b15',zorder=4)
axs[1].set(xlabel=r'Emission angle $u=\gamma\phi$',ylabel=r'$ct_{arr}\gamma^3/R$ (relative to tangent)',title=r'Arrival scale: $R/(c\gamma^3)$')
axs[1].text(0,2.35,r'$ct_{arr}\gamma^3/R\simeq u/2+u^3/6$',ha='center',fontsize=12)
for ax in axs:ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Relativistic beaming and the compressed synchrotron flash',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
