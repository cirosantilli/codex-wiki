"""Original connectivity diagrams, not crystallographic geometries; output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,3,figsize=(14,4.7),facecolor='white')
for a in axs:a.set(xlim=(-2.7,2.7),ylim=(-2.6,2.7),aspect='equal');a.axis('off')
def label(a,p,s,fs=12,col='black'):a.text(*p,s,ha='center',va='center',fontsize=fs,color=col,bbox=dict(fc='white',ec='none',pad=1))
def line(a,p,q,**kw):a.plot([p[0],q[0]],[p[1],q[1]],color=kw.pop('color','#333333'),lw=1.3,**kw)
a=axs[0];a.set_title('Co–Co single bond; 18 e at each Co',fontsize=12,weight='bold')
for x in [-.9,.9]:
 p=np.array([x,0]);label(a,p,'Co',14)
 for ang in ([80,145,215,280] if x<0 else [35,100,260,325]):
  q=p+1.3*np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))]);line(a,p,q);label(a,q,'PF₃',10)
line(a,(-.65,0),(.65,0));label(a,(0,-2.05),'Four terminal P donors per cobalt',10)
a=axs[1];a.set_title('Ti–Ti single bond; 18 e at each Ti',fontsize=12,weight='bold')
line(a,(-.75,0),(.75,0))
for x in [-.85,.85]:
 p=np.array([x,0]);label(a,p,'Ti',14)
 for ang in ([95,160,220,280] if x<0 else [80,20,-40,-95]):
  q=p+1.25*np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))]);line(a,p,q);label(a,q,'CO',10)
 q=p+np.array([0,1.85]);line(a,p,q,ls='--');label(a,q,'η⁵-Cp',11)
label(a,(0,-2.05),'Four terminal CO + one Cp per titanium',10)
a=axs[2];a.set_title('Three Ti–Ti edges; 14 e at each Ti',fontsize=12,weight='bold')
ps=[np.array([0,1.05]),np.array([-1.05,-.8]),np.array([1.05,-.8])]
for i in range(3):
 p,q=ps[i],ps[(i+1)%3]
 a.plot([p[0],q[0]],[p[1],q[1]],color='#333333',lw=2.3)
 mid=(p+q)/2;v=mid/np.linalg.norm(mid)*.58;r=mid+v
 line(a,p,r,color='#9b6039',ls='--');line(a,q,r,color='#9b6039',ls='--');label(a,r,'μ-Cl',10,'#9b6039')
for i,p in enumerate(ps):
 v=p/np.linalg.norm(p);q=p+v*.75;line(a,p,q);label(a,q,'Cl',10)
 label(a,p,'Ti',13)
 # Compact P,P-chelate annotation: one chelate per metal, separate from bridges.
 t=p+np.array([.8, .2]) if i==0 else p+np.array([0,-.85])
 label(a,t,'κ²-dmpe',9,'#2268a0');line(a,p,t,color='#2268a0')
label(a,(0,-2.3),'Solid edges: Ti–Ti; dashed paths: Ti–Cl–Ti',9)
fig.tight_layout();fig.savefig('paper-2-clusters.png',dpi=170,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)
