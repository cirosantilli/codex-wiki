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
from itertools import product
fig=plt.figure(figsize=(10,4.5))
for index in range(2):
 ax=fig.add_subplot(1,2,index+1,projection='3d')
 if index==0:
  fe=np.array([[0,0,1.1],[0,0,-1.1]])
  pd=np.array([[np.cos(x),np.sin(x),0] for x in np.linspace(0,2*np.pi,4)[:-1]])
  edges=[(f,p) for f in fe for p in pd];title=r'4: $\mathrm{Fe_2Pd_3}$, charge $+10$'
 else:
  fe=np.array(list(product([-1,1],repeat=3)))
  pd=np.array([[s if j==i else 0 for j in range(3)] for i in range(3) for s in [-1,1]])
  edges=[(f,p) for f in fe for p in pd if np.dot(f,p)==1];title=r'5: $\mathrm{Fe_8Pd_6}$, charge $+28$'
 for a,b in edges:ax.plot(*np.array([a,b]).T,color='0.45',lw=1.6)
 ax.scatter(*fe.T,s=110,c='#bd5c26',depthshade=False,label='Fe: three arms')
 ax.scatter(*pd.T,s=110,c='#198b99',depthshade=False,label='Pd: two or four links')
 ax.set_title(title,pad=0);ax.set_axis_off();ax.view_init(elev=18,azim=30);ax.set_box_aspect((1,1,1))
handles,labels=fig.axes[0].get_legend_handles_labels()
fig.legend(handles,labels,loc='lower center',ncol=2,frameon=False)
fig.text(.5,.97,'Connections represent pyridyl-bearing ligand arms',ha='center')
fig.subplots_adjust(bottom=.12,top=.84,wspace=.01);save(fig,'paper-3-cages.png')
