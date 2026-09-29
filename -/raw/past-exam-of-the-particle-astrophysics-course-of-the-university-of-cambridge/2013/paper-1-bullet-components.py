"""Original schematic, not a reconstruction of any observational image.

Python 3.14, numpy, matplotlib. Output basename to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


def main():
    fig, ax = plt.subplots(figsize=(9.5, 4.5), layout='constrained', facecolor='white')
    xx, yy = np.meshgrid(np.linspace(-4, 4, 360), np.linspace(-2, 2, 200))
    gas = np.exp(-((xx+.45)**2/1.1+(yy+.05)**2/.65)) + .65*np.exp(-((xx-.65)**2/.5+(yy-.1)**2/.3))
    mass = 1.2*np.exp(-((xx+2.1)**2/.65+yy**2/.7)) + .8*np.exp(-((xx-2.05)**2/.45+(yy-.05)**2/.45))
    ax.contourf(xx, yy, gas, levels=[.2,.45,.75,1.1,1.6], colors=['#fff2e8','#ffd7ba','#ffa675','#ee7958'], alpha=.9)
    ax.contour(xx, yy, mass, levels=[.2,.4,.6,.8,1.0], colors=['#2166ac'], linewidths=1.4)
    offsets=np.array([[-.3,.2],[.25,.3],[.1,-.35],[-.18,-.12],[.45,-.12],[-.25,-.5]])
    for cx in [-2.1,2.05]:
        ax.scatter(cx+offsets[:,0],offsets[:,1],marker='*',s=55,c='#252525',zorder=4)
    for x0,x1 in [(-2.1,-3.2),(2.05,3.15)]:
        ax.annotate('',(x1,1.2),(x0,1.2),arrowprops={'arrowstyle':'-|>','lw':2,'color':'#2166ac'})
    ax.text(0,1.48,'Galaxies and dominant lensing mass continue outward',ha='center',fontsize=11)
    ax.annotate('Slower hot gas',(.15,.22),(.15,-1.25),ha='center',fontsize=11,
                arrowprops={'arrowstyle':'->','color':'#b64029'},color='#9f3e2e')
    ax.legend(handles=[Line2D([0],[0],color='#2166ac',label='Projected mass: lensing contours'),
                       Line2D([0],[0],marker='*',ls='none',color='#252525',markersize=9,label='Galaxies: optical light'),
                       Patch(facecolor='#ffa675',label='Hot gas: X-rays')],loc='lower center',bbox_to_anchor=(.5,-.06),ncol=3,frameon=False,fontsize=9)
    ax.set(xlim=(-3.8,3.8),ylim=(-1.65,1.8),aspect='equal',title='Illustrative post-collision geometry — not measured positions')
    ax.axis('off')
    fig.savefig('paper-1-bullet-components.png',dpi=170,facecolor='white')
    plt.close(fig)

if __name__=='__main__':
    main()
