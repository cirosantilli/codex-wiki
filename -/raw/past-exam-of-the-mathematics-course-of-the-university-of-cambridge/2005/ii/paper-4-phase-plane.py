"""Phase portrait for the feedback system; Python 3.14, NumPy, Matplotlib.
Output is an opaque PNG in the caller's current directory.
The caller supplies MPLCONFIGDIR when its default cache is unavailable.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-3.2,3.2,150)
y=np.linspace(-2,4.5,150)
X,Y=np.meshgrid(x,y)
U=X*(1-Y);V=X*X-Y
speed=np.hypot(U,V)
fig,ax=plt.subplots(figsize=(8,6),dpi=130,facecolor='white')
ax.set_facecolor('white')
ax.streamplot(x,y,U,V,color='#b1b8c2',density=1.0,linewidth=.65,arrowsize=.8)
ax.plot(x,np.ones_like(x),'--',color='#2563a6',lw=1.3,label='Horizontal nullcline: y = 1')
xx=np.linspace(-2.12,2.12,300)
ax.plot(xx,xx*xx,'--',color='#c08018',lw=1.3,label='Vertical nullcline: y = x²')
ax.axvline(0,color='#76569b',lw=1.5,label='Stable axis: x = 0')
def f(z):
    return np.array([z[0]*(1-z[1]),z[0]**2-z[1]])
def trajectory(z,n=6000,h=.006):
    ans=[np.asarray(z,dtype=float)]
    for _ in range(n):
        z=ans[-1]
        a=f(z);b=f(z+h*a/2);c=f(z+h*b/2);d=f(z+h*c)
        ans.append(z+h*(a+2*b+2*c+d)/6)
    return np.array(ans)
for z,color in [((2,-1),'#b73337'),((-2,-1),'#22634b'),((.25,3.5),'#257fb9'),((-.25,3.5),'#7a8c24')]:
    a=trajectory(z)
    ax.plot(a[:,0],a[:,1],lw=1.4,color=color)
    ax.scatter(*a[0],s=22,color=color,zorder=5)
    j=140
    ax.annotate('',xy=a[j+12],xytext=a[j],arrowprops={'arrowstyle':'->','color':color,'lw':1.5})
ax.scatter([0],[0],s=45,marker='x',color='black',zorder=8)
ax.scatter([-1,1],[1,1],s=45,color='black',zorder=8)
ax.annotate('saddle',(0,0),xytext=(.16,-.32),fontsize=9)
ax.annotate('stable focus',(1,1),xytext=(1.2,1.35),fontsize=9)
ax.annotate('stable focus',(-1,1),xytext=(-2.5,1.35),fontsize=9)
ax.set(xlim=(-3.2,3.2),ylim=(-2,4.5),xlabel='x',ylabel='y',title='Feedback system: stable foci separated by a saddle axis')
ax.legend(loc='upper right',fontsize=8,framealpha=1)
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig('paper-4-phase-plane.png',facecolor='white',transparent=False)
plt.close(fig)
