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

fig,ax=plt.subplots(figsize=(10,4));fig.subplots_adjust(top=.82);finish(ax,(-.5,11),(-1.8,2.8),'The quench fixes which propene carbon bonds to the naphthyl arm')
atom(ax,(1.5,1.6),'Ar–CH(Me)–CH₂–Hf',17);flow(ax,(4,1.6),(5.7,1.6),'H₂O workup');atom(ax,(8.2,1.6),'Ar–CH(Me)₂',17)
ax.text(5.4,.7,'Hf–N(amido) also becomes NH on hydrolysis',ha='center',fontsize=11,color=BLUE)
atom(ax,(1.5,-.3),'Ar–CH₂–CH(Me)–Hf',15);flow(ax,(4,-.3),(5.7,-.3),'alternative orientation');atom(ax,(8.2,-.3),'Ar–CH₂–CH₂Me',15)
ax.text(8.2,-1.1,'n-propyl: inconsistent with the drawn quench product',ha='center',fontsize=10,color=ORANGE)
save(fig,Path(__file__).with_suffix('.png').name)
