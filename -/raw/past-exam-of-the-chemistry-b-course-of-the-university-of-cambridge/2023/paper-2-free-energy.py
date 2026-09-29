"""Original illustrative amide-rotation profiles. Python 3.14; PNG to cwd."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import save
T=298.;delta=8.314462618*T*np.log(25)/1000
x=np.linspace(0,1,501);shape=np.sin(np.pi*x)**2
fig,ax=plt.subplots(figsize=(8,4.6),facecolor='white')
ax.plot(x,80*shape,lw=2.5,color='#245c9f',label='Chloroform: illustrative barrier 80 kJ mol⁻¹')
ax.plot(x,(80+delta)*shape,lw=2.5,color='#b45309',label=f'Water: higher barrier by {delta:.2f} kJ mol⁻¹ at 298 K')
ax.annotate('',(.5,80+delta),(.5,80),arrowprops={'arrowstyle':'<->','color':'0.2','lw':1.2})
ax.text(.56,85,'RT ln 25',fontsize=12)
ax.text(.03,6,'Planar rotamer',fontsize=10);ax.text(.74,6,'Planar rotamer',fontsize=10);ax.text(.39,55,'Twisted\ntransition region',ha='center',fontsize=11)
ax.set(xlim=(0,1),ylim=(-2,103),xlabel='Amide torsional reaction coordinate (not time)',ylabel='G relative to each solvent’s starting minimum / kJ mol⁻¹')
ax.legend(loc='upper center',fontsize=9,frameon=False);ax.spines[['top','right']].set_visible(False)
fig.text(.5,.015,'Chosen absolute barriers and equal endpoint energies are schematic, not measured. Only the relative rate ratio is supplied.',ha='center',fontsize=8)
fig.tight_layout(rect=(0,.04,1,1));save(fig,'paper-2-free-energy.png',dpi=150)
