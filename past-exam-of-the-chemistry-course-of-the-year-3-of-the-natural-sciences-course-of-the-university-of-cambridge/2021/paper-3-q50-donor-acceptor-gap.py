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

fig,axs=plt.subplots(1,2,figsize=(8,4.5));fig.subplots_adjust(left=.05,right=.98,top=.85,bottom=.17,wspace=.3)
for ax,name,homo in zip(axs,['Fluorene donor','Cyclopentadithiophene donor'],[-2,-1]):
 ax.set(xlim=(-1,1),ylim=(-2.7,2));ax.axis('off');ax.set_title(name,fontsize=12)
 ax.hlines(homo,-.7,.7,color=BLUE,lw=2);ax.hlines(1.2,-.7,.7,color=ORANGE,lw=2)
 ax.text(0,homo-.4,'donor-rich HOMO',ha='center',fontsize=10);ax.text(0,1.5,'acceptor-rich LUMO',ha='center',fontsize=10)
 ax.annotate('',(.1,1.15),(.1,homo+.05),arrowprops={'arrowstyle':'<->','color':'0.2'});ax.text(.25,(1.2+homo)/2,'gap',fontsize=11)
fig.suptitle('Qualitative donor–acceptor frontier-level comparison',fontsize=14);fig.text(.5,.04,'Stronger donor raises HOMO → narrower optical gap; no numerical energies implied.',ha='center',fontsize=10)
save(fig,Path(__file__).with_suffix('.png').name)
