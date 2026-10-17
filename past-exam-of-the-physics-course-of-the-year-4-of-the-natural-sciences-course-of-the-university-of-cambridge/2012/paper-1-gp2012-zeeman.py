"""Calculated weak-field sodium positions, not a reconstruction of an exam spectrum."""
import numpy as np
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,1,figsize=(8,5.5),facecolor='white',layout='constrained',sharex=True)
for ax, label, shifts in [(axes[0],r'$D_1$: $J_u=1/2$',np.array([-4,-2,2,4])/3),(axes[1],r'$D_2$: $J_u=3/2$',np.array([-5,-3,-1,1,3,5])/3)]:
    ax.vlines(shifts,0,1,color='#235d87',lw=2.7)
    ax.axvline(0,color='#ba6a1c',ls='--',lw=1,label='Zero-field position')
    ax.axhline(0,color='.5',lw=.8)
    ax.set(ylim=(-.05,1.3),yticks=[],ylabel=label)
    for value in shifts:
        numerator=round(value*3)
        text=str(numerator//3) if numerator%3==0 else str(numerator)+'/3'
        ax.text(value,1.08,text,ha='center',fontsize=11)
axes[1].set(xlim=(-2,2),xlabel=r'Photon-energy shift / $(\mu_B B)$')
fig.suptitle('Weak-field sodium: allowed line positions\nEqual heights schematic; dashed orange marks zero shift',fontsize=13)
fig.savefig('paper-1-gp2012-zeeman.png',dpi=165,facecolor='white')
plt.close(fig)
