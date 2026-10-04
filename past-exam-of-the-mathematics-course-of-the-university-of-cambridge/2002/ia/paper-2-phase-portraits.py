"""Original figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to caller CWD."""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='ia2-phase-mpl-')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def vector(z,alpha):
    x,y=z
    return np.array([alpha*x-y+y**3,-x])

def trajectory(z,alpha,dt,steps=23000):
    points=[np.array(z,dtype=float)]
    for _ in range(steps):
        z=points[-1]
        k1=vector(z,alpha);k2=vector(z+dt*k1/2,alpha)
        k3=vector(z+dt*k2/2,alpha);k4=vector(z+dt*k3,alpha)
        z=z+dt*(k1+2*k2+2*k3+k4)/6
        points.append(z)
        if abs(z[0])>1.9 or abs(z[1])>2.1: break
    return np.array(points)

fig,axes=plt.subplots(1,3,figsize=(11.5,4.6),layout='constrained')
xs=np.linspace(-1.8,1.8,240);ys=np.linspace(-2,2,270);X,Y=np.meshgrid(xs,ys)
for ax,alpha in zip(axes,[0.,.1,-.1]):
    U=alpha*X-Y+Y**3;V=-X;norm=np.hypot(U,V)
    ax.streamplot(xs,ys,U/np.maximum(norm,1e-8),V/np.maximum(norm,1e-8),density=.85,color='#c4c7cf',linewidth=.55,arrowsize=.75)
    if alpha==0:
        H=X*X-Y*Y+Y**4/2
        ax.contour(X,Y,H,levels=[-.46,-.3,-.12,.16,.6,1.3,2.3],colors='#1664ba',linewidths=.9)
        ax.contour(X,Y,H,levels=[0],colors='#882255',linewidths=2)
    else:
        eigenvalues=[(alpha-np.sqrt(alpha*alpha+4))/2,(alpha+np.sqrt(alpha*alpha+4))/2]
        for eig,color in zip(eigenvalues,['#ba620d','#882255']):
            direction=np.array([1.,-1/eig]);direction/=np.linalg.norm(direction)
            for sign in [-1,1]:
                t=trajectory(sign*1e-4*direction,alpha,-.012 if eig<0 else .012)
                ax.plot(t[:,0],t[:,1],color=color,lw=1.4)
    ax.scatter([0,0],[1,-1],color='#1664ba',s=24,zorder=4)
    ax.scatter([0],[0],color='black',marker='x',s=28,zorder=4)
    name='Centers and closed orbits' if alpha==0 else ('Outward spirals; unstable foci' if alpha>0 else 'Inward spirals; stable foci')
    ax.set(xlim=(-1.8,1.8),ylim=(-2,2),xlabel='x',ylabel='y',title=f'α = {alpha:g}\n{name}')
    ax.set_aspect('equal')
fig.suptitle('Quartic double well: arrows show forward time; orange stable and purple unstable saddle branches',fontsize=10)
fig.savefig('paper-2-phase-portraits.png',dpi=125,facecolor='white',transparent=False)
