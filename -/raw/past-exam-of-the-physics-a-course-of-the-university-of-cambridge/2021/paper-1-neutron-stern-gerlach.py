"""Original ideal neutron-beam schematic; Python 3.14/matplotlib 3.10.7.

Run from the mirrored _media directory; geometry is illustrative, not measured.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(9.0, 3.8), layout='constrained')
    ax.add_patch(Rectangle((.12, -.23), .65, .46, fc='#e8edf4', ec='#34495e'))
    ax.text(.45, -.42, 'neutron\nsource', ha='center', va='top')
    for x in [1.55, 2.25]:
        ax.plot([x,x], [.12,.6], color='0.25', lw=4)
        ax.plot([x,x], [-.6,-.12], color='0.25', lw=4)
    ax.text(1.9, -.78, 'collimating slits', ha='center')
    ax.add_patch(Polygon([(3, .95),(6,.60),(6,1.6),(3,1.6)], fc='#e7e7e7',ec='0.35'))
    ax.add_patch(Rectangle((3,-1.55),3,.75,fc='#e7e7e7',ec='0.35'))
    ax.text(4.5,1.32,'shaped magnet poles',ha='center',fontsize=10)
    ax.text(4.5,-1.33,r'$\partial B_z/\partial z\ne0$',ha='center',fontsize=12)
    ax.annotate('',xy=(4.45,.62),xytext=(4.45,-.5),arrowprops={'arrowstyle':'->','color':'0.5','lw':1.4})
    ax.text(4.62,.44,r'$\mathbf{B}$',color='0.35',fontsize=11)
    ax.plot([.77,3],[0,0],color='#34495e',lw=2)
    x=np.linspace(3,9.3,401)
    y=np.where(x<=6,.045*(x-3)**2,.405+.27*(x-6))
    for sign,color in [(1,'#236bc0'),(-1,'#c26712')]:
        ax.plot(x,sign*y,color=color,lw=2.3)
        ax.scatter([9.3],[sign*y[-1]],color=color,s=55,zorder=5)
    ax.add_patch(Rectangle((9.4,-1.55),.18,3.1,fc='#dcecd9',ec='#346536'))
    ax.text(9.5,1.78,'position-sensitive\nneutron detector',ha='center',va='bottom',fontsize=10)
    ax.text(7.1,1.12,r'$\mu_z=+|\mu_n|$',color='#236bc0',fontsize=11)
    ax.text(7.1,-1.26,r'$\mu_z=-|\mu_n|$',color='#c26712',fontsize=11)
    ax.annotate('',xy=(8.9,-1.7),xytext=(7,-1.7),arrowprops={'arrowstyle':'->','color':'0.4'})
    ax.text(7.95,-1.83,'beam direction',ha='center',color='0.35',fontsize=10)
    ax.annotate('',xy=(.5,1.5),xytext=(.5,.8),arrowprops={'arrowstyle':'->'})
    ax.text(.62,1.4,r'$z$',fontsize=12)
    ax.set(xlim=(-.05,10.7),ylim=(-2.05,2.18))
    ax.set_axis_off()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
