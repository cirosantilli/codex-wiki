"""Original amplitude/phase response of a resistor-fed parallel LC branch."""
import numpy as np
import matplotlib.pyplot as plt
x=np.geomspace(.02,50,1200);Q=1.;q=Q*(1/x-x)
lo=(np.sqrt(4+Q**(-2))-1/Q)/2;hi=(np.sqrt(4+Q**(-2))+1/Q)/2
fig,axes=plt.subplots(2,1,figsize=(8,6),sharex=True,facecolor='white',layout='constrained')
axes[0].semilogx(x,1/np.sqrt(1+q*q),color='#235c87',lw=2)
axes[0].axhline(1/np.sqrt(2),color='.6',ls=':',lw=1);axes[0].scatter([lo,hi],[1/np.sqrt(2)]*2,s=30,color='#b5671a',zorder=4)
axes[1].semilogx(x,np.rad2deg(np.arctan(q)),color='#235c87',lw=2)
for ax in axes:
    for val,ls in [(lo,':'),(1,'--'),(hi,':')]:ax.axvline(val,color='.55',ls=ls,lw=1)
    ax.grid(alpha=.15)
axes[0].set(ylabel=r'$|V_C/V_i|$',ylim=(0,1.12),title=r'Series-fed parallel LC: $Q=R\sqrt{C/L}=1$')
axes[0].annotate('Half-power points',(hi,1/np.sqrt(2)),xytext=(2.6,.9),arrowprops=dict(arrowstyle='->'),fontsize=11)
axes[1].set(xlabel=r'$\omega/\omega_0$',ylabel='Phase (degrees)',ylim=(-95,95),yticks=[-90,-45,0,45,90])
fig.savefig('paper-1-ia2010-lc-response.png',dpi=165,facecolor='white');plt.close(fig)
