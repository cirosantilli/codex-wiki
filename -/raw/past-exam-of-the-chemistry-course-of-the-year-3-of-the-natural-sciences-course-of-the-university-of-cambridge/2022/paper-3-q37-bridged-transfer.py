"""Original explanatory chemistry drawing; Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save
BLUE='#245c9f'
def label(ax,p,text,size=10):
    ax.text(*p,text,ha='center',va='center',fontsize=size,color=BLUE)

fig,axes=plt.subplots(3,1,figsize=(9,6.2),layout='constrained')
rows=[('Remote N attack on Co–SCN',['Coᴵᴵᴵ','S','C','N','Crᴵᴵ'],'N-bound Crᴵᴵᴵ product'),('Adjacent S attack on Co–SCN',['Coᴵᴵᴵ','S(CN)','Crᴵᴵ'],'S-bound Crᴵᴵᴵ product'),('Remote S attack on Co–NCS',['Coᴵᴵᴵ','N','C','S','Crᴵᴵ'],'S-bound Crᴵᴵᴵ product')]
for ax,(title,labels,product) in zip(axes,rows):
    for i,t in enumerate(labels):
        atom(ax,(i*1.4,0),t,size=13)
        if i:bond(ax,((i-1)*1.4+.3,0),(i*1.4-.3,0))
    ax.text(3,-.65,'Bridge formation → electron transfer → Co-side cleavage',ha='center',fontsize=10)
    ax.text(3,-1.12,product+'; Coᴵᴵ becomes hexaaqua',ha='center',fontsize=10,color=BLUE)
    finish(ax,(-.65,7),(-1.45,.65),title)

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
