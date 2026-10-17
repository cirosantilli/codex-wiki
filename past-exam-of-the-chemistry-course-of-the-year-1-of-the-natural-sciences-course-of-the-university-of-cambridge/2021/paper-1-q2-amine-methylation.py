"""Original solution diagram. Python 3.14 / matplotlib 3.10 / numpy 2.3.
Run from the mirrored media directory; output is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,ring,curly,flow,finish,save,BLUE,ORANGE

fig,ax=plt.subplots(figsize=(10,3.2));finish(ax,(-.4,11),(-1.1,2.2),'N-methylation by backside attack')
atom(ax,(1.6,.7),'HOCH₂CH₂–NMe₂:',15);atom(ax,(5,.7),'CH₃',15);atom(ax,(6.2,.7),'I',15);bond(ax,(5.28,.7),(6.04,.7))
curly(ax,(3.18,.78),(4.8,.8),rad=-.45);curly(ax,(5.7,.73),(6.2,.9),rad=-.5)
flow(ax,(6.7,.7),(7.5,.7));atom(ax,(9,.9),'[HOCH₂CH₂–NMe₃]⁺',14);atom(ax,(9,.2),'I⁻',14)
ax.text(2.8,-.25,'N lone pair → methyl carbon',color=ORANGE,ha='center',fontsize=11);ax.text(5.8,-.7,'C–I bond pair → iodine',color=ORANGE,ha='center',fontsize=11)
save(fig,Path(__file__).with_suffix('.png').name)
