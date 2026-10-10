"""Exact geometric acceptance of an on-axis disk; output basename.png in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(geo,ax)=plt.subplots(1,2,figsize=(10.6,4.8),layout='constrained',gridspec_kw={'width_ratios':[1,1.15]})
    geo.plot([0,1],[0,1],color='#ed8b29',lw=2)
    geo.plot([0,1],[0,-1],color='#ed8b29',lw=2)
    geo.plot([0,1.15],[0,0],color='#788a96',ls=':',lw=1.3)
    geo.plot([1,1],[-1,1],color='#1476a5',lw=5)
    geo.scatter([0],[0],color='black',s=28)
    geo.text(-.10,-.19,'O')
    geo.add_patch(Arc((0,0),.75,.75,theta1=0,theta2=45,color='#202020',lw=1.4))
    geo.text(.40,.12,r'$\theta$',fontsize=14)
    geo.annotate('',xy=(1.18,1),xytext=(1.18,0),arrowprops={'arrowstyle':'<->','color':'#1476a5'})
    geo.text(1.25,.45,r'$a$')
    geo.annotate('',xy=(1,-1.28),xytext=(0,-1.28),arrowprops={'arrowstyle':'<->','color':'#535e66'})
    geo.text(.47,-1.50,r'$d$')
    geo.text(.04,1.36,'On-axis circular detector',weight='bold')
    geo.text(-.12,-1.93,r'$\tan\theta=a/d$; disk area $A=\pi a^2$',fontsize=11)
    geo.text(-.12,-2.23,'Meridian section; the blue segment rotates about the axis.',fontsize=10)
    geo.set_aspect('equal');geo.set_xlim(-.25,1.75);geo.set_ylim(-2.4,1.7);geo.axis('off')
    ratio=np.geomspace(.2,12,500)
    exact=.5/(np.sqrt(1+ratio**2)*(np.sqrt(1+ratio**2)+ratio))
    # Stable form of (1-d/sqrt(d²+a²))/2 with a=1.
    ax.plot(ratio,exact,color='#1476a5',lw=2.6,label='Exact disk acceptance')
    far=ratio[ratio>=.72]
    ax.plot(far,1/(4*far**2),color='#c55b28',ls='--',lw=2,label=r'Far-field $a^2/(4d^2)$')
    for x,offset in [(1,(22,28)),(5,(-60,35))]:
        y=.5*(1-x/np.sqrt(x*x+1))
        ax.scatter([x],[y],color='#1476a5',s=32,zorder=5)
        ax.annotate(f'd/a = {x}\n{100*y:.3f}%',(x,y),xytext=offset,textcoords='offset points',
                    fontsize=10,arrowprops={'arrowstyle':'->','color':'#687784'})
    ax.axhline(.5,color='#8d969d',ls=':',lw=1.5)
    ax.text(.22,.507,'Hemisphere limit: 50%',fontsize=10)
    ax.set(xscale='log',xlim=(.2,12),ylim=(0,.55),xlabel=r'Axial distance / radius, $d/a$',
           ylabel=r'Fraction of isotropic emission, $\Omega/(4\pi)$',title='Acceptance saturates near the source')
    ax.set_xticks([.2,.5,1,2,5,10],labels=['0.2','0.5','1','2','5','10'])
    ax.grid(alpha=.18);ax.legend(loc='upper right',fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
