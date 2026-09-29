"""Original chemistry solution figure; Python 3.14, numpy and matplotlib.
Run from the desired output directory. No source figures or media paths are used.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
import chemistry_diagram as d
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,4,figsize=(15,4.2))
a,b,c,e=axes
for ax,title in zip(axes,['A: tetrahedral N⁺','A: pyramidal sulfoxide','B: trans, diequatorial chair','C: tetrahedral phosphorus']):d.finish(ax,(-1.8,1.8),(-1.8,1.8),title)
d.atom(a,(0,0),'N⁺');d.bond(a,(-.15,.1),(-1,.9));d.atom(a,(-1,.9),'Ph');d.bond(a,(-.15,-.1),(-1,-.9));d.atom(a,(-1,-.9),'Et');d.wedge(a,(.12,.1),(.9,.9));d.atom(a,(.9,.9),'Me');d.wedge(a,(.12,-.1),(.9,-.8),False);d.atom(a,(.9,-.9),'CH₂CH₂S(O)Me',9)
d.atom(b,(0,0),'S⁺');d.bond(b,(-.1,.05),(-1,.8));d.atom(b,(-1,.8),'chain');d.wedge(b,(.1,.1),(1,.8));d.atom(b,(1,.8),'O⁻',14);d.wedge(b,(.1,-.1),(.9,-.9),False);d.atom(b,(.9,-.9),'Me');d.atom(b,(-.6,-.65),'··',17);b.text(0,-1.6,'two unlike carbon groups + O + lone pair',ha='center',fontsize=8)
pts,axial,eq=d.chair(c,(0,0),scale=.85)
for i in [0,3]:d.bond(c,pts[i],eq[i]);d.atom(c,eq[i],'Me',11)
c.plot(0,0,'o',color=d.ORANGE,ms=4);c.text(0,-1.5,'r ↦ −r maps the complete chair onto itself',ha='center',fontsize=8);d.bond(c,pts[0],pts[3],style='dotted',lw=.8,color=d.ORANGE)
d.atom(e,(0,0),'P');d.bond(e,(-.1,.1),(-1,1),2);d.atom(e,(-1,1),'O');d.bond(e,(-.1,-.1),(-1,-1));d.atom(e,(-1,-1),'OEt');d.wedge(e,(.1,.1),(1,1));d.atom(e,(1,1),'OMe');d.wedge(e,(.1,-.1),(1,-1),False);d.atom(e,(1,-1),'OPh')
fig.tight_layout();d.save(fig,'paper-1-stereochemical-models.png')
