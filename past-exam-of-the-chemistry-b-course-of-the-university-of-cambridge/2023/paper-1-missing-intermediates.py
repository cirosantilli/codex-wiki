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
fig,(a,b)=plt.subplots(1,2,figsize=(13,5.4),gridspec_kw={'width_ratios':[1,1.3]})
h=np.array([[-1,1],[-.15,.5],[-.15,-.5],[-1,-1],[-1.85,-.5],[-1.85,.5]])
p=np.array([[1.3,1.4],[2.15,.8],[1.85,-.2],[.8,-.2],[.5,.8]])
d.ring(a,h,{5:2});d.ring(a,p,{1:2});d.bond(a,h[1],p[3]);d.bond(a,h[0],(-1,1.9));d.atom(a,(-1,1.9),'N(pyrrolidine)',11)
d.bond(a,p[0],(1.3,2.2),2);d.atom(a,(1.3,2.2),'O');d.bond(a,p[1],(2.9,1));d.atom(a,(2.9,1),'Me')
for i,q in enumerate(h):a.text(q[0]-.22,q[1]+.10,'h'+str(i+1),fontsize=9,color=d.BLUE)
for i,q in enumerate(p):a.text(q[0]+.10,q[1]+.10,'p'+str(i+1),fontsize=9,color=d.BLUE)
a.annotate('',p[2],h[5],arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=.45','color':d.ORANGE,'lw':1.8});a.text(-.8,-1.9,'Next bond: h₆–p₃\nN on h₁ becomes iminium',ha='center',color=d.ORANGE)
d.finish(a,(-2.6,3.5),(-2.4,2.7),'B2(b): B, after elimination')
th=np.pi/2-np.arange(6)*np.pi/3
left=np.column_stack((np.cos(th),np.sin(th)))+[-1.7,0]
right=np.column_stack((np.cos(th),np.sin(th)))+[1.7,0]
d.ring(b,left,{0:2,2:2,4:2});d.ring(b,right,{0:2,2:2,4:2})
# Each ether attachment is ortho to the respective CH2-amide / nitro substituent.
d.bond(b,left[1],(-.7,1.4));d.atom(b,(-.7,1.4),'O',14);d.bond(b,(-.5,1.4),right[5])
d.bond(b,left[2],(-.4,-.9));d.atom(b,(-.4,-.9),'CH₂',12);d.bond(b,(-.15,-.9),(.55,-1.5));d.atom(b,(.8,-1.7),'C(=O)–N(morpholine)',10)
d.bond(b,right[4],(.6,-.9));d.atom(b,(.6,-.9),'NO₂',12)
b.annotate('',right[5],(-.4,-.9),arrowprops={'arrowstyle':'->','color':d.ORANGE,'lw':1.6,'connectionstyle':'arc3,rad=-.15'})
b.text(0,-2.45,'G: O–aryl attachment precedes the orange C–aryl closure.\nThe aryl–O bond then breaks; the original oxygen becomes OH.',ha='center',fontsize=10,color=d.ORANGE)
d.finish(b,(-3.1,3.1),(-2.9,2.5),'B2(c): diaryl ether G')
fig.tight_layout();d.save(fig,'paper-1-missing-intermediates.png')
