"""Competition phase portraits; Python 3.14, dependencies in pyproject.toml."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

A, B, RHO = 2., .75, 1.
RED, GREY, PATH = '#b33336', '#276a94', '#62518c'

def field(z, gamma):
    x, y = z
    return np.array([x*(1-x-A*y), RHO*y*(gamma-y-B*x)])

def trajectory(start, gamma, step=.025, count=4800):
    z = np.array(start, dtype=float)
    points = [z.copy()]
    for _ in range(count):
        k1 = field(z, gamma)
        k2 = field(z+step*k1/2, gamma)
        k3 = field(z+step*k2/2, gamma)
        k4 = field(z+step*k3, gamma)
        z = np.maximum(0, z+step*(k1+2*k2+2*k3+k4)/6)
        points.append(z.copy())
        if np.linalg.norm(points[-1]-points[-2]) < 1e-10:
            break
    return np.array(points)

fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=100, facecolor='white', sharey=True)
starts = [(x,y) for x,y in [(0.03,0.05),(.15,.1),(.1,.45),(.35,.15),(.8,.08),(.7,.7),(1.25,.25),(.2,1.1),(.8,1.1),(1.25,1.05)]]
for ax, gamma, title in zip(axes, [1., .62, .4], ['Grey dominance', 'Two stable outcomes', 'Red dominance']):
    ax.set_facecolor('white')
    xx, yy = np.meshgrid(np.linspace(.035,1.3,15),np.linspace(.035,1.12,14))
    fx, fy = field((xx,yy),gamma)
    size = np.hypot(fx,fy)
    ax.quiver(xx,yy,fx/np.maximum(size,1e-14),fy/np.maximum(size,1e-14),color='#b8b8b8',alpha=.65,scale=26,width=.003)
    x = np.linspace(0,1.4,400)
    y1=(1-x)/A;y2=gamma-B*x
    ax.plot(x[y1>=0],y1[y1>=0],color=RED,lw=2,label='Red nullcline')
    ax.plot(x[y2>=0],y2[y2>=0],color=GREY,lw=2,label='Grey nullcline')
    for start in starts:
        p=trajectory(start,gamma)
        ax.plot(p[:,0],p[:,1],color=PATH,lw=1,alpha=.75)
    ax.scatter([1],[0],s=54,facecolor=RED if gamma<B else 'white',edgecolor=RED,zorder=4,clip_on=False)
    ax.scatter([0],[gamma],s=54,facecolor=GREY if gamma>1/A else 'white',edgecolor=GREY,zorder=4,clip_on=False)
    if 1/A < gamma < B:
        ax.scatter([(A*gamma-1)/(A*B-1)],[(B-gamma)/(A*B-1)],marker='x',color='black',s=50,zorder=5)
    ax.set(xlim=(0,1.35),ylim=(0,1.15),xlabel=r'Red population $u_1$',title=title+rf' ($\gamma={gamma:g}$)')
    ax.spines[['top','right']].set_visible(False)
axes[0].set_ylabel(r'Grey population $u_2$')
axes[0].legend(loc='upper right',fontsize=9,frameon=True)
fig.suptitle(r'Competition with removal: $A=2$, $B=0.75$, $\rho=1$',fontsize=13)
fig.tight_layout(rect=(0,0,1,.95))
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
