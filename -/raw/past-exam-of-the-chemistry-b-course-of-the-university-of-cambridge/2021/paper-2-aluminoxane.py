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
fig,ax=plt.subplots(figsize=(7,7.0),layout='constrained')
th=np.arange(6)*np.pi/3;front=np.column_stack([1.3*np.cos(th),.55*np.sin(th)]);back=front+np.array([.45,2.2])
for pts in [front,back]:ring(ax,pts)
for a,b in zip(front,back):bond(ax,a,b)
for lev,pts in enumerate([front,back]):
    for j,p in enumerate(pts):
        isal=(j+lev)%2==0
        atom(ax,p,'Al' if isal else 'O',color=BLUE if isal else ORANGE)
        if isal:
            v=p-(np.array([.45,2.2]) if lev else np.array([0.,0.]));v=v/(np.linalg.norm(v) or 1);e=p+.55*v;bond(ax,p,e);atom(ax,e,'R',size=11)
ax.text(.25,-1.4,'6 Al, 6 O, 18 Al–O connections',ha='center')
ax.text(.25,-1.75,'Al: three O + R; each O: three Al',ha='center')
finish(ax,(-2.2,2.7),(-2.1,3.6),'One compatible (RAlO)₆ cage')
save(fig,'paper-2-aluminoxane.png')
