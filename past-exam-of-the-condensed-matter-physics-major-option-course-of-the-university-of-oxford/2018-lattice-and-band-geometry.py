"""Original lattice, band and neutron geometry; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(11,8.2),layout='constrained',facecolor='white')
a1=np.array([np.sqrt(3)/2,.5]);a2=np.array([np.sqrt(3)/2,-.5]);db=np.array([-1/(2*np.sqrt(3)),0]);dn=-db
ax=axs[0,0]
for m in range(-2,3):
 for n in range(-2,3):
  R=m*a1+n*a2
  for pos,color in [(R+db,'#355a9b'),(R+dn,'#bd7820')]:
   if abs(pos[0])<1.5 and abs(pos[1])<1.3:ax.scatter(*pos,color=color,s=38,zorder=3)
for j,v in enumerate([dn-db,dn-db-a1,dn-db-a2],1):
 ax.annotate('',db+v,db,arrowprops={'arrowstyle':'->','color':'#269572','lw':2})
 ax.text(*(db+.7*v+np.array([.02,.06])),f'n{j}',color='#147455')
for v,label in [(a1,'a₁'),(a2,'a₂')]:
 ax.annotate('',db+v,db,arrowprops={'arrowstyle':'->','color':'#555','linestyle':'--'})
 ax.text(*(db+1.08*v),label)
ax.set(xlim=(-1.55,1.55),ylim=(-1.35,1.35),aspect='equal',xlabel='x / a',ylabel='y / a',title='A  Two-site honeycomb; blue B, ochre N')
ax=axs[0,1]
verts=np.array([[0,4*np.pi/3],[2*np.pi/np.sqrt(3),2*np.pi/3],[2*np.pi/np.sqrt(3),-2*np.pi/3],[0,-4*np.pi/3],[-2*np.pi/np.sqrt(3),-2*np.pi/3],[-2*np.pi/np.sqrt(3),2*np.pi/3]])
ax.add_patch(Polygon(verts,facecolor='#e7eff9',edgecolor='#355a9b',lw=2))
for v,label in [(np.array([2*np.pi/np.sqrt(3),2*np.pi]),'b₁'),(np.array([2*np.pi/np.sqrt(3),-2*np.pi]),'b₂')]:
 ax.annotate('',v,(0,0),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#555'})
 ax.text(*(v+np.array([.15,0])),label)
ax.scatter([0,0],[0,4*np.pi/3],color='#bd7820',zorder=4);ax.text(.2,0,'Γ');ax.text(.2,4*np.pi/3,'K')
ax.set(xlim=(-5,5),ylim=(-7,7),aspect='equal',xlabel='a kₓ',ylabel='a kᵧ',title='B  First Brillouin zone and reciprocal basis')
ax=axs[1,0];q=np.linspace(-.8,.8,400)
for delta,color,label in [(0,'#355a9b','equivalent sites'),(.5,'#bd7820','inequivalent sites')]:
 E=np.sqrt(delta**2+.75*q*q);ax.plot(q,E,color=color,label=label,lw=2);ax.plot(q,-E,color=color,lw=2)
ax.annotate('',(0,.5),(0,-.5),arrowprops={'arrowstyle':'<->','color':'#777'});ax.text(.04,0,'gap 2Δ')
ax.set(xlabel='a q near K',ylabel='energy relative to band midpoint',title='C  Normalized valley models');ax.legend(frameon=False,fontsize=9)
ax=axs[1,1];ki=3.8049825318;kf=2.196807689;phi=np.deg2rad(-46.50948104);pf=kf*np.array([np.cos(phi),np.sin(phi)]);pi=np.array([ki,0])
for start,end,color,label in [(np.zeros(2),pi,'#355a9b','kᵢ'),(np.zeros(2),pf,'#bd7820',r'$k_f$'),(pf,pi,'#269572','Q = kᵢ − kf')]:
 ax.annotate('',end,start,arrowprops={'arrowstyle':'->','lw':2.3,'color':color});mid=(start+end)/2;ax.text(*(mid+np.array([.05,.12])),label,color=color)
omega=np.deg2rad(-55.19936864)
for ang,label in [(omega,'+a'),(omega+np.pi/2,'+c')]:
 end=1.25*np.array([np.cos(ang),np.sin(ang)]);ax.annotate('',end,(0,0),arrowprops={'arrowstyle':'->','color':'#777','linestyle':'--'});ax.text(*end,label,color='#555')
ax.text(0,-2.3,'φ = −46.51°; ω = −55.20°',fontsize=10)
ax.set(xlim=(-.4,4.3),ylim=(-2.6,1.1),aspect='equal',xlabel='wavevector component (Å⁻¹)',title='D  Positive l = 2; +c initially 90° from +a')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
