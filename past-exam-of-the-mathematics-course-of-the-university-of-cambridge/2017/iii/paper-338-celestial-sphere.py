# Original exam-solution diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
# Run beside the eventual paper with its working directory set to the mirrored _media directory.
import os
import tempfile
from pathlib import Path
# A caller may reuse its fresh publication namespace; standalone runs create one.
_cache_root = Path(os.environ['PAPER_338_PUBLICATION_CACHE']) if os.environ.get('PAPER_338_PUBLICATION_CACHE') else Path(tempfile.mkdtemp(prefix='2017-iii-paper-338-publication-', dir='/tmp'))
os.environ['MPLCONFIGDIR'] = str(_cache_root / 'mpl-cache')
os.environ['XDG_CACHE_HOME'] = str(_cache_root / 'xdg-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white','savefig.transparent':False})

fig=plt.figure(figsize=(11,6.5),dpi=100)
ax=fig.add_axes([.01,.01,.72,.92],projection='3d');ax.set_box_aspect((1,1,1));ax.set_axis_off();ax.view_init(elev=20,azim=135)
theta,delta,h=np.deg2rad([35,20,45]);n=np.array([1.,0,0]);w=np.array([0.,1,0]);z=np.array([0.,0,1]);p=np.cos(theta)*n+np.sin(theta)*z;e=-np.sin(theta)*n+np.cos(theta)*z
q=np.cos(h)*e+np.sin(h)*w;x=np.sin(delta)*p+np.cos(delta)*q
H=x.copy();H[2]=0;H/=np.linalg.norm(H);eta=np.arctan2(x[1],x[0]);gamma=np.arcsin(x[2])
def line(v,**kw):ax.plot(*v.T,**kw)
def circle(a,b,color,ls='-'):
 t=np.linspace(0,2*np.pi,401);line(np.cos(t)[:,None]*a+np.sin(t)[:,None]*b,color=color,lw=1.3,ls=ls)
def arc(a,b,angle,col,label):
 t=np.linspace(0,angle,100);v=np.cos(t)[:,None]*a+np.sin(t)[:,None]*b;line(v,color=col,lw=3);v0=v[len(v)//2]*1.09;ax.text(*v0,label,color=col,fontsize=15)
circle(n,w,'#777777');circle(e,w,'#1976b9');circle(n,z,'#999999','--');circle(p,q,'#bd9270','--');circle(H,z,'#bbbbbb','--')
arc(n,z,theta,'#a73ab0',r'$\theta$');arc(n,w,eta,'#c86b00',r'$\eta$');arc(H,z,gamma,'#dd3333',r'$\gamma$');arc(e,w,h,'#1b916c',r'$h$');arc(q,p,delta,'#1643c6',r'$\delta$')
for v,t,col in [(n,'North','#444444'),(w,'West','#444444'),(z,'Z: zenith','#222222'),(p,'P: north pole','#a73ab0'),(x,'X: star','#dd3333'),(H,'H','#c86b00'),(q,'Q','#1643c6'),(e,'Meridian / equator','#1976b9')]:
 ax.scatter(*v,color=col,s=25)
 if t not in ['H','Q']:ax.text(*(v*1.1),t,color=col,fontsize=10)
for v in [p,z,x]:line(np.array([[0.,0,0],v]),color='#cccccc',lw=.8)
ax.text(0,0,0,'O',color='#555555');ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),zlim=(-1.3,1.3))
fig.text(.74,.86,'Reference circles',weight='bold',fontsize=13)
labels=[('Horizon','#777777'),('Celestial equator','#1976b9'),('Meridian / hour circle','#999999')]
for i,(t,c) in enumerate(labels):fig.text(.74,.81-i*.045,t,color=c)
fig.text(.74,.60,'Angle conventions',weight='bold',fontsize=13)
for i,(t,c) in enumerate([(r'$\theta$: north to pole','#a73ab0'),(r'$\eta$: north toward west','#c86b00'),(r'$\gamma$: H to X','#dd3333'),(r'$h$: meridian to Q','#1b916c'),(r'$\delta$: Q to X','#1643c6')]):fig.text(.74,.55-i*.05,t,color=c)
fig.text(.287,.49,r'$\gamma$',color='#dd3333',fontsize=15)
fig.text(.283,.397,'H',color='#c86b00',fontsize=11)
fig.text(.353,.55,'Q',color='#1643c6',fontsize=11)
fig.text(.74,.20,'Example only:\nlatitude 35°, declination 20°\nhour angle 45° west\nStar above the horizon',linespacing=1.7,fontsize=10)
fig.suptitle('Celestial sphere: horizon and equatorial coordinates',fontsize=14)
fig.savefig('paper-338-celestial-sphere.png',dpi=100);plt.close(fig)
