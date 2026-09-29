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

fig,ax=plt.subplots(figsize=(10,4));finish(ax,(-1,10),(-1.5,2.4),'Grob fragmentation · aligned donor–bond–leaving-group array')
pts=[(.2,.3),(2,.3),(3.8,.3),(5.6,.3),(7.4,.3)]
for a,b in zip(pts,pts[1:]):bond(ax,a,b)
for pos,t in zip(pts,['O⁻','Cₐ','Cᵦ','Cγ','OTs']):atom(ax,pos,t,16)
curly(ax,(.5,.6),(1.35,.55),rad=-.6);curly(ax,(2.8,.45),(4.7,.5),rad=-.55);curly(ax,(6.4,.45),(7.4,.7),rad=-.5)
ax.text(3.8,-.6,'O=Cₐ    +    Cᵦ=Cγ    +    OTs⁻',ha='center',fontsize=17,color=BLUE)
ax.text(3.8,-1.2,'The remaining scaffold connects the two product fragments into one molecule.',ha='center',fontsize=10)
save(fig,Path(__file__).with_suffix('.png').name)
