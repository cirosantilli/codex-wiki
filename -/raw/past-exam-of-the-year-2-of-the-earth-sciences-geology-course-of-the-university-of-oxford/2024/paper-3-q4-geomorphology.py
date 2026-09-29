"""Original normal-fault geomorphology sketches, not copies of exam figures.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; opaque basename PNG to CWD.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    plt.rcParams.update({'font.size':10})
    fig,axes=plt.subplots(2,2,figsize=(10.5,6.9),layout='constrained')
    ax=axes[0,0]
    ax.fill_between([-3,0,.7,3],[-.2,.6,-.6,-.3],-1.8,color='#e7d8bd')
    ax.plot([-3,0,.7,3],[-.2,.6,-.6,-.3],'k',lw=2)
    ax.plot([0,1.5],[.6,-1.8],color='#a42f21',lw=2)
    ax.annotate('',xy=(1,-.9),xytext=(.65,-.35),arrowprops={'arrowstyle':'->','lw':2})
    ax.text(-2.8,.9,'Footwall relief');ax.text(1.2,.15,'Hanging-wall basin')
    ax.text(-2.8,-1.5,'Throw = slip × sin(dip)\nHeave = slip × cos(dip)')
    ax.set(title='Slip rate, dip, segmentation and surface slope',xlim=(-3.2,3.2),ylim=(-1.9,1.5));ax.axis('off')
    ax=axes[0,1];x=np.linspace(-3,3,601)
    for width,label,color in [(.08,'Fresh step','#a42f21'),(.45,'Younger scarp','#175b89'),(1.05,'Older / more diffused','#60723d')]:
        y=-.65*np.array([math.erf(a/width) for a in x]);ax.plot(x,y,color=color,label=label)
    ax.set(title='Weathering and hillslope transport round scarps',xlabel='Across fault (relative distance)',ylabel='Relative height');ax.legend(fontsize=8)
    ax=axes[1,0]
    ax.plot([0,0],[0,4],'#a42f21',lw=2)
    for y in (.5,1.7,2.9):
        ax.add_patch(Polygon([(-1.9,y+.45),(0,y),(0,y+.9)],facecolor='#d4d8c0',edgecolor='0.4'))
        ax.plot([-2.1,-.3,.7,2],[y+.45,y+.45,y+.1,y-.05],color='#175b89',lw=1.4)
        ax.plot([.2,1.1,1.8],[y-.1,y+.15,y+.4],color='#ae854d',lw=1)
    ax.text(-2.2,4.1,'Mountain front (plan view)');ax.text(-2.6,-.25,'Faceted spurs');ax.text(.3,4.1,'Fan deposition')
    ax.text(.3,-.25,'Deflected streams; fan / terrace offsets')
    ax.set(xlim=(-2.7,3.1),ylim=(-.55,4.5),title='Drainage incises the footwall; fans fill the basin');ax.axis('off')
    ax=axes[1,1]
    ax.fill_between([-3,0,.4,3],[.6,.6,-.5,-.5],-1.4,color='#e7d8bd')
    ax.plot([-3,0,.4,3],[.6,.6,-.5,-.5],color='0.4',ls='--')
    ax.fill_between([0,.4,3],[.7,.6,.1],[.6,-.5,-.5],color='#e4bd80')
    ax.plot([-3,0,.4,3],[.6,.7,.6,.1],'k',lw=2)
    ax.text(.6,.8,'Aggradation buries relief');ax.text(-2.9,-1.1,'A subdued scarp can conceal an active fault')
    ax.set(xlim=(-3.2,3.2),ylim=(-1.5,1.4),title='Climate, material strength, sediment supply');ax.axis('off')
    fig.suptitle('Active normal faults: landforms reflect both deformation and surface processes')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
