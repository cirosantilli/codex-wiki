"""Compare linear decibel loss with exponential surviving power.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is written to the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
z=np.linspace(0,10,501)
alpha=0.2
loss=alpha*z
fraction=np.power(10.0,-loss/10.0)
fig,axs=plt.subplots(1,2,figsize=(10.8,5.4),dpi=100)
fig.subplots_adjust(left=0.085,right=0.97,bottom=0.29,top=0.77,wspace=0.28)
axs[0].plot(z,loss,lw=2.8,color='#a95b1a')
axs[1].plot(z,fraction,lw=2.8,color='#006b83')
for ax in axs:
    ax.set_xlim(0,10)
    ax.set_xticks([0,2,4,6,8,10])
    ax.set_xlabel('Distance z (km)')
    ax.grid(alpha=0.25)
    ax.spines[['top','right']].set_visible(False)
    ax.axvline(5,color='#777777',ls=':',lw=1)
axs[0].set_ylim(0,2.25);axs[0].set_ylabel('Positive loss A(z) (dB)')
axs[1].set_ylim(0.55,1.035);axs[1].set_ylabel('Surviving power P(z) / P(0)')
axs[0].set_title('Losses add',loc='left');axs[1].set_title('Power fractions multiply',loc='left')
for pos in [0,5,10]:
    axs[0].plot(pos,alpha*pos,'o',color='#a95b1a',clip_on=False)
    axs[1].plot(pos,10**(-alpha*pos/10),'o',color='#006b83',clip_on=False)
axs[0].annotate('5 km: 1 dB',(5,1),xytext=(2.1,1.5),arrowprops={'arrowstyle':'->','color':'#a95b1a'},color='#874716')
axs[0].annotate('10 km: 2 dB',(10,2),xytext=(5.2,1.9),color='#874716')
axs[1].annotate('5 km: 0.794328',(5,10**(-0.1)),xytext=(0.6,0.69),arrowprops={'arrowstyle':'->','color':'#006b83'},color='#006b83')
axs[1].annotate('10 km: 0.630957',(10,10**(-0.2)),xytext=(4.0,0.585),arrowprops={'arrowstyle':'->','color':'#006b83'},color='#006b83')
fig.suptitle('Optical fibre: distance and surviving power',fontsize=18,y=0.95)
fig.text(0.5,0.85,r'Illustrative uniform model: $\alpha_{\rm dB}=0.2\ \mathrm{dB/km}$',ha='center',fontsize=13)
fig.text(0.5,0.15,r'$1\ \mathrm{dB}+1\ \mathrm{dB}=2\ \mathrm{dB}$     ↔     $10^{-0.1}\times10^{-0.1}=10^{-0.2}$',ha='center',fontsize=14)
fig.text(0.5,0.065,'Model curves, not measured traces • Excludes launch, connector and bend losses • Not a universal fibre coefficient',ha='center',fontsize=10)
fig.savefig(Path.cwd()/f'{Path(__file__).stem}.png',facecolor='white',transparent=False)
plt.close(fig)
