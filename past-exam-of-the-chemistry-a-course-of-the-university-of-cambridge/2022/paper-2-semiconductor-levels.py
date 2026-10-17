"""Schematic energy-level diagrams only; gaps and shallow levels not to scale."""
from pathlib import Path
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,3,figsize=(9,4.5),layout='constrained')
for ax,title,fermi in zip(axes,['Intrinsic','Donor-doped, n type','Acceptor-doped, p type'],[.5,.70,.30]):
    ax.axhspan(-.30,0,color='#d7e4f4');ax.axhspan(1,1.30,color='#e6edf3')
    ax.plot([.08,.92],[0,0],color='#245c9f',lw=1.6)
    ax.plot([.08,.92],[1,1],color='#245c9f',lw=1.6)
    ax.plot([.08,.92],[fermi,fermi],color='#37774b',ls='--',lw=1.5)
    ax.text(.1,fermi+.035,'$E_F$',color='#37774b',fontsize=11)
    ax.text(.50,1.15,'conduction band',ha='center',fontsize=10)
    ax.text(.50,-.17,'valence band',ha='center',fontsize=10)
    ax.text(.95,1,'$E_c$',va='center',fontsize=11);ax.text(.95,0,'$E_v$',va='center',fontsize=11)
    ax.set(xlim=(0,1.15),ylim=(-.3,1.3));ax.axis('off');ax.set_title(title,fontsize=12)
axes[0].annotate('',(.75,1),(.75,0),arrowprops={'arrowstyle':'<->','color':'0.3'})
axes[0].text(.80,.53,'$E_g$',fontsize=12,va='center')
axes[1].plot([.15,.85],[.89,.89],color='#b45309',ls=':',lw=2)
axes[1].text(.60,.83,'$E_D$',color='#b45309',fontsize=11)
axes[2].plot([.15,.85],[.11,.11],color='#b45309',ls=':',lw=2)
axes[2].text(.60,.15,'$E_A$',color='#b45309',fontsize=11)
fig.suptitle('Band edges, Fermi levels and shallow impurity levels',fontsize=13)
fig.supxlabel('Energy increases upwards. Fermi levels are illustrative; shallow binding energies and the gap are not to scale.',fontsize=9)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
plt.close(fig)
