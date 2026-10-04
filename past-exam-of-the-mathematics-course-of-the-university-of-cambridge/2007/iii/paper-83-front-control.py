"""Original gravity-current nose sketch; Python 3.14 with root dependencies.

Write the PNG basename to caller CWD, respecting MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np


def main():
    fig,(ax,section)=plt.subplots(1,2,figsize=(8.,3.6),dpi=130,
                                 gridspec_kw={'width_ratios':[1.65,1]},facecolor='white')
    x=np.linspace(-2,0,200)
    h=np.where(x<-.35,1.,np.sqrt(np.maximum(0,1-(x+.35)**2/.35**2)))
    ax.fill_between(x,0,h,color='#c7e0f1')
    ax.plot(x,h,color='#176dab',lw=2)
    ax.plot([-2.2,1.9],[0,0],color='#4d5963',lw=2)
    ax.add_patch(Rectangle((-1.5,.05),3.,1.85,fill=False,ls='--',lw=1,color='#707b85'))
    ax.annotate('',xy=(-.1,1.55),xytext=(1.3,1.55),arrowprops={'arrowstyle':'->','color':'#495b6a'})
    ax.text(.5,1.7,r'Ambient: $-u_f$',ha='center',fontsize=10)
    ax.annotate('',xy=(-1.4,1.35),xytext=(-.45,1.35),arrowprops={'arrowstyle':'->','color':'#495b6a'})
    ax.text(-1.2,1.1,'Return flow',fontsize=9)
    ax.text(-1.2,.38,r'Dense layer: $u-u_f=0$',fontsize=9)
    ax.annotate('',xy=(-1.8,1.),xytext=(-1.8,0),arrowprops={'arrowstyle':'<->','color':'#333e48'})
    ax.text(-2.08,.48,r'$h_f$',fontsize=11)
    ax.text(.42,.2,'Nose',fontsize=10)
    ax.text(-1.5,2.02,'Nose-fixed control volume',fontsize=11)
    ax.set(xlim=(-2.25,1.9),ylim=(-.1,2.2))
    ax.set_axis_off()
    k=.65;level=1.
    section.add_patch(Polygon([[-k*level,level],[k*level,level],[0,0]],facecolor='#c7e0f1',edgecolor='none'))
    section.plot([-k*1.6,0,k*1.6],[1.6,0,1.6],color='#4d5963',lw=2)
    section.plot([-k*level,k*level],[level,level],color='#176dab',lw=2)
    section.text(0,.5,r'$\rho_1$',ha='center',fontsize=12)
    section.text(0,1.3,r'$\rho_2$',ha='center',fontsize=12)
    section.text(0,-.28,r'$A(h)=kh^2$',ha='center',fontsize=11)
    section.set(xlim=(-1.2,1.2),ylim=(-.35,1.8),title='Triangular cross-section')
    section.set_aspect('equal');section.set_axis_off()
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-83-front-control.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
