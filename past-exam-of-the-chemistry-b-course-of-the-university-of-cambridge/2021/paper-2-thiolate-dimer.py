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
fig,ax=plt.subplots(figsize=(7,4.8),layout='constrained')
co=[(0,1),(0,-1)];ss=[(-1.4,0),(1.4,0)]
for c in co:
    for s in ss:bond(ax,c,s)
bond(ax,co[0],co[1],color=ORANGE,lw=2.6)
for c in co:atom(ax,c,'Co');end=(0,c[1]*1.85);bond(ax,c,end);atom(ax,end,'η⁵-Cp')
for s in ss:atom(ax,s,'S');end=(s[0]*1.7,0);bond(ax,s,end);atom(ax,end,'Me')
ax.text(2.2,1.25,'no S–S bond',ha='center',color=ORANGE)
finish(ax,(-3,3),(-2.5,2.5),'[CpCo(μ-SMe)]₂: two sulfur bridges plus Co–Co')
save(fig,'paper-2-thiolate-dimer.png')
