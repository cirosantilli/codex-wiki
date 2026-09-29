"""Original cap/wall/base sketches. Python 3.14; NumPy 2.3.5,
Matplotlib 3.10.7. Outputs paper-3-closed-surface.png to CWD only;
preserves any MPLCONFIGDIR supplied by the caller.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig=plt.figure(figsize=(8.0,7.0),dpi=130,facecolor='white')
    theta=np.linspace(0,2*np.pi,70);radius=np.linspace(0,1,25)
    tt,rr=np.meshgrid(theta,radius);xx=rr*np.cos(tt);yy=rr*np.sin(tt)
    tw,zz=np.meshgrid(theta,np.linspace(0,1,18))
    panels=[('cap',r'$S_1$: paraboloid cap'),('wall',r'$S_2$: cylindrical wall'),('base',r'$S_3$: base disk'),('all',r'$S=S_1\cup S_2\cup S_3$')]
    for i,(kind,title) in enumerate(panels,1):
        ax=fig.add_subplot(2,2,i,projection='3d')
        if kind in ('cap','all'):
            ax.plot_surface(xx,yy,3-2*rr**2,color='#6092bd',alpha=0.86,linewidth=0,shade=True)
        if kind in ('wall','all'):
            ax.plot_surface(np.cos(tw),np.sin(tw),zz,color='#da985f',alpha=0.82,linewidth=0,shade=True)
        if kind in ('base','all'):
            ax.plot_surface(xx,yy,np.zeros_like(xx),color='#6d9f83',alpha=0.85,linewidth=0,shade=True)
        ax.plot(np.cos(theta),np.sin(theta),np.zeros_like(theta) if kind=='base' else np.ones_like(theta),color='0.25',lw=0.8)
        ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),zlim=(0,3.2),xlabel='$x$',ylabel='$y$',zlabel='$z$')
        ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_zticks([0,1,3]);ax.set_box_aspect((2,2,3));ax.view_init(elev=22,azim=-55)
        ax.set_title(title,fontsize=10,pad=2);ax.tick_params(labelsize=8,pad=0)
    fig.subplots_adjust(left=0.01,right=0.94,bottom=0.08,top=0.95,wspace=0.0,hspace=0.28)
    fig.savefig('paper-3-closed-surface.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
