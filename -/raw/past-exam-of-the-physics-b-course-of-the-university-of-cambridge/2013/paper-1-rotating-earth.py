"""Original rotating-Earth force geometry and first-order projectile curves. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"axes.titlesize":10,"axes.labelsize":10})
from matplotlib.patches import Ellipse
fig,ax=plt.subplots(1,2,figsize=(9,3.8),layout='constrained');a=ax[0];a.add_patch(Ellipse((0,0),2,1.8,fc='#e8f3fa',ec='#3b6580'));a.axvline(0,color='.4',ls=':');a.axhline(0,color='.6',lw=.7);lam=np.pi/4;p=np.array([np.cos(lam),.9*np.sin(lam)]);up=np.array([np.cos(lam),np.sin(lam)]);north=np.array([-np.sin(lam),np.cos(lam)])
for v,label,col in [(np.array([.65,0]),'centrifugal','#c14537'),(-.55*up,'gravity','#345ba0'),(.5*up,'radial up','#008261')]:
 a.annotate('',xy=p+v,xytext=p,arrowprops=dict(arrowstyle='->',lw=2,color=col));a.text(*(p+1.15*v),label,fontsize=9,color=col,ha='center')
a.scatter(*p,s=35,c='k');a.text(0,1.05,'rotation axis',ha='center');a.text(0,-1.25,'Flattening exaggerated; force directions are local',ha='center',fontsize=8);a.set(xlim=(-1.25,1.65),ylim=(-1.4,1.35),aspect='equal',title='Force away from the rotation axis');a.axis('off')
t=np.linspace(0,2,300);z=2*t-t*t;x=-t*t+t**3/3;td=np.linspace(0,1,200);xd=td**3/3;zd=1-td*td;a=ax[1];a.plot(x,z,label='Launch and return');a.plot(xd,zd,label='Drop from same maximum height');a.scatter([0,-4/3,1/3],[0,0,0],c=['k','#3569ac','#e78e22']);a.axhline(0,color='.5',lw=.8);a.set(xlabel=r'East displacement / $(\Omega u^3\cos\lambda/g^2)$',ylabel=r'Height / $h_0$',title='Launch returns west; drop lands east');a.legend(fontsize=8);a.grid(alpha=.2)
fig.savefig('paper-1-rotating-earth.png',dpi=150,facecolor='white')
