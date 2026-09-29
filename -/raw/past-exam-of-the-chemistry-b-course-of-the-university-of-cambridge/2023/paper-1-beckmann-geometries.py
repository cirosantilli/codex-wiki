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
fig,axes=plt.subplots(1,2,figsize=(11,4.6))
for ax,name,side in zip(axes,['B → D: aromatic-side migration','C → E: spiro-side migration'],[-1,1]):
 K=np.array([-.4,0]);N=np.array([.8,0]);ra=np.array([-1.3,.9]);rs=np.array([-1.3,-.9]);OH=np.array([1.6,side*.9])
 d.bond(ax,K,N,2);d.atom(ax,K,'K');d.atom(ax,N,'N');d.bond(ax,K,ra);d.atom(ax,ra,'Rₐ');d.bond(ax,K,rs);d.atom(ax,rs,'Rₛ');d.bond(ax,N,OH);d.atom(ax,OH,'OH')
 ax.annotate('',(-1.65,-.8),(-1.65,.8),arrowprops={'arrowstyle':'-','connectionstyle':'arc3,rad=.7','ls':'dotted','color':'0.45'})
 ax.text(-2.2,0,'ring\ntether',ha='center',fontsize=9)
 moving=ra if side==-1 else rs;d.curly(ax,(-.9,.45 if side==-1 else -.45),(.6,.12 if side==-1 else -.12),rad=-.4*side)
 ax.text(0,-1.65,'O-tosylation → anti migration → nitrilium → water → lactam',ha='center',fontsize=10)
 ax.text(0,1.65,'Rₐ = path towards arene; Rₛ = path towards spiro junction',ha='center',fontsize=9,color=d.BLUE)
 d.finish(ax,(-2.7,2.25),(-2,2),name)
fig.tight_layout();d.save(fig,'paper-1-beckmann-geometries.png')
