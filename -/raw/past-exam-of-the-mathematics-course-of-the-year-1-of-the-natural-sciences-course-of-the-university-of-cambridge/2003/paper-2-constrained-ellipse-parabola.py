"""Plot original quadratic contours and their minimum on a parabola."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams.update({'font.size':11, 'figure.facecolor':'white', 'axes.facecolor':'white'})
    roots=np.roots([3,-21,48,-32])
    lam=float(next(root.real for root in roots if abs(root.imag)<1e-10))
    xm=lam/(6*lam-16)
    ym=xm*xm-.25
    minimum=2*(xm-ym)**2+(xm+ym)**2
    fig,ax=plt.subplots(figsize=(6.4,6.1),dpi=120,layout='constrained')
    t=np.linspace(0,2*np.pi,1200)
    for value in [minimum,.4,1,2.5]:
        p=np.sqrt(value/2)*np.cos(t)
        q=np.sqrt(value/4)*np.sin(t)
        xx=(p+q)/np.sqrt(2)
        yy=(p-q)/np.sqrt(2)
        special=value==minimum
        ax.plot(xx,yy,color='#227ca6' if special else '#9cbac9',lw=2.6 if special else 1.25,label=fr'$u_{{\min}}={minimum:.5f}$' if special else None)
        if not special:
            ind=130
            ax.text(xx[ind]+.015,yy[ind]+.012,f'u = {value:g}',fontsize=10,color='#4f6d7c')
    xp=np.linspace(-1.1,1.1,800)
    ax.plot(xp,xp*xp-.25,color='#b76527',lw=2.2,label=r'Constraint $y=x^2-1/4$')
    ax.scatter([xm],[ym],color='#842b58',s=40,zorder=6)
    ax.annotate(f'Unique minimum\n({xm:.4f}, {ym:.4f})',xy=(xm,ym),xytext=(-.96,-.63),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
    ax.axhline(0,color='0.6',lw=.8)
    ax.axvline(0,color='0.6',lw=.8)
    ax.set(xlim=(-1.12,1.12),ylim=(-.79,1.12),xlabel='x',ylabel='y',title=r'Quadratic contours $u=2(x-y)^2+(x+y)^2$')
    ax.set_aspect('equal')
    ax.legend(loc='upper center',fontsize=10)
    ax.grid(alpha=.15)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
