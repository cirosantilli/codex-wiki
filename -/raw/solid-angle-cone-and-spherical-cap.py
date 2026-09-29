"""Draw two views of a cone's direction set; output basename.png in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    theta = np.pi / 4
    fig = plt.figure(figsize=(10.4, 4.9), layout='constrained')
    ax = fig.add_subplot(121)
    ax.set_aspect('equal')
    t = np.linspace(0, 2*np.pi, 500)
    for radius, color in [(1, '#9ba8b0'), (1.65, '#ccd2d6')]:
        ax.plot(radius*np.cos(t), radius*np.sin(t), color=color, lw=1.2)
        cap = np.linspace(np.pi/2-theta, np.pi/2+theta, 150)
        ax.plot(radius*np.cos(cap), radius*np.sin(cap), color='#126fa1', lw=5)
    for sign in [-1, 1]:
        ax.plot([0, sign*1.8*np.sin(theta)], [0, 1.8*np.cos(theta)], color='#ef8b29', lw=2)
    ax.plot([0,0], [0,1.85], color='#586571', ls=':', lw=1.4)
    ax.add_patch(Arc((0,0), .9,.9, theta1=45, theta2=90, color='#222222', lw=1.5))
    ax.text(.13,.49,r'$\theta=45^\circ$', fontsize=11)
    ax.scatter([0],[0],color='#111111',s=20,zorder=5)
    ax.text(-.12,-.18,'O')
    ax.annotate(r'$R$', (.98,0), (.70,-.35), arrowprops={'arrowstyle':'->','color':'#697983'})
    ax.annotate(r'$1.65R$', (1.63,-.06), (1.00,-.75), arrowprops={'arrowstyle':'->','color':'#697983'})
    ax.text(-1.77,1.83,'Same directions on both spheres', fontsize=12, weight='bold')
    ax.text(-1.77,-1.95,r'Cap area scales as $R^2$; $\Omega=A/R^2$ stays fixed.', fontsize=11)
    ax.text(-1.77,-2.25,'Meridian section: rotate the blue arcs about the dotted axis.', fontsize=10)
    ax.set_xlim(-1.9,1.9); ax.set_ylim(-2.4,2.05); ax.axis('off')

    ax3 = fig.add_subplot(122, projection='3d')
    ph = np.linspace(0,2*np.pi,60)
    polar = np.linspace(0,np.pi,25)
    pp,tt = np.meshgrid(ph,polar)
    ax3.plot_wireframe(np.sin(tt)*np.cos(pp),np.sin(tt)*np.sin(pp),np.cos(tt),
                       color='#aebac1', alpha=.36, linewidth=.45,rstride=2,cstride=4)
    pc,tc = np.meshgrid(ph,np.linspace(0,theta,24))
    ax3.plot_surface(np.sin(tc)*np.cos(pc),np.sin(tc)*np.sin(pc),np.cos(tc),
                     color='#218dc0',alpha=.94,linewidth=0,shade=True)
    ax3.plot(np.sin(theta)*np.cos(ph),np.sin(theta)*np.sin(ph),np.full_like(ph,np.cos(theta)),
              color='#0a537e', lw=2)
    for az in [0,np.pi/2,np.pi,3*np.pi/2]:
        ax3.plot([0,np.sin(theta)*np.cos(az)],[0,np.sin(theta)*np.sin(az)],
                   [0,np.cos(theta)],color='#ed8c2c',lw=1.7)
    ax3.scatter([0],[0],[0],color='black',s=18)
    ax3.text(0,0,-.12,'O')
    ax3.set_box_aspect((1,1,1)); ax3.set_axis_off(); ax3.view_init(elev=20,azim=30)
    ax3.set_title('The cap is a surface patch, not the filled cone',fontsize=12,pad=8)
    ax3.text2D(.06,.00,r'$\Omega=2\pi(1-\cos45^\circ)=1.8403\ \mathrm{sr}$',transform=ax3.transAxes,fontsize=12)
    ax3.text2D(.06,-.08,r'$\Omega/(4\pi)=0.1464$: about 14.64% of all directions',transform=ax3.transAxes,fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
