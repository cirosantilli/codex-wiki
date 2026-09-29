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

fig,ax=plt.subplots(figsize=(9,4.8));finish(ax,(-3,8),(-2,2.8),'Strained donor–acceptor cyclophanediene · connectivity schematic')
atom(ax,(0,1.6),'F',20);atom(ax,(0,-.6),'BT',20)
for side in [-1,1]:
 bond(ax,(side*.3,1.6),(side*1.5,1.6));bond(ax,(side*1.5,1.6),(side*1.5,-.6),2);bond(ax,(side*1.5,-.6),(side*.4,-.6))
 atom(ax,(side*1.5,1.6),'CH',12);atom(ax,(side*1.5,-.6),'CH',12)
flow(ax,(2.1,.5),(3.7,.5),'Ru alkylidene; ROMP')
atom(ax,(5.5,.5),'[–F–CH=CH–BT–CH=CH–]ₙ',13)
ax.text(4.9,-.3,'Ring strain → chain growth',ha='center',fontsize=12,color=BLUE)
ax.text(1.8,-1.5,'F: 9,9-dioctylfluorene-2,7-diyl   ·   BT: 4,7-benzothiadiazolylene',ha='center',fontsize=11)
save(fig,Path(__file__).with_suffix('.png').name)
