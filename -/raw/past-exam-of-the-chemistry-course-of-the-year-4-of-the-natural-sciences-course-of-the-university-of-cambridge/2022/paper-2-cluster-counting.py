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
fig,axs=plt.subplots(1,3,figsize=(13,4.5),layout='constrained');a=axs[0]
for y,xs,filled,lab in [(0,[0],True,r'$a_1^2$ / 1S'),(1,[-.5,0,.5],True,r'$t_2^6$ / 1P'),(2.4,[-.65,-.32,0,.32,.65],False,'higher empty levels')]:
 for x in xs:
  a.plot([x-.12,x+.12],[y,y],c='black')
  if filled:a.text(x,y+.16,r'$\uparrow\downarrow$',ha='center',fontsize=10)
 a.text(-1.2,y,lab,ha='right',va='center',fontsize=10)
a.annotate('',(-2.5,2.8),(-2.5,-.4),arrowprops={'arrowstyle':'->'});finish(a,(-2.8,1),(-.6,3),r'Al$_4$Cp*$_4$: eight occupied core electrons')
a=axs[1];p=np.array([[0,1.3],[-1,0],[0,-.5],[1,0],[0,-1.3],[0,.5]])
for i in [0,4]:
 for j in [1,2,3,5]:bond(a,p[i],p[j],style='dashed' if j==5 else 'solid')
for i,j in [(1,2),(2,3),(3,5),(5,1)]:bond(a,p[i],p[j],style='dashed' if 5 in [i,j] else 'solid')
for i,xy in enumerate(p):atom(a,xy,'GeAr' if i in [0,4] else 'Sn',10)
a.text(0,-1.9,'2 × 3 + 4 × 2 = 14 skeletal e⁻',ha='center',fontsize=10);finish(a,(-1.6,1.6),(-2.2,2),r'Ge$_2$Sn$_4$Ar$_2$: closo octahedral core')
a=axs[2];v=np.array([[x,y,z] for z in [-1,1] for y in [-1,1] for x in [-1,1]]);M=np.array([[.8,.45,0],[-.2,.35,.8]]);q=v@M.T
for i in range(8):
 for j in range(i):
  if np.sum(v[i]!=v[j])==1:bond(a,q[i],q[j],color='0.6')
for xy in q:a.plot(*xy,'o',c='#245c9f',ms=6)
for axis in range(3):
 for sign in [-1,1]:
  face=np.zeros(3);face[axis]=sign*1.35;xy=M@face;atom(a,xy,'H' if axis==2 and sign==-1 else 'CEt',9,color='#b45309')
a.text(0,-2,'Blue vertices = AlMe; five carbon caps + H',ha='center',fontsize=8);finish(a,(-2,2),(-2.3,2),r'B: capped Al$_8$ cube; 32 skeletal e⁻')
save(fig,'paper-2-cluster-counting.png')
