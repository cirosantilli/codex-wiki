"""Qualitative cooling sketch; emit an opaque PNG basename in caller cwd only."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
xt=np.array([4.0,np.log10(15000),4.35,4.65,4.85,5.0,5.2,5.5,5.9,6.2,6.6,7.0,7.5,8.0])
yt=np.array([-23.8,-21.8,-22.0,-22.7,-22.4,-22.15,-22.55,-23.1,-23.5,-23.4,-23.2,-23.0,-22.75,-22.5])
x=np.linspace(4,8,800);y=np.interp(x,xt,yt)
metals=y+1.3*np.exp(-((x-5.6)/.9)**2)
fig,ax=plt.subplots(figsize=(8,4.4),dpi=100,facecolor='white');ax.set_facecolor('white')
ax.plot(x,y,lw=2.5,color='#254c83',label='Metal-free H/He guide')
ax.plot(x,metals,lw=1.8,ls='--',color='#aa4936',label='Enriched guide (schematic)')
ax.scatter([np.log10(15000),7],[-21.8,-23.0],color='#254c83',s=34,zorder=4)
ax.annotate('Supplied H-line label\n15,000 K; -21.8',xy=(np.log10(15000),-21.8),xytext=(4.35,-21.2),fontsize=9,arrowprops=dict(arrowstyle='-',color='#555'))
ax.annotate('He line/ionization feature',xy=(5.0,-22.15),xytext=(5.07,-22.65),fontsize=9,arrowprops=dict(arrowstyle='-',color='#555'))
ax.annotate('Supplied label\n10 million K; -23.0',xy=(7,-23),xytext=(6.5,-23.85),fontsize=9,arrowprops=dict(arrowstyle='-',color='#555'))
ax.text(7.35,-22.05,r'Free-free: $\Lambda\propto T^{1/2}$',ha='center',fontsize=10)
ax.set_xlim(4,8);ax.set_ylim(-24.1,-20.9);ax.set_xlabel(r'$\log_{10}(T/\mathrm{K})$',fontsize=12)
ax.set_ylabel(r'$\log_{10}[\Lambda/(\mathrm{erg\,cm^3\,s^{-1}})]$',fontsize=12)
ax.set_title('Primordial atomic cooling: qualitative shape',fontsize=14);ax.grid(alpha=.18)
ax.legend(loc='upper right',fontsize=9)
fig.text(.5,.025,'Optically thin collisional-equilibrium sketch; enriched curve is illustrative, not a rate table.',ha='center',fontsize=9,color='#444')
fig.subplots_adjust(left=.11,right=.98,bottom=.17,top=.89)
fig.savefig('paper-61-primordial-cooling.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
