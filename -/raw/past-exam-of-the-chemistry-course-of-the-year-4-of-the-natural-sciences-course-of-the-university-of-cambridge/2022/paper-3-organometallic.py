"""Original solution diagram. Python 3.14, NumPy and Matplotlib.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, wedge, save
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig,axes=plt.subplots(1,3,figsize=(12,3.3))
for ax in axes:ax.set_aspect('equal');ax.set_axis_off()
ax=axes[0]
for a,b in [((0,0),(1,0)),((0,0),(-.8,.8)),((1,0),(1.8,.8))]:bond(ax,a,b,order=2 if b==(1,0) else 1)
atom(ax,(-1,1),'chain');atom(ax,(2,1),'Br');atom(ax,(0,-.9),'H');atom(ax,(1,-.9),'H')
bond(ax,(0,0),(0,-.7));bond(ax,(1,0),(1,-.7));ax.set(xlim=(-1.6,2.7),ylim=(-1.4,1.6));ax.set_title('36(a): Z terminal unit')
ax=axes[1];p=[(0,0),(1,0),(1,1),(0,1)]
for i in range(4):bond(ax,p[i],p[(i+1)%4])
for xy,t in zip(p,[r'Cp$_2$Ti',r'CH$_2$',r'C',r'CH$_2$']):atom(ax,xy,t)
bond(ax,(1,1),(1.7,1.5));bond(ax,(1,1),(1.7,.8));atom(ax,(2,1.6),'Ph');atom(ax,(2,.8),'OMe')
ax.set(xlim=(-1,2.7),ylim=(-1,2));ax.set_title('Cyclic precursor')
ax=axes[2];p=[(0,0),(1,0),(1.7,.8)]
bond(ax,p[0],p[1]);bond(ax,p[1],p[2],order=2)
atom(ax,(-2.2,0),r'Cp$_2$Ti(OMe)');bond(ax,(-1.35,0),(-.2,0));atom(ax,(0,0),r'CH$_2$');atom(ax,(1,0),'C');atom(ax,(1.9,1),r'CH$_2$');bond(ax,(1,0),(1,-.7));atom(ax,(1,-1),'Ph')
ax.set(xlim=(-3.7,2.8),ylim=(-1.5,1.5));ax.set_title('36(b): B, allyltitanium')
fig.tight_layout();save(fig,'paper-3-organometallic.png')
