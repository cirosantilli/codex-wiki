"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(1,2,figsize=(10,4.9),layout='constrained')
ax=axs[0];p=[[-1,1],[-1,0],[0,-.45],[1,0],[.8,1]]
ring(ax,p,{2:2});atom(ax,p[0],'O');atom(ax,p[4],'Al',13,color=BLUE)
bond(ax,p[2],[0,-1.45]);atom(ax,[0,-1.45],'H',13,color=ORANGE)
bond(ax,p[3],[1.9,-.6]);atom(ax,[1.9,-.6],r'CH$_2$R′',11)
ax.text(.1,1.75,'Other Al ligands and counterion omitted',ha='center',fontsize=9)
ax.text(0,-2.05,'Al and the newly delivered H are trans',ha='center',fontsize=10)
finish(ax,(-2.15,2.55),(-2.45,2.4),'O-directed vinylaluminate')
ax=axs[1];a=np.array([-.6,0]);b=np.array([.6,0]);bond(ax,a,b,2)
for v,end,label in [(a,[-1.35,1],r'CH$_2$OH'),(a,[-1.35,-1],'H'),(b,[1.35,1],'I'),(b,[1.35,-1],r'CH$_2$R′')]:
 bond(ax,v,end);atom(ax,end,label,12,color=ORANGE if label=='I' else '.15')
ax.plot([-1.75,1.7],[1.45,1.45],':',color=BLUE)
ax.text(0,1.85,'Higher-priority groups on the same side',ha='center',fontsize=10,color=BLUE)
ax.text(0,-2.05,'C–Al → C–I retains alkene geometry',ha='center',fontsize=10)
finish(ax,(-2.4,2.4),(-2.45,2.4),'Iodination and work-up: Z vinyl iodide')
save(fig,Path(__file__).with_suffix('.png').name)
