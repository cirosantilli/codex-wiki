"""Original solution diagram; Python 3.14, matplotlib 3.10, numpy 2.3.
Run from the mirrored media directory: PNG basename is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save,wedge,BLUE,ORANGE

fig,ax=plt.subplots(figsize=(7,4));finish(ax,(-.4,5),(-1.7,2.4),'Conditional azimuthal averaging of a polymer segment')
flow(ax,(0,0),(2,0));flow(ax,(2,0),(4,1.4));ax.text(1,.2,'ℓᵢ₊₁',ha='center',fontsize=15);ax.text(3,1,'ℓᵢ₊₂',fontsize=15)
bond(ax,(2,0),(4,0),style='dashed',color=BLUE);bond(ax,(4,0),(4,1.4),style='dashed',color=ORANGE)
ax.text(3,-.4,'ℓ cos α',ha='center',fontsize=14,color=BLUE);ax.text(4.25,.65,'u⊥',fontsize=14,color=ORANGE)
ax.text(3.3,-1.2,'Uniform dihedral rotation:  ⟨u⊥⟩ = 0',ha='center',fontsize=13)
save(fig,Path(__file__).with_suffix('.png').name)
