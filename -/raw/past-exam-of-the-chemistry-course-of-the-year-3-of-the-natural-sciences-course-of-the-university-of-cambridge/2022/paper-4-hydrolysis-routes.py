"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(10.5,5.1),layout='constrained')
boxes=[
(.12,.82,'Neutral p-hydroxy ester C'),
(.12,.30,'Phenoxide ester C⁻'),
(.49,.82,'Tetrahedral intermediate\nOH⁻ addition to neutral ester'),
(.49,.30,'Quinoid ketene + ArO⁻\nFragmentation of C⁻'),
(.88,.82,'Hydroxybenzoate\nRegion 2: β = −0.35'),
(.88,.30,'Water capture\nRegion 1: β = −1.33')]
for x,y,t in boxes:ax.text(x,y,t,ha='center',va='center',transform=ax.transAxes,fontsize=10,bbox={'boxstyle':'round,pad=.55','facecolor':'#eef4fa','edgecolor':'#2166ac'})
for a,b in [((.08,.69),(.08,.43)),((.22,.82),(.32,.82)),((.65,.82),(.76,.82)),((.20,.30),(.34,.30)),((.65,.30),(.78,.30))]:
    ax.annotate('',xy=b,xytext=a,xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.5})
ax.text(.20,.56,'OH⁻ / H₂O\nacid–base equilibrium',ha='center',transform=ax.transAxes,fontsize=9)
ax.text(.53,.05,'Additional OH⁻ attack on C⁻ → tetrahedral route (region 3)\nrate ∝ [C⁻][OH⁻] ∝ [C][OH⁻]²; β = −0.20',ha='center',transform=ax.transAxes,fontsize=10)
ax.set_title('Parallel pathways explain kinetic order and leaving-group slopes');ax.axis('off')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
