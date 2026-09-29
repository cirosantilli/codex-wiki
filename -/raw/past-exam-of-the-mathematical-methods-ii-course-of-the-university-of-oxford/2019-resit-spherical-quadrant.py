"""Original spherical-patch geometry; Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.

Write only the same-basename PNG in the caller's working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig=plt.figure(figsize=(6.3,5.3),dpi=120,facecolor='white')
    ax=fig.add_subplot(projection='3d');ax.set_facecolor('white')
    theta=np.linspace(np.pi/2,np.pi,45);phi=np.linspace(np.pi,2*np.pi,65)
    th,ph=np.meshgrid(theta,phi)
    ax.plot_surface(4*np.sin(th)*np.cos(ph),4*np.sin(th)*np.sin(ph),4*np.cos(th),
                    color='#2d7bb3',alpha=.78,linewidth=0,antialiased=True,shade=True)
    rad=np.linspace(0,4,22);ang=np.linspace(np.pi,2*np.pi,65);rr,aa=np.meshgrid(rad,ang)
    ax.plot_surface(rr*np.cos(aa),np.zeros_like(rr),rr*np.sin(aa),color='#d7b892',alpha=.24,linewidth=0,shade=False)
    ax.plot_surface(rr*np.cos(aa),rr*np.sin(aa),np.zeros_like(rr),color='#b7c9c5',alpha=.22,linewidth=0,shade=False)
    ax.plot(4*np.cos(ang),np.zeros_like(ang),4*np.sin(ang),color='#9e7445',lw=1.5)
    ax.plot(4*np.cos(ang),4*np.sin(ang),np.zeros_like(ang),color='#527e79',lw=1.5)
    ax.plot([4,-4],[0,0],[0,0],color='#8a959d',lw=.9)
    for j,label in enumerate(['x','y','z']):
        end=np.zeros(3);end[j]=5 if j==0 else 2.1
        ax.quiver(0,0,0,*end,color='#5d6f7d',arrow_length_ratio=.07,linewidth=1)
        ax.text(*(end*1.08),label,color='#334e61',fontsize=12)
    ax.text(-2.5,-2.35,-2.1,'S',fontsize=17,color='white')
    ax.text(0,.08,-2.2,r'$D_y$',color='#86613c',fontsize=13,bbox={'facecolor':'white','edgecolor':'none','alpha':.8,'pad':1})
    ax.text(0,-2.2,.1,r'$D_z$',color='#436e68',fontsize=13)
    ax.quiver(0,0,-2.4,0,1,0,color='#86613c',arrow_length_ratio=.22,linewidth=1.5)
    ax.quiver(0,-2.4,0,0,0,1,color='#436e68',arrow_length_ratio=.22,linewidth=1.5)
    ax.set(xlim=(-4.8,5.5),ylim=(-4.8,2.7),zlim=(-4.8,2.7))
    ax.set_box_aspect((1.3,1,1),zoom=1.5);ax.view_init(elev=20,azim=-58);ax.set_axis_off()
    ax.set_title(r'Spherical patch: $R=4$, $y\leq0$, $z\leq0$',pad=12,fontsize=14)
    fig.text(.5,.035,'Blue: curved surface. Pale half-discs: auxiliary caps. Cap normals point toward +y and +z.',ha='center',fontsize=9,color='#3b5567')
    fig.subplots_adjust(left=.01,right=.99,bottom=.08,top=.9)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'codex-wiki spherical quadrant'})
    plt.close(fig)


if __name__=='__main__':
    main()
