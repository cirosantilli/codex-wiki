"""Original numbered Robinson-annulation graphs and arrows; output to cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
from tools.chemistry_diagram import *
fig,axs=plt.subplots(1,3,figsize=(13,4.7),layout='constrained',facecolor='white')
for ax,stage,title in zip(axs,[0,1,2],['Terminal enolate closes onto C1','Six-membered aldol intermediate','B: fused conjugated enone']):
 r=[(0,1),(.866,.5),(.866,-.5),(0,-1),(-.866,-.5),(-.866,.5)];ring(ax,r)
 chain=[r[5],(-1.7,1),(-2.6,.5),(-2.6,1.6),(-1.7,2.1)]
 for a,b in zip(chain,chain[1:]):bond(ax,a,b)
 bond(ax,chain[3],(-3.45,1.6),2);atom(ax,(-3.45,1.6),'O');bond(ax,r[1],(1.7,1));atom(ax,(1.7,1),'Me')
 for point,label in [(r[0],'C1'),(r[5],'C6'),(chain[1],'a'),(chain[2],'b'),(chain[3],'c'),(chain[4],'d')]:ax.text(point[0]+.08,point[1]-.18,label,fontsize=10,color=BLUE)
 if stage<2:bond(ax,r[0],(0,2),2 if stage==0 else 1);atom(ax,(0,2),'O' if stage==0 else 'OH')
 if stage==0:
  atom(ax,(-1.7,2.55),'−',color=ORANGE);curly(ax,(-1.6,2.2),(-.05,1.15),-.15);curly(ax,(.05,1.5),(.05,2.0),-.6)
 else:bond(ax,chain[4],r[0],2 if stage==2 else 1,color=BLUE)
 if stage==1:ax.text(-2.8,-1.8,'Base / heat: E1cb dehydration',fontsize=10);curly(ax,(-1.6,2.2),(-.65,1.55),-.3);curly(ax,(0,1.5),(.05,2.0),-.6)
 finish(ax,(-3.95,2.15),(-2.05,2.95),title)
fig.suptitle('The original ring methyl is retained; the side-chain methyl supplies the new enone α carbon.',fontsize=12)
save(fig,'paper-1-annulation.png')
