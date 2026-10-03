"""Original C3 diagram. Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-1-c3-roots-chambers.png in the current directory.
The caller's MPLCONFIGDIR is preserved; no environment mutation is needed.
"""
from itertools import combinations, product
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

def unit(x):
    x=np.asarray(x,dtype=float)
    return x/np.linalg.norm(x)

E=np.eye(3)
long=np.array([2*s*E[i] for i in range(3) for s in (-1,1)])
short=np.array([s*E[i]+t*E[j] for i,j in combinations(range(3),2) for s,t in product((-1,1),repeat=2)])
fig=plt.figure(figsize=(12.4,6.2),dpi=100,facecolor='white')
ax=fig.add_subplot(121,projection='3d')
for roots,col,label in ((short,'#236da7','12 short roots'),(long,'#c94635','6 long roots')):
    ax.quiver(np.zeros(len(roots)),np.zeros(len(roots)),np.zeros(len(roots)),roots[:,0],roots[:,1],roots[:,2],color=col,alpha=.78,arrow_length_ratio=.055,linewidth=.9)
    ax.scatter(*roots.T,s=25,color=col,label=label,depthshade=False)
for i in range(3):
    p=2.22*E[i]
    # Coordinate axes already label directions; no crowded tip annotations.
ax.set(xlim=(-2.3,2.3),ylim=(-2.3,2.3),zlim=(-2.3,2.3),xlabel='$x_1$',ylabel='$x_2$',zlabel='$x_3$')
ax.set_box_aspect((1,1,1))
ax.view_init(elev=22,azim=35)
ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);ax.set_zticks([-2,0,2])
ax.set_title('C3 roots: actual relative lengths',pad=18)
ax.legend(loc='upper left',frameon=False,fontsize=10)

bx=fig.add_subplot(122)
n=unit([3,2,1]);u=unit([-2,3,0]);v=np.cross(n,u)
def project(points):
    points=np.asarray(points)
    return np.stack((points@u,points@v),axis=-1)
verts=[E[0],unit([1,1,0]),unit([1,1,1])]
def arc(a,b,count=120):
    t=np.linspace(0,1,count)
    points=(1-t[:,None])*a+t[:,None]*b
    return points/np.linalg.norm(points,axis=1)[:,None]
boundary=np.concatenate([arc(verts[i],verts[(i+1)%3]) for i in range(3)])
bx.add_patch(Polygon(project(boundary),closed=True,facecolor='#f3ce69',edgecolor='none',alpha=.9))
# All nine reflecting planes; each great circle is drawn only on the visible hemisphere.
normals=list(E)+[E[i]+s*E[j] for i,j in combinations(range(3),2) for s in (-1,1)]
for normal in normals:
    normal=unit(normal)
    seed=E[np.argmin(abs(normal))]
    a=unit(np.cross(normal,seed));b=np.cross(normal,a)
    theta=np.linspace(0,2*np.pi,1600)
    pts=np.cos(theta)[:,None]*a+np.sin(theta)[:,None]*b
    p=project(pts)
    p[pts@n < -1e-8]=np.nan
    bx.plot(p[:,0],p[:,1],color='#526375',lw=1)
bx.add_patch(Circle((0,0),1,fill=False,edgecolor='#26374a',lw=1.5))
for point,label,offset in zip(verts,['$(1,0,0)$',r'$(1,1,0)/\sqrt{2}$',r'$(1,1,1)/\sqrt{3}$'],[(-.28,-.12),(.04,-.12),(.02,.06)]):
    x,y=project(point)
    bx.scatter(x,y,s=23,color='#92481e',zorder=6)
    bx.text(x+offset[0],y+offset[1],label,fontsize=10,zorder=7)
center=project(unit([3,2,1]))
bx.text(center[0]-.36,center[1]-.035,'$x_1>x_2>x_3>0$',fontsize=10,color='#773b12')
bx.set_aspect('equal');bx.set_xlim(-1.15,1.15);bx.set_ylim(-1.15,1.15);bx.axis('off')
bx.set_title('Weyl chambers on a visible hemisphere',pad=17)
bx.text(0,-1.17,'9 reflecting planes; 48 spherical triangles on the full sphere',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.98,top=.88,bottom=.12,wspace=.13)
fig.savefig('paper-1-c3-roots-chambers.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
