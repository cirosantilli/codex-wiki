"""Original solution diagram; Python 3.14, numpy and matplotlib.
The PNG output basename is relative to the current working directory.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, wedge, atom, ring, curly, flow, finish, save, BLUE, ORANGE, GREEN
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(14,4.5),gridspec_kw={'width_ratios':[1.2,1,1.1]})
a,b,c=axes
mid=np.array([[0,1],[.866,.5],[.866,-.5],[0,-1],[-.866,-.5],[-.866,.5]])
left=np.array([mid[5],[-1.732,1],[-2.598,.5],[-2.598,-.5],[-1.732,-1],mid[4]])
right=np.array([mid[1],[1.732,1],[2.598,.5],[2.598,-.5],[1.732,-1],mid[2]])
ring(a,mid);ring(a,left,{0:2,2:2,4:2});ring(a,right,{0:2,2:2,4:2});atom(a,mid[3],'O');bond(a,mid[0],(0,1.8),2);atom(a,(0,1.8),'O')
for i,label,q in [(1,'Br',(1.73,1.9)),(2,'OH',(3.45,.9)),(3,'Br',(3.45,-.9))]:
 bond(a,right[i],q);atom(a,q,label,color=ORANGE if label=='Br' else '0.15');a.text(right[i][0]-.24,right[i][1]+.05,str(i),color=BLUE,fontsize=9)
finish(a,(-3.1,3.95),(-2.1,2.3),'B1(a): 1,3-dibromo-2-hydroxyxanthone')
bond(b,(-.4,0),(.65,0),2);atom(b,(-.4,0),'C');atom(b,(.65,0),'CH₂');bond(b,(-.4,0),(-1.2,-.7));atom(b,(-1.2,-.7),'tBu');bond(b,(-.4,0),(-.4,.95));atom(b,(-.4,.95),'O⁻');atom(b,(.85,.95),'Na⁺');b.text(0,-1.5,'the two =CH₂ hydrogens are not equivalent',ha='center',fontsize=9);finish(b,(-2,2),(-2,2),'B1(b): sodium enolate D')
pts=[(-1.2,0),(0,-.55),(1.2,0)];bond(c,pts[0],pts[1],2);bond(c,pts[1],pts[2]);bond(c,pts[0],(-1.2,1));atom(c,(-1.2,1),'O');bond(c,(-1.2,1),(-.4,1.15));atom(c,(-.4,1.15),'H');bond(c,pts[2],(1.2,1),2);atom(c,(1.2,1),'O');bond(c,(-.3,1.15),(1.05,1.03),style='dotted',color=BLUE);bond(c,pts[0],(-1.85,-.55));atom(c,(-1.85,-.55),'tBu');bond(c,pts[2],(1.85,-.55));atom(c,(1.85,-.55),'tBu');atom(c,pts[1],'CH');c.text(0,-1.5,'degenerate proton transfer averages the two ends',ha='center',fontsize=9);finish(c,(-2.5,2.5),(-2,2),'B1(b): internally hydrogen-bonded enol E')
fig.tight_layout();fig.savefig('paper-1-products.png',dpi=140,facecolor='white',bbox_inches='tight',pad_inches=.18);plt.close(fig)
