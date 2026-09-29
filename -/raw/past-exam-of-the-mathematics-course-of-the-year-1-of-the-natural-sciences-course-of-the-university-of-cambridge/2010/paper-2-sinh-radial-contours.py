"""Original contour sketch. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Save the white PNG to cwd, normally the mirrored _media paper directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6.3,6.3,1000);X,Y=np.meshgrid(x,x)
H=Y*(np.hypot(X,Y)-4)
fig,ax=plt.subplots(figsize=(7.2,6.4),layout='constrained',facecolor='white')
levels=[-8,-3,-1,1,3,8]
fmt={v:rf'$\sinh({v})$' for v in levels}
# Label each level explicitly, including both its closed and unbounded components.
for value in levels:
    cs=ax.contour(X,Y,H,levels=[value],colors=['#0072b2' if value<0 else '#d55e00'],linewidths=1.35)
    sign=np.sign(value)
    manual=[(0,sign*(2+np.sqrt(4+abs(value))))]
    if abs(value)<4:
        manual.append((0,-sign*(2+np.sqrt(4-abs(value)))))
    ax.clabel(cs,fmt=fmt,manual=manual,inline=True,fontsize=9)
p=np.linspace(0,2*np.pi,600)
ax.plot(4*np.cos(p),4*np.sin(p),color='#444444',lw=1.4)
ax.axhline(0,color='#444444',lw=1.4)
ax.text(-5.9,.17,'$g=0$',fontsize=10,color='#333333')
ax.text(2.9,3.0,'$g=0$',fontsize=10,color='#333333')
for px,py in [(-4,0),(4,0),(0,2),(0,-2)]:
    ax.scatter(px,py,color='#222222',s=23,zorder=5)
ax.annotate(r'Minimum: $-\sinh4$',(0,2),xytext=(.45,2.55),arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
ax.annotate(r'Maximum: $+\sinh4$',(0,-2),xytext=(.45,-2.8),arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
ax.annotate('Saddle: 0',(-4,0),xytext=(-5.8,-1.0),arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
ax.annotate('Saddle: 0',(4,0),xytext=(4.3,1.1),arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
ax.set(xlabel='$x$',ylabel='$y$',title=r'Level values of $g=\sinh[y(\sqrt{x^2+y^2}-4)]$',xlim=(-6.3,6.3),ylim=(-6.3,6.3))
ax.set_aspect('equal');ax.set_xticks([-6,-4,-2,0,2,4,6]);ax.set_yticks([-6,-4,-2,0,2,4,6]);ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
