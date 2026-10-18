"""Original affine-plane and sphere-section geometry. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig=plt.figure(figsize=(10.8,5.1),layout='constrained');ax=fig.add_subplot(121,projection='3d');bx=fig.add_subplot(122)
a=np.array([3,1,-2]);p=np.array([-4,1,6]);q=np.array([-1,-2,3]);s,t=np.meshgrid(np.linspace(-.15,1.1,9),np.linspace(-.15,1.1,9));r=a[:,None,None]+p[:,None,None]*s+q[:,None,None]*t
ax.plot_surface(*r,alpha=.2,color='tab:blue',edgecolor='white',linewidth=.5)
ax.quiver(0,0,0,*a,color='black',arrow_length_ratio=.12);ax.quiver(*a,*p,color='tab:red',arrow_length_ratio=.1);ax.quiver(*a,*q,color='tab:green',arrow_length_ratio=.12)
for point,label,color in [(a,'A = r₀','black'),(a+p,'B = r₀ + p','tab:red'),(a+q,'C = r₀ + q','tab:green')]:ax.scatter(*point,color=color,s=24);ax.text(*(point+np.array([.15,.1,.15])),label,color=color,fontsize=9)
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Plane: 5x + 2y + 3z = 11');ax.view_init(elev=25,azim=-58)
u=np.linspace(0,2*np.pi,1001);d=.55;rad=np.sqrt(1-d*d)
bx.plot(np.cos(u),np.sin(u),color='tab:blue',label='sphere cross-section');bx.plot([-1.1,1.1],[d,d],color='tab:red',label='cutting plane, edge-on')
bx.plot([0,rad],[0,d],color='.4');bx.plot([0,0],[0,d],'--',color='.4');bx.plot([0,rad],[d,d],color='black',lw=2);bx.plot([0,0,rad],[0,d,d],'o',color='black',ms=4)
bx.text(-.08,-.12,'S',ha='right');bx.text(-.07,d+.04,'H',ha='right');bx.text(.04,d/2,'d');bx.text(rad/2,d+.06,'r');bx.text(rad/2+.08,d/2-.05,'R')
bx.plot([0,.07,.07],[d-.07,d-.07,d],color='.4',lw=.8);bx.set(xlabel='coordinate within the plane',ylabel='normal coordinate',xlim=(-1.2,1.2),ylim=(-1.15,1.2),title=r'Perpendicular section: $r^2+d^2=R^2$');bx.set_aspect('equal');bx.legend(fontsize=9,loc='lower left');bx.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
