"""Original asymptotic sketches. Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7.
Run from the output directory. Dependencies are in the wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,2,figsize=(11,5),constrained_layout=True)
xs=np.linspace(-3.5,4.1,800); h=lambda x:x**3/3-x
for ax, positive in zip(axes,[True,False]):
    ax.plot(xs,h(xs),color='#444444',lw=1.5,label=r'$y=x^3/3-x$')
    for xx in [-2.8,-1.5,-.5,.5,1.5,2.8]:
        for yy in [-1.4,0,1.4]:
            f=xx-xx**3/3+yy; direction=np.sign(f)*(1 if positive else -1)
            ax.annotate('',xy=(xx+.24*direction,yy),xytext=(xx,yy),arrowprops=dict(arrowstyle='->',color='#999999',lw=.8))
    ax.axhline(0,color='#cccccc',lw=.6);ax.axvline(0,color='#cccccc',lw=.6)
    ax.set(xlabel='$x$',ylabel='$y$',ylim=(-2.4,2.2));ax.grid(alpha=.12)
right=np.linspace(2,1,150);left=np.linspace(-2,-1,150)
for xx in [right,left]:axes[0].plot(xx,h(xx),lw=3,color='#256998')
for yy,a,b in [(-2/3,1,-2),(2/3,-1,2)]:axes[0].annotate('',xy=(b,yy),xytext=(a,yy),arrowprops=dict(arrowstyle='->',color='#256998',lw=2))
for a,b in [(1.8,1.6),(-1.8,-1.6)]:axes[0].annotate('',xy=(b,h(b)),xytext=(a,h(a)),arrowprops=dict(arrowstyle='->',color='#256998',lw=2))
axes[0].scatter([1,-1],[-2/3,2/3],s=20,color='#256998');axes[0].set(xlim=(-3.2,3.2),title=r'$\epsilon\to0^+$: attracting outer branches')
# Numerical trajectories only illustrate the small-negative-epsilon motion.
def rhs(z):
    x,y=z
    return np.array([-x+x**3/3-y,-.02*x])
for z0,col,label in [([3.,1.],'#b9413b','(3, 1)'),([1.,-2.],'#c17b18','(1, -2)'),([-1.,-1/3],'#39834b','(-1, -1/3)')]:
    z=np.array(z0);out=[z.copy()];dt=.004
    for _ in range(60000):
        a=rhs(z);b=rhs(z+dt*a/2);c=rhs(z+dt*b/2);e=rhs(z+dt*c);z=z+dt*(a+2*b+2*c+e)/6
        out.append(z.copy())
        if abs(z[0])>4.1 or abs(z[1])>3:break
    q=np.array(out);axes[1].plot(q[:,0],q[:,1],color=col,lw=2,label=label);axes[1].scatter(*z0,color=col,s=22)
axes[1].set(xlim=(-2.1,4.1),title=r'$\epsilon=-0.02$: central attraction, then escape');axes[1].legend(fontsize=8,loc='upper left')
fig.savefig('2009-relaxation-phase-plane.png',dpi=145,facecolor='white')
