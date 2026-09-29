"""Original bistable-flow sketch. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-1-bistable-flow.png to caller CWD; inherits MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

MU, NU = 0.3, 1.0

def field(p):
    x, y = p
    return np.array([-MU*x+y, x*x/(1+x*x)-NU*y])

def trajectory(p, dt, steps=3500):
    out=[np.array(p,dtype=float)]
    for _ in range(steps):
        v=out[-1]
        k1=field(v);k2=field(v+dt*k1/2);k3=field(v+dt*k2/2);k4=field(v+dt*k3)
        v=v+dt*(k1+2*k2+2*k3+k4)/6
        if not (0<=v[0]<=4.2 and 0<=v[1]<=1.45): break
        out.append(v)
    return np.array(out)

def main():
    x=np.linspace(0,4.1,180);y=np.linspace(0,1.4,120)
    xx,yy=np.meshgrid(x,y)
    fig,ax=plt.subplots(figsize=(8,4.9),dpi=125,facecolor='white')
    ax.set_facecolor('white')
    ax.streamplot(x,y,-MU*xx+yy,xx*xx/(1+xx*xx)-NU*yy,color='#c5cbd1',density=1.0,linewidth=.7,arrowsize=.8)
    ax.plot(x,MU*x,color='#255c9b',lw=2,label=r'$\dot x=0$')
    ax.plot(x,x*x/(NU*(1+x*x)),color='#31845b',lw=2,label=r'$\dot y=0$')
    roots=[(1-np.sqrt(1-4*MU*MU*NU*NU))/(2*MU*NU),(1+np.sqrt(1-4*MU*MU*NU*NU))/(2*MU*NU)]
    saddle=np.array([roots[0],MU*roots[0]])
    J=np.array([[-MU,1],[2*saddle[0]/(1+saddle[0]**2)**2,-NU]])
    vals,vecs=np.linalg.eig(J)
    for name,i,dt,color,ls in [('stable',int(np.argmin(vals)),-.012,'#cb7925','--'),('unstable',int(np.argmax(vals)),.025,'#a63d75','-')]:
        v=vecs[:,i].real;v/=np.linalg.norm(v)
        for sign in [-1,1]:
            path=trajectory(saddle+sign*1e-5*v,dt)
            ax.plot(path[:,0],path[:,1],color=color,ls=ls,lw=2,label=f'{name} manifold' if sign==1 else None)
    for p,label,offset in [(np.zeros(2),'O',(7,8)),(saddle,r'$P_-$',(8,10)),(np.array([roots[1],MU*roots[1]]),r'$P_+$',(7,8))]:
        ax.scatter(*p,s=35,color='#242424',zorder=5)
        ax.annotate(label,p,xytext=offset,textcoords='offset points',fontsize=11)
    ax.set(xlim=(-.025,4.1),ylim=(-.015,1.4),xlabel='$x$',ylabel='$y$',title=r'Bistability: $\mu=0.3$, $\nu=1$')
    ax.legend(loc='upper left',fontsize=9,framealpha=1)
    fig.tight_layout()
    fig.savefig('paper-1-bistable-flow.png',facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
