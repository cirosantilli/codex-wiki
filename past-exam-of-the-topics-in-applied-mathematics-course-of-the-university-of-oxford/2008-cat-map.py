"""Original polygon cut-and-translate construction. Python3.14.4; root pyproject dependencies. Output:CWD."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
A=np.array([[2,1],[1,1]]);square=np.array([[0,0],[1,0],[1,1],[0,1]],float);para=square@A.T
# Sutherland--Hodgman clipping against an axis-aligned integer cell.
def clip(poly,axis,value,keep_greater):
 if not len(poly):return poly
 out=[]
 for p,q in zip(poly,np.roll(poly,-1,axis=0)):
  inside_p=(p[axis]>=value-1e-12) if keep_greater else (p[axis]<=value+1e-12)
  inside_q=(q[axis]>=value-1e-12) if keep_greater else (q[axis]<=value+1e-12)
  if inside_p:out.append(p)
  if inside_p!=inside_q:out.append(p+(q-p)*(value-p[axis])/(q[axis]-p[axis]))
 return np.array(out)
def area(v):return abs(np.dot(v[:,0],np.roll(v[:,1],-1))-np.dot(v[:,1],np.roll(v[:,0],-1)))/2 if len(v)>2 else 0
pieces=[]
for j in range(3):
 for k in range(2):
  p=para.copy()
  for axis,val,gt in [(0,j,True),(0,j+1,False),(1,k,True),(1,k+1,False)]:p=clip(p,axis,val,gt)
  if area(p)>1e-10:pieces.append((j,k,p))
assert abs(sum(area(p) for j,k,p in pieces)-1)<1e-10
fig,axes=plt.subplots(1,3,figsize=(10,3.7),layout='constrained',facecolor='white')
colors=['#7bb2d4','#edaf75','#93bf91','#c69bcc','#e7d77b','#70c3b8']
for number,(j,k,p) in enumerate(pieces):
 color=colors[number];src=p@np.linalg.inv(A).T;dst=p-[j,k]
 for ax,v in zip(axes,[src,p,dst]):
  ax.add_patch(Polygon(v,facecolor=color,edgecolor='white',lw=1));center=v.mean(axis=0);ax.text(*center,str(number+1),ha='center',va='center',fontsize=10)
axes[1].plot(*np.vstack([para,para[0]]).T,color='black',lw=1)
for ax,title in zip(axes,['Before the linear map','Cut at the integer grid','Translate each piece modulo 1']):
 ax.set_title(title,fontsize=11);ax.set_aspect('equal');ax.set_xlabel('x');ax.set_ylabel('y');ax.grid(alpha=.25)
for ax in [axes[0],axes[2]]:ax.set(xlim=(-.03,1.03),ylim=(-.03,1.03),xticks=[0,1],yticks=[0,1])
axes[1].set(xlim=(-.05,3.05),ylim=(-.05,2.05),xticks=range(4),yticks=range(3))
fig.savefig('2008-cat-map.png',dpi=160,facecolor='white')
