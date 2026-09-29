# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Writes PNG to CWD.
import numpy as np
import matplotlib.pyplot as plt
def rhs(z):
 x,y=z;return np.array([y,2*x-y-3*x**3])
def step(z,dt):
 a=rhs(z);b=rhs(z+dt*a/2);c=rhs(z+dt*b/2);d=rhs(z+dt*c);return z+dt*(a+2*b+2*c+d)/6
fig,ax=plt.subplots(figsize=(7,5),facecolor='white');x,y=np.meshgrid(np.linspace(-1.65,1.65,180),np.linspace(-2,2,190));ax.streamplot(x,y,y,2*x-y-3*x**3,density=1.0,color='#c5c5c5',linewidth=.6,arrowsize=.8)
for sign in [-1,1]:
 z=np.array([sign*.0002,sign*.0002]);arr=[z.copy()]
 for i in range(2200):z=step(z,.01);arr.append(z.copy())
 arr=np.array(arr);ax.plot(arr[:,0],arr[:,1],color='#c34127',lw=2,label='Unstable branches'if sign==1 else None)
 z=np.array([sign*.0001,-sign*.0002]);arr=[z.copy()]
 for i in range(2500):
  z=step(z,-.004);arr.append(z.copy())
  if abs(z[0])>1.7 or abs(z[1])>2.1:break
 arr=np.array(arr);ax.plot(arr[:,0],arr[:,1],color='#244eab',lw=2,label='Stable branches'if sign==1 else None)
xx=np.linspace(-.36,.36,200);ax.plot(xx,-2*xx+3*xx**3/7,'--',color='#163f9f',lw=2,label='Stable cubic graph');ax.plot(xx,xx-3*xx**3/5,'--',color='#9c271c',lw=2,label='Unstable cubic graph');ax.scatter([0,np.sqrt(2/3),-np.sqrt(2/3)],[0,0,0],color='black',s=24,zorder=5);ax.set(xlim=(-1.65,1.65),ylim=(-2,2),xlabel='$x$',ylabel='$y$',title='Damped double-well phase portrait');ax.legend(loc='lower right',fontsize=8);ax.grid(alpha=.15);fig.tight_layout()
fig.savefig('2007-damped-double-well.png',dpi=160,facecolor='white')
