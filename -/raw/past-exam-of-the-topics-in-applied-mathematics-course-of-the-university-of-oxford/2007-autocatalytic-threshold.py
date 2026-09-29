# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Writes PNG to CWD.
import numpy as np
import matplotlib.pyplot as plt
eps=.06;K=1.;lam=.6;eta=.3;ue=lam/eta-K;ve=ue/(ue+K)
def rhs(z):
 u,v=z;return np.array([eta*u-u+u*v+(K-lam)*v,(u-u*v-K*v)/eps])
def step(z,dt):
 a=rhs(z);b=rhs(z+dt*a/2);c=rhs(z+dt*b/2);e=rhs(z+dt*c);return z+dt*(a+2*b+2*c+e)/6
fig,ax=plt.subplots(figsize=(7,5),facecolor='white');u=np.linspace(0,3,500)
ax.plot(u,u/(u+K),label="Complex nullcline",color='#246b9b');ax.plot(u,(1-eta)*u/(u+K-lam),label='Substrate nullcline',color='#2c834d')
xx,yy=np.meshgrid(np.linspace(.05,2.95,21),np.linspace(.03,1.1,13));du=eta*xx-xx+xx*yy+(K-lam)*yy;dv=(xx-xx*yy-K*yy)/eps;norm=np.sqrt(du*du+dv*dv);ax.quiver(xx,yy,du/norm,dv/norm,color='#b5b5b5',alpha=.7)
J=np.array([[eta-1+ve,ue+K-lam],[(1-ve)/eps,-(ue+K)/eps]]);vals,vec=np.linalg.eig(J);v=vec[:,np.argmin(vals)].real;v/=np.linalg.norm(v)
for sign in [-1,1]:
 z=np.array([ue,ve])+sign*1e-6*v;arr=[z.copy()]
 for i in range(5000):
  z=step(z,-.0004);arr.append(z.copy())
  if z[1]<0 or z[1]>1.13:break
 arr=np.array(arr);ax.plot(arr[:,0],arr[:,1],color='#aa2a67',lw=2,label='Stable separatrix'if sign==1 else None)
for u0,col in [(.8,'#3946b2'),(1.3,'#cb4829')]:
 z=np.array([u0,0.]);arr=[z.copy()]
 for i in range(14000):
  z=step(z,.001);arr.append(z.copy())
  if z[0]>3:break
 arr=np.array(arr);ax.plot(arr[:,0],arr[:,1],color=col,lw=2)
ax.scatter([0,ue],[0,ve],color='black',zorder=6);ax.text(.05,.04,'Attracting origin');ax.text(ue+.07,ve+.04,'Saddle');ax.set(xlim=(0,3),ylim=(0,1.13),xlabel='Scaled substrate u',ylabel='Complex fraction v',title='Extinction and autocatalytic runaway');ax.legend(loc='upper left',fontsize=8);ax.grid(alpha=.15);fig.tight_layout()
fig.savefig('2007-autocatalytic-threshold.png',dpi=160,facecolor='white')
