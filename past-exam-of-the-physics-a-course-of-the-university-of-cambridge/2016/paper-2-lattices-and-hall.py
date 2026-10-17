"""Original derivation schematics; Python3.14, numpy/matplotlib; PNG to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10})
fig,axs=plt.subplots(2,2,figsize=(12,9),layout='constrained')
ax=axs[0,0];ax.add_patch(Rectangle((0,0),5,2,facecolor='#dae7f2',edgecolor='black'))
for x in np.linspace(.4,4.6,8):ax.text(x,1.85,'+',ha='center');ax.text(x,.05,'−',ha='center')
ax.annotate('current +x',xy=(4,1.2),xytext=(1,1.2),arrowprops={'arrowstyle':'->'})
ax.annotate('electrons',xy=(1,.7),xytext=(3.2,.7),arrowprops={'arrowstyle':'->'})
ax.annotate('Eᵧ',xy=(4.5,.4),xytext=(4.5,1.5),arrowprops={'arrowstyle':'->'})
ax.text(2.4,2.2,'Vᵧ =φ(top)−φ(bottom)>0',ha='center')
ax.text(2.5,-.45,'Vₓ =φ(left)−φ(right)>0',ha='center')
ax.text(5.3,1,'⊙ Bz>0',ha='left')
ax.set(xlim=(-.4,6.6),ylim=(-1,2.8),aspect='equal',title='A  Signed electron charge; explicit probe polarities');ax.axis('off')
ax=axs[0,1];O=np.array([0.,0.]);P=np.array([.9,.7]);D=np.array([4.,2.3])
for v,label in [(O,'O'),(P,'P')]:
 ax.plot(*v,'ko');ax.text(*(v+[-.15,-.15]),label)
 ax.annotate('',xy=v,xytext=v+[-1.1,0],arrowprops={'arrowstyle':'->','color':'tab:blue'})
 ax.plot([v[0],D[0]],[v[1],D[1]],color='tab:orange')
ax.annotate('',xy=P,xytext=O,arrowprops={'arrowstyle':'->','color':'black'})
ax.text(.2,.5,'rₙ');ax.text(-.6,.85,'kᵢ',color='tab:blue');ax.text(2.1,1.6,r'$k_f$',color='tab:orange')
ax.plot(*D,'ks');ax.text(*(D+[.1,0]),'far detector')
ax.text(-.8,-.6,'relative phase =(kᵢ−kf)·rₙ')
ax.set(xlim=(-1.4,5.5),ylim=(-1,3.2),aspect='equal',title='B  Incident and outgoing path-phase changes');ax.axis('off')
a=np.array([1.,0]);b=np.array([.5,np.sqrt(3)/2])
A=np.array([1.,-1/np.sqrt(3)]);B=np.array([0.,2/np.sqrt(3)])
for ax,v,w,title,xlabel in [(axs[1,0],a,b,'C  Direct triangular lattice','x/a'),(axs[1,1],A,B,'D  Reciprocal triangular lattice','Gₓ/(2π/a)')]:
 pts=np.array([i*v+j*w for i in range(-3,4) for j in range(-3,4)])
 ax.scatter(pts[:,0],pts[:,1],s=12,color='gray')
 ax.add_patch(Polygon([np.zeros(2),v,v+w,w],facecolor='#d1e9ff',edgecolor='black',alpha=.7))
 for vec,lab in [(v,'a' if title.startswith('C') else 'A'),(w,'b' if title.startswith('C') else 'B')]:
  ax.annotate('',xy=vec,xytext=(0,0),arrowprops={'arrowstyle':'->','color':'tab:red'})
  ax.text(*(vec+[.1,.1]),lab,color='tab:red')
 ax.set(xlim=(-2.7,2.7),ylim=(-2.7,2.7),aspect='equal',title=title,xlabel=xlabel,ylabel='y/a' if title.startswith('C') else 'Gᵧ/(2π/a)')
 if title.startswith('D'):
  ax.add_patch(Circle((0,0),2/np.sqrt(3),fill=False,color='tab:blue',ls=':'))
  ax.text(-2.5,-2.4,'first nonzero shell |G|=4π/(√3a)',fontsize=9)
fig.savefig('paper-2-lattices-and-hall.png',dpi=155,facecolor='white')

