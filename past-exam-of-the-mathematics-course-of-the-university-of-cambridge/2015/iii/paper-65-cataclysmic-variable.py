"""Generate an original schematic; write the PNG basename in the current directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
MPLCONFIGDIR supplied by the caller is respected.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.paper-65-mplconfig'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,FancyArrowPatch
Q=.4
OM=np.sqrt(1+Q)
XC=Q/(1+Q)
def potential(x,y):
 return -1/np.hypot(x,y)-Q/np.hypot(x-1,y)-.5*(1+Q)*((x-XC)**2+y*y)
def gradient(x,y):
 r=np.hypot(x,y);s=np.hypot(x-1,y)
 return np.array([x/r**3+Q*(x-1)/s**3-(1+Q)*(x-XC),y/r**3+Q*y/s**3-(1+Q)*y])
def l1():
 lo,hi=.001,.999
 for _ in range(80):
  mid=(lo+hi)/2
  if gradient(mid,0)[0]>0:lo=mid
  else:hi=mid
 return (lo+hi)/2
def donor_boundary():
 point=l1();crit=potential(point,0);points=[]
 for theta in np.linspace(-np.pi,np.pi,1001):
  d=np.array([np.cos(theta),np.sin(theta)])
  if abs(abs(theta)-np.pi)<1e-8:r=1-point
  else:
   radii=np.linspace(.001,.7,1000);vals=potential(1+radii*d[0],radii*d[1])-crit
   indices=np.flatnonzero(vals>=0)
   if not len(indices):raise RuntimeError('No first equipotential crossing')
   hi=radii[indices[0]];lo=hi-.7/999
   for _ in range(45):
    mid=(lo+hi)/2
    if potential(1+mid*d[0],mid*d[1])<crit:lo=mid
    else:hi=mid
   r=(lo+hi)/2
  points.append([1+r*d[0],r*d[1]])
 return np.array(points)
def rhs(s):
 x,y,vx,vy=s;gx,gy=gradient(x,y)
 return np.array([vx,vy,-gx+2*OM*vy,-gy-2*OM*vx])
def stream():
 s=np.array([l1()-.002,0.,-.006,0.]);points=[s.copy()];dt=.0008
 for _ in range(20000):
  k1=rhs(s);k2=rhs(s+dt*k1/2);k3=rhs(s+dt*k2/2);k4=rhs(s+dt*k3)
  s=s+dt*(k1+2*k2+2*k3+k4)/6;points.append(s.copy())
  if np.hypot(*s[:2])<=.28:break
 else:raise RuntimeError('Stream did not reach disk')
 return np.array(points)
def main():
 fig,ax=plt.subplots(figsize=(12,7),dpi=100,facecolor='white')
 ax.set_facecolor('white');ax.set_aspect('equal');ax.set_xlim(-.55,1.6);ax.set_ylim(-.58,.62);ax.axis('off')
 ax.add_patch(Polygon(donor_boundary(),closed=True,fc='#efb979',ec='#985f2d',lw=2))
 ax.add_patch(Circle((0,0),.28,fc='#b7def3',ec='#337ba5',lw=2))
 for r in [.075,.12,.17,.22]:ax.add_patch(Circle((0,0),r,fill=False,ec='white',lw=1))
 ax.add_patch(Circle((0,0),.037,fc='#f8af48',ec='#e07d00',lw=1.2))
 ax.add_patch(Circle((0,0),.022,fc='white',ec='#2a465b',lw=1.5))
 s=stream();ax.plot(s[:,0],s[:,1],c='#15694f',lw=3,zorder=5)
 end=s[-1,:2];ax.plot(*end,'o',color='#df423b',ms=10,zorder=7)
 pt=l1();ax.plot(pt,0,'ko',ms=4,zorder=7)
 def label(text,xy,pos,color='#183747'):
  ax.annotate(text,xy=xy,xytext=pos,ha='center',va='center',fontsize=11,color=color,arrowprops={'arrowstyle':'-','color':color,'lw':1.2},zorder=10)
 label('Cool donor fills its Roche lobe',(1,.19),(1.03,.48))
 ax.text(1,-.04,'Donor star',ha='center',va='center',fontsize=13,color='#5d3512')
 label(r'Inner Lagrange point $L_1$',(pt,0),(.65,-.3))
 label('Ballistic gas stream',s[len(s)//2,:2],(.53,.37))
 label('Stream-impact hot spot',end,(-.03,.48))
 label('White dwarf\n(radius enlarged)',(0,0),(-.34,-.34))
 label('Boundary layer',(.033,0),(.06,-.48))
 label('Accretion disk',(-.19,.13),(-.36,.26))
 ax.add_patch(FancyArrowPatch((.05,.205),(.02,.11),arrowstyle='->',mutation_scale=15,color='#28617c',lw=2))
 ax.text(-.10,.195,'Gas inward',fontsize=9,color='#28617c',ha='center')
 ax.add_patch(FancyArrowPatch((-.08,-.1),(-.15,-.24),arrowstyle='->',mutation_scale=15,color='#28617c',lw=2))
 ax.text(-.17,-.11,'Angular momentum\noutward',fontsize=9,color='#28617c',ha='center')
 ax.text(.52,.61,'A nonmagnetic cataclysmic variable',ha='center',va='center',fontsize=17,weight='bold')
 ax.text(.52,-.58,'Orbital-plane schematic: weak white-dwarf magnetic field; sizes of inner regions exaggerated.',ha='center',va='center',fontsize=10,color='#456')
 fig.subplots_adjust(left=.03,right=.98,bottom=.04,top=.96)
 fig.savefig(Path.cwd()/'paper-65-cataclysmic-variable.png',dpi=100,facecolor='white',transparent=False)
 plt.close(fig)
if __name__=='__main__':main()
