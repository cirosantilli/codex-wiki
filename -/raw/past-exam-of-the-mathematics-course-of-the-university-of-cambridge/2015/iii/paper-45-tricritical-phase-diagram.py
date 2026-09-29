"""Generate paper-45-tricritical-phase-diagram.png in the current directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject deps).
"""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'codex-wiki-matplotlib'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def wing(u,q):
    # Two equal global minima a=q*ell and b=ell, sextic coefficient v=1.
    u0=-2*(2*q*q+q+2)/3
    ell=np.sqrt(u/u0)
    s=(q+1)*ell;p=q*ell*ell
    r=(s**4-s*s*p+3*p*p)/3
    h=s**3*p/3
    return r,h

def main():
    fig=plt.figure(figsize=(12,6),dpi=100,facecolor='white',layout='constrained')
    ax=fig.add_subplot(1,2,1)
    u=np.linspace(-1.2,.7,300);rco=np.where(u<0,3*u*u/16,0)
    ax.fill_betweenx(u,-.25,rco,color='#d4e9dd')
    ax.fill_betweenx(u,rco,.7,color='#e3edf7')
    un=u[u<0];up=u[u>=0]
    ax.plot(3*un*un/16,un,color='#7a3591',lw=2.5,label='First-order coexistence')
    ax.plot(np.zeros_like(up),up,color='#1a6c40',lw=2.5,label='Continuous critical line')
    ax.scatter([0],[0],s=65,color='black',zorder=5)
    ax.annotate('Tricritical point',(0,0),(.18,.22),arrowprops={'arrowstyle':'->'},fontsize=10)
    ax.text(-.22,-.82,'Ordered\n$M=\\pm M_0$',fontsize=11)
    ax.text(.38,-.46,'Disordered\n$M=0$',fontsize=11)
    ax.text(.14,-1.08,'$r=3u^2/16$\n($v=1$)',color='#7a3591',fontsize=11)
    ax.set(xlim=(-.25,.7),ylim=(-1.2,.7),xlabel='$r$ (temperature-like control)',ylabel='$u$ (quartic control)',title='Symmetric slice: $h=0$')
    ax.legend(loc='upper right',fontsize=8,frameon=False)
    ax.grid(alpha=.2)
    bx=fig.add_subplot(1,2,2,projection='3d')
    us=np.linspace(-1.2,-.001,65);qs=np.linspace(0,1,60)
    U,Q=np.meshgrid(us,qs);RR,HH=wing(U,Q)
    bx.plot_surface(U,RR,HH,color='#d78b22',alpha=.7,linewidth=0,antialiased=True)
    bx.plot_surface(U,RR,-HH,color='#367cad',alpha=.7,linewidth=0,antialiased=True)
    # h=0 ordered +/- coexistence sheet, bounded by the triple/critical curves.
    ua=np.linspace(-1.2,.7,65);fraction=np.linspace(0,1,25)
    UA,FF=np.meshgrid(ua,fraction);top=np.where(UA<0,3*UA**2/16,0)
    RA=-.25+FF*(top+.25)
    bx.plot_surface(UA,RA,np.zeros_like(RA),color='#666666',alpha=.18,linewidth=0)
    rc,hc=wing(us,np.ones_like(us))
    bx.plot(us,rc,hc,color='#a52022',lw=2.2)
    bx.plot(us,rc,-hc,color='#a52022',lw=2.2)
    bx.plot(us,3*us**2/16,np.zeros_like(us),color='#7a3591',lw=2.3)
    bx.plot(up,np.zeros_like(up),np.zeros_like(up),color='#1a6c40',lw=2.3)
    bx.scatter([0],[0],[0],color='black',s=45,depthshade=False)
    bx.set(xlabel='$u$',ylabel='$r$',zlabel='$h$',xlim=(-1.2,.7),ylim=(-.25,.7),zlim=(-.22,.22),title='Three-dimensional coexistence surfaces')
    bx.view_init(elev=24,azim=-62)
    bx.set_box_aspect((1.25,1,1))
    handles=[Patch(color='#d78b22',alpha=.7,label='First-order wings (both signs of $h$)'),Line2D([],[],color='#a52022',lw=2,label='Ordinary critical wing edges'),Line2D([],[],color='#7a3591',lw=2,label='Three-phase line at $h=0$'),Patch(color='#666666',alpha=.3,label='Ordered +/- coexistence sheet')]
    bx.legend(handles=handles,loc='upper left',bbox_to_anchor=(-.05,-.06),fontsize=8,frameon=False)
    fig.suptitle('Sextic Landau potential: $f=rM^2/2+uM^4/4+M^6/6-hM$',fontsize=13)
    fig.savefig(Path.cwd()/'paper-45-tricritical-phase-diagram.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
