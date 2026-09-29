"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(1,2,figsize=(9.5,4.8),layout='constrained')
theta=np.pi/2-np.arange(7)*2*np.pi/7;p=np.column_stack([1.1*np.cos(theta),1.1*np.sin(theta)])
for j,ax in enumerate(axs):
 ring(ax,p,{0:2} if j==0 else {})
 bond(ax,p[0],[0,2],1 if j==0 else 2);atom(ax,[0,2],r'O$^-$' if j==0 else 'O')
 me=p[2]+[.8,-.1];wedge(ax,p[2],me,True);atom(ax,me,'Me')
 ax.text(p[1,0]-.22,p[1,1]-.05,'2',fontsize=10,color=BLUE);ax.text(p[2,0]-.28,p[2,1]-.08,'3',fontsize=10,color=BLUE)
 if j==0:
  ax.annotate('electrophile approaches\nopposite the methyl face',p[1],(-1.25,-1.95),arrowprops={'arrowstyle':'->','color':ORANGE},fontsize=10,ha='center')
 else:
  r=p[1]+[.9,.35];wedge(ax,p[1],r,False);atom(ax,r,'R',13)
  ax.text(-.1,-1.9,r'R = CH(OH)CH$_2$K',ha='center',fontsize=11);ax.text(-.1,-2.3,'K = methyl-substituted cyclic ketal',ha='center',fontsize=9)
 finish(ax,(-2.3,2.6),(-2.65,2.65),'Copper enolate after methyl addition' if j==0 else 'Aldol product: starred centers trans')
save(fig,Path(__file__).with_suffix('.png').name)
