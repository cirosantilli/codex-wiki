"""Schematic homojunction bands, not a fitted device solution; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(11, 4.7), layout='constrained', facecolor='white')
x = np.linspace(-4, 4, 600); Eg=3.4
for ax, bias, title in zip(axs, [0, 2.5], ['Equilibrium', 'Forward bias: barrier lowered by 2.5 eV']):
    ec = 0.1 + (Eg-0.2-bias)*(1-np.tanh(x))/2; ev=ec-Eg
    ax.plot(x, ec, color='#245c9f', lw=2, label=r'Conduction edge $E_c$'); ax.plot(x, ev, color='#21633d', lw=2, label=r'Valence edge $E_v$')
    ax.axvspan(-1, 1, color='0.5', alpha=0.07)
    if bias == 0:
        ax.axhline(0, color='0.35', ls='--', label='Fermi level')
        ax.annotate('Internal electric field', (-2.3, -3.55), (1.1, -3.55), fontsize=10, arrowprops={'arrowstyle':'->', 'color':'#b45309'})
    else:
        ax.plot([-4,-0.4],[-bias,-bias],ls='--',color='0.35');ax.text(-3.9,-bias+0.12,'Hole quasi-Fermi level',fontsize=9)
        ax.plot([0.4,4],[0,0],ls='--',color='0.35');ax.text(0.55,-0.48,'Electron quasi-Fermi level',fontsize=9)
        ix=np.argmin(np.abs(x));mid=ec[ix]
        ax.annotate('',(0,mid-Eg+0.15),(0,mid-0.15),arrowprops={'arrowstyle':'->','color':'#b45309','lw':2})
        ax.text(0.2,mid-Eg/2,'Photon\n≈ Eɡ',color='#b45309',fontsize=11)
        ax.annotate('Electron injection',(-2,1.2),(0.3,1.2),fontsize=9,arrowprops={'arrowstyle':'->','color':'#245c9f'})
        ax.annotate('Hole injection',(1.9,-3.5),(-2.2,-3.5),fontsize=9,arrowprops={'arrowstyle':'->','color':'#21633d'})
    ax.text(-3.6,3.6,'p type',fontsize=12);ax.text(2.3,3.6,'n type',fontsize=12)
    ax.set(xlim=(-4,4),ylim=(-3.9,4),xlabel='Position across junction (schematic)',ylabel='Electron energy / eV',title=title)
    ax.spines[['top','right']].set_visible(False);ax.set_xticks([])
axs[0].legend(loc='upper left',bbox_to_anchor=(0.02,0.80),fontsize=9,frameon=False)
fig.savefig(Path('paper-2-gan-junction.png'),dpi=140,facecolor='white');plt.close(fig)
