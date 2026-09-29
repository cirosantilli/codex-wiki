"""Sketch one invariant spherical octant via squared-coordinate barycentrics.
Output basename to caller CWD; Python 3.14, root numpy/matplotlib dependencies.
Does not override caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
n=580
s=np.linspace(0,1,n);t=np.linspace(0,np.sqrt(3)/2,n);S,T=np.meshgrid(s,t)
Z=2*T/np.sqrt(3);W=S-Z/2;U=1-W-Z
prod=np.ma.masked_where((U<0)|(W<0)|(Z<0),U*W*Z)
fig,ax=plt.subplots(figsize=(7,6.1),facecolor='white')
ax.contour(S,T,prod,levels=[.001,.004,.01,.02,.03,.035],colors='#286ca1',linewidths=1.4)
verts=np.array([[0,0],[1,0],[.5,np.sqrt(3)/2],[0,0]])
ax.plot(verts[:,0],verts[:,1],color='#b62f2f',lw=2.3)
for A,B in zip(verts[:-1],verts[1:]):
 delta=B-A;ax.annotate('',xy=A+.61*delta,xytext=A+.41*delta,arrowprops={'arrowstyle':'->','color':'#b62f2f','lw':2})
for u,w,z in [(.7,.18,.12),(.12,.7,.18),(.18,.12,.7),(.45,.36,.19),(.19,.45,.36),(.36,.19,.45)]:
 du=2*u*(z-w);dw=2*w*(u-z);dz=2*z*(w-u)
 vel=np.array([dw+.5*dz,np.sqrt(3)/2*dz]);vel=vel/np.linalg.norm(vel)*.045
 start=np.array([w+.5*z,np.sqrt(3)/2*z]);ax.annotate('',xy=start+vel,xytext=start-vel,arrowprops={'arrowstyle':'->','color':'#286ca1','lw':1.3})
ax.scatter([0,1,.5],[0,0,np.sqrt(3)/2],marker='x',color='black',s=75,zorder=5)
ax.scatter([.5],[np.sqrt(3)/6],color='black',s=32,zorder=5)
ax.text(-.025,-.035,'x-axis\nU = 1',ha='center',va='top');ax.text(1.025,-.035,'y-axis\nW = 1',ha='center',va='top');ax.text(.5,np.sqrt(3)/2+.04,'z-axis\nZ = 1',ha='center',va='bottom')
ax.annotate('Center: U = W = Z = 1/3',(.5,np.sqrt(3)/6),xytext=(.60,.63),arrowprops={'arrowstyle':'-','color':'#777777'},fontsize=10)
ax.text(.5,-.16,'Blue: closed contours of UWZ\nRed: heteroclinic cycle; arrows for c = e > 0\nOther octants follow by sign reflection; c < 0 reverses arrows.',ha='center',fontsize=10)
ax.set_title('One octant of X = μ/a in squared coordinates',pad=15)
ax.set(xlim=(-.13,1.13),ylim=(-.23,1.03));ax.set_aspect('equal');ax.axis('off');fig.tight_layout()
fig.savefig('paper-78-sphere.png',dpi=145,facecolor='white',transparent=False)
