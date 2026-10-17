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
fig,ax=plt.subplots(figsize=(10,3));ax.set_aspect('equal');ax.axis('off')
for shift,product in [(0,False),(5,True)]:
 A=np.array([shift,0.]);B=np.array([shift+1.5,0.]);M=np.array([shift+1.5,-1.]);bond(ax,A,B)
 for q,t in [(A,r'$C_A$'),(B,r'$C_B$'),(M,r'$C_M$')]:atom(ax,q,t)
 bond(ax,A,(shift,.9),order=1 if product else 2);atom(ax,(shift,1.2),'OH' if product else 'O')
 bond(ax,B,(shift+1.5,.9),order=2 if product else 1);atom(ax,(shift+1.5,1.2),'O' if product else 'OH')
 bond(ax,A if product else B,M,color='#b02b38')
ax.annotate('',xy=(4.5,.25),xytext=(2.4,.25),arrowprops={'arrowstyle':'->','lw':1.5});ax.text(3.4,.6,r'$H^+$',ha='center')
ax.text(3.4,-1.9,r'Migrating $\sigma(C_B-C_M)$ aligns with $\pi^*(C_A=O)$',ha='center')
ax.text(3.4,-2.4,'Other cage bonds retained; no net oxygen loss',ha='center')
ax.set(xlim=(-1,8),ylim=(-2.8,1.6));fig.tight_layout();save(fig,'paper-3-ketol.png')
