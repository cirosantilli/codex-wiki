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

fig,axs=plt.subplots(3,1,figsize=(10,7));fig.subplots_adjust(top=.91,bottom=.04,hspace=.55)
rows=[('1 · Insertion into Hf–Ar','Ar–CH₂–CH(Hf)–CH₂OEt','The Hf–Me bond is still present.'),('2 · β-Alkoxide elimination','Ar–CH₂–CH=CH₂   +   Hf–OEt','C–O cleavage is coupled to C=C formation.'),('3 · Tethered alkene inserts into Hf–Me','Ar–CH₂–CH(Hf)–CH₂Me','Second allyl ethyl ether binds through O; it remains intact.')]
for ax,(title,s,note) in zip(axs,rows):
 ax.axis('off');ax.set_title(title,loc='left',fontsize=13,color=BLUE);ax.text(.5,.6,s,ha='center',fontsize=19);ax.text(.5,.15,note,ha='center',fontsize=11)
fig.suptitle('Atom-balanced route to the enlarged chelate of G',fontsize=15)
save(fig,Path(__file__).with_suffix('.png').name)
