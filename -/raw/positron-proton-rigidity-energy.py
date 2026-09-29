"""Compare kinetic energies at equal magnetic rigidity in a chosen example.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; output is written to the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
fig,(ax,table)=plt.subplots(1,2,figsize=(9.6,5.5),gridspec_kw={'width_ratios':[1.15,1]})
fig.suptitle('Equal bending fixes momentum, not particle mass',fontsize=15,y=.97)
B=1.0
r=np.linspace(.5,12,400)  # cm
pc=299.792458*B*r/100  # MeV
masses=[.511,938.272]
colors=['#1768ac','#bd4b00']
for mass,name,color in zip(masses,['positron','proton'],colors):
    k=pc**2/(np.hypot(pc,mass)+mass)
    ax.plot(r,k,color=color,lw=2.5,label=name)
    for rc in [5,10]:
        p=299.792458*rc/100
        kval=p*p/(np.hypot(p,mass)+mass)
        ax.plot(rc,kval,'o',color=color,ms=7)
for rc,label in [(5,'after'),(10,'before')]:
    ax.axvline(rc,color='#999999',ls=':',lw=1,zorder=0)
    ax.text(rc,50,label,ha='center',fontsize=10)
ax.set_yscale('log')
ax.set(xlim=(0,12),ylim=(.001,80),xlabel='Radius $r$ (cm), for $B=1$ T',ylabel='Kinetic energy $K$ (MeV)')
ax.grid(axis='y',alpha=.18); ax.legend(loc='lower right',frameon=False)
ax.spines[['top','right']].set_visible(False)
table.axis('off')
table.text(.5,.95,'Chosen inputs, not historical data',ha='center',fontsize=12,transform=table.transAxes)
rows=[]
for mass,name in zip(masses,['Positron','Proton']):
    vals=[]
    for rc in [10,5]:
        p=299.792458*rc/100
        vals.append(p*p/(np.hypot(p,mass)+mass))
    rows.append([name,f'{vals[0]:.3f}',f'{vals[1]:.3f}'])
t=table.table(cellText=rows,colLabels=['Hypothesis','Before','After'],loc='center',bbox=[.01,.52,.98,.30],cellLoc='center')
t.auto_set_font_size(False);t.set_fontsize(11)
for (i,j),cell in t.get_celld().items():
    cell.set_edgecolor('#cccccc')
    if i==0: cell.set_facecolor('#edf1f4')
table.text(.5,.85,'$K$ in MeV',ha='center',transform=table.transAxes)
table.text(.05,.42,'Same momenta for both hypotheses:\n29.979 → 14.990 MeV/$c$',transform=table.transAxes,linespacing=1.6)
table.text(.05,.20,'Independent range information is needed\nto reject the proton hypothesis.\nNo material stopping curve is assumed.',transform=table.transAxes,linespacing=1.6)
fig.text(.5,.035,'Rounded rest energies: 0.511 MeV (positron), 938.272 MeV (proton) • exact relativistic formula',ha='center',fontsize=10)
fig.subplots_adjust(left=.09,right=.98,bottom=.15,top=.85,wspace=.28)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=130,facecolor='white')
plt.close(fig)
