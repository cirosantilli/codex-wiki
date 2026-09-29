"""Original exact radial-coverage model, sigma=2 cm; output PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10.8,4.9),layout='constrained')
    sigma=2.0;r95=sigma*np.sqrt(-2*np.log(.05))
    disks=[(r95,'#ebac36',.12),(4,'#338ea1',.13),(2,'#4767a7',.18)]
    for r,color,alpha in disks:
        ax.add_patch(Circle((0,0),r,fc=color,alpha=alpha,ec='none'))
        ax.add_patch(Circle((0,0),r,fc='none',ec=color,lw=2))
    ax.plot(0,0,'+',ms=12,mew=2,color='#293746')
    ax.text(.18,.15,'Intended point',fontsize=10,color='#293746')
    for r,label,color,angle in [(2,'39.35%', '#4767a7',-65),(4,'86.47%','#197a8d',145),(r95,'95.00%','#aa7014',45)]:
        theta=np.deg2rad(angle)
        ax.text(r*np.cos(theta),r*np.sin(theta),label,fontsize=11,ha='center',va='center',
                color=color,bbox={'fc':'white','ec':'none','alpha':.85,'pad':2})
    ax.axhline(0,color='#a1aab3',lw=.7,zorder=0);ax.axvline(0,color='#a1aab3',lw=.7,zorder=0)
    ax.set(xlim=(-5.6,5.6),ylim=(-5.6,5.6),aspect='equal',xlabel='Horizontal error (cm)',ylabel='Vertical error (cm)',
           title=r'Chosen model: each coordinate has $\sigma=2$ cm')
    r=np.linspace(0,7,600);cdf=-np.expm1(-r*r/(2*sigma*sigma))
    bx.plot(r,cdf,lw=2.7,color='#245988')
    for rad,label,color in [(2,'1 component SD','#4767a7'),(4,'2 component SD','#197a8d'),(r95,'95% radius','#aa7014')]:
        p=-np.expm1(-rad*rad/(2*sigma*sigma))
        bx.plot([rad,rad],[0,p],ls='--',lw=1.2,color=color)
        bx.scatter([rad],[p],color=color,zorder=5,s=45)
    bx.annotate('95% threshold\n4.8955 cm',(r95,.95),xytext=(3.0,.56),fontsize=11,
                arrowprops={'arrowstyle':'->','color':'#aa7014'},color='#996410')
    bx.text(.2,.86,r'$F_R(r)=1-e^{-r^2/(2\sigma^2)}$',fontsize=14)
    bx.text(.2,.75,'Computed coverage, not measured counts',fontsize=10)
    bx.set(xlim=(0,7),ylim=(0,1.04),xlabel='Disk radius r (cm)',ylabel='Probability inside disk',
           title='A 1-SD disk contains only about 39%')
    bx.grid(alpha=.17)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
