"""Original explanatory figure. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run through the root Makefile; the PNG basename is written to the current directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(12,7),layout='constrained')
def five(a,center=(0,0),scale=1):
 t=np.pi/2+np.arange(5)*2*np.pi/5;return np.asarray(center)+scale*np.column_stack([np.cos(t),np.sin(t)])
a=axs[0,0];p=five(a);ring(a,p,{1:2,3:2})
# cyclic order S1 C2 N3 C4 C5
for i,l in [(0,'S'),(2,'N')]:atom(a,p[i],l)
for i,l in [(1,'3-F-phenyl'),(3,'OTf'),(4,r'CO$_2$Et')]:
 d=p[i]*.7;bond(a,p[i],p[i]+d);atom(a,p[i]+1.45*d,l,10)
finish(a,(-2.8,2.8),(-2.4,2.3),'D: 4-triflate, 5-ester thiazole')
a=axs[0,1];p=five(a);ring(a,p,{1:2,3:2})
for i,l in [(0,'NH'),(1,'N'),(2,'N')]:atom(a,p[i],l)
for i,l in [(3,'thiazol-4-yl'),(4,r'(CH$_2$)$_3$CO$_2$Et')]:d=p[i]*.7;bond(a,p[i],p[i]+d);atom(a,p[i]+1.45*d,l,10)
finish(a,(-3.1,3.5),(-2.3,2.3),'F: NH triazole; thiazole ester retained')
a=axs[1,0];p=np.array([[-1,0],[-1.4,1],[-.55,1.7],[.45,1.1],[.2,0]]);ring(a,p,{1:2,3:2});atom(a,p[0],'S');atom(a,p[2],'N');bond(a,p[1],[-2.1,1.1]);atom(a,[-2.6,1.1],'Ar')
r=np.array([p[3],[1.5,1.7],[2.35,1],[2.1,0],[1.1,-.5],p[4]]);ring(a,r,{1:2,5:2});atom(a,r[3],'NH');bond(a,r[4],[1.15,-1.2],2);atom(a,[1.15,-1.4],'O');bond(a,r[2],[3.0,1.5]);atom(a,[3.2,1.8],r'(CH$_2$)$_3$CO$_2$H',10)
finish(a,(-3.1,3.7),(-1.7,3.1),'H: fused pyridone (ring O → NH)')
a=axs[1,1];p=five(a);ring(a,p,{1:2,3:2});atom(a,p[0],'NH');bond(a,p[1],p[1]*1.7);atom(a,p[1]*2.05,r'CO$_2$Et',10);bond(a,p[3],p[3]*1.7);atom(a,p[3]*2.1,'C(O)-p-tolyl',10);finish(a,(-2.8,2.8),(-2.5,2.2),'K: C4 acylation of the C2 ester pyrrole')
save(fig,'paper-2-heterocyclic-products.png')
