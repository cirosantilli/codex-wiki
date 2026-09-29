"""Original explanatory diagram; Python 3.14, matplotlib and numpy.
Run from the desired output directory; the PNG is written to that directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(2,1,figsize=(9,5.6),layout='constrained')
ax=axs[0]
bond(ax,(.3,0),(2.5,0));bond(ax,(2.5,0),(3.7,0))
for x,w,txt in [(.6,.9,'empty M σ'),(1.8,.8,'occupied CO 5σ')]:
    ax.add_patch(Ellipse((x,0),w,.6,fc='#e0ecfa',ec=BLUE,alpha=.8));ax.text(x,-.65,txt,ha='center')
atom(ax,(0,0),'M');atom(ax,(2.5,0),'C');atom(ax,(3.7,0),'O')
flow(ax,(1.65,.6),(.4,.6),'two-electron donation')
finish(ax,(-.5,4.5),(-1.1,1.2),'Sigma channel: carbon-end lone pair → metal')
ax=axs[1]
for x,y,sgn in [(.35,.43,'+'),(.35,-.43,'−'),(-.35,.43,'−'),(-.35,-.43,'+')]:
    ax.add_patch(Ellipse((x,y),.55,.75,fc='#e0ecfa' if sgn=='+' else '#fff0dd',ec=BLUE));ax.text(x,y,sgn,ha='center',va='center')
for x,signs in [(2.5,['+','−']),(3.7,['−','+'])]:
    for y,sgn in zip([.43,-.43],signs):
        ax.add_patch(Ellipse((x,y),.48,.72,fc='#e0ecfa' if sgn=='+' else '#fff0dd',ec=BLUE));ax.text(x,y,sgn,ha='center',va='center')
bond(ax,(0,0),(2.5,0));bond(ax,(2.5,0),(3.7,0))
for x,s in [(0,'M'),(2.5,'C'),(3.7,'O')]:atom(ax,(x,0),s)
flow(ax,(.7,1.05),(2.5,1.05),'occupied dπ → empty CO π*')
ax.text(0,-1.05,'occupied metal dπ',ha='center');ax.text(3.1,-1.05,'CO π*: opposite phases on C and O',ha='center')
finish(ax,(-.8,4.7),(-1.45,1.65),'Pi channel: metal → ligand; a second channel is perpendicular')
save(fig,'paper-2-carbonyl-orbitals.png')
