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
fig,ax=plt.subplots(figsize=(8,5));ax.set_aspect('equal');ax.axis('off')
p={'B':(0,1),'u':(-1,1.5),'D':(-2,1),'E':(-2,0),'v':(-1,-.5),'C':(0,0),'A':(1,1.5),'r':(2,1),'m':(2,0),'s':(1,-.5),'N':(.5,2.5),'F':(-1,2.5),'O':(-1,0)}
old=[('B','u'),('u','D'),('D','E'),('E','v'),('v','C'),('C','B'),('B','A'),('A','r'),('r','m'),('m','s'),('s','C'),('A','N'),('N','F'),('N','O')]
for a,b in old:bond(ax,p[a],p[b],color='0.45')
for a,b in [('F','D'),('O','E')]:bond(ax,p[a],p[b],color='#12805c')
labels={'B':r'$C_B$','D':r'$C_D$','E':r'$C_E$','C':r'$C_C$','A':r'$C_A$','N':'N','F':r'$C_F$','O':'O'}
for k,t in labels.items():atom(ax,p[k],t)
wedge(ax,p['m'],(2.7,-.3),front=False);atom(ax,(3,-.4),'Me')
ax.text(.1,3.15,'E: saturated isoxazolidine connectivity',ha='center',fontsize=13)
ax.text(.3,-1.25,r'New bonds: $C_F-C_D$ and $O-C_E$ (green)',ha='center',color='#12805c')
ax.text(.3,-1.75,r'$C_F$ comes from formaldehyde; N-O survives until reduction',ha='center')
ax.text(.3,-2.2,'Schematic projection; retained carbon configurations as in D',ha='center',fontsize=10)
ax.set(xlim=(-3,3.5),ylim=(-2.5,3.5));fig.tight_layout();save(fig,'paper-3-isoxazolidine.png')
