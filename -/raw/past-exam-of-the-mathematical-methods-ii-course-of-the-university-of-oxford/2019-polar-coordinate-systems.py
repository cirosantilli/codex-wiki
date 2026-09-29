"""Original polar-coordinate sketches, Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.

The only generated file is the same-basename PNG in the caller's current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig=plt.figure(figsize=(10,4.8),dpi=120,facecolor='white')
    p=np.array([1.1,.9,1.4]);q=p.copy();q[2]=0
    phi=np.arctan2(p[1],p[0]);theta=np.arctan2(np.linalg.norm(q),p[2])
    for index in range(2):
        ax=fig.add_subplot(1,2,index+1,projection='3d')
        ax.set_facecolor('white')
        for j,label in enumerate(['x','y','z']):
            end=np.zeros(3);end[j]=2.25
            ax.quiver(0,0,0,*end,color='#71808c',arrow_length_ratio=.045,linewidth=1)
            ax.text(*(end*1.04),label,color='#334f60',fontsize=12)
        ax.plot([q[0],p[0]],[q[1],p[1]],[0,p[2]],ls='--',color='#8b969e',lw=1)
        ax.plot([p[0],p[0]],[0,p[1]],[0,0],ls=':',color='#a4adb4')
        ax.plot([0,p[0]],[p[1],p[1]],[0,0],ls=':',color='#a4adb4')
        ax.scatter(*p,s=30,color='#224f78');ax.scatter(*q,s=18,color='#8b969e')
        ax.text(*(p+np.array([.04,.04,.08])),'P',fontsize=12,color='#224f78')
        ax.text(*(q+np.array([.03,.04,-.13])),'Q',fontsize=11,color='#6b747d')
        a=np.linspace(0,phi,60);rphi=.62
        ax.plot(rphi*np.cos(a),rphi*np.sin(a),np.zeros_like(a),color='#9c5421',lw=1.5)
        ax.text(.73*np.cos(phi/2),.73*np.sin(phi/2),.02,r'$\phi$',fontsize=13,color='#9c5421')
        if index==0:
            ax.quiver(0,0,0,*q,color='#227b74',arrow_length_ratio=.06,linewidth=2)
            ax.quiver(*q,0,0,p[2],color='#9c5421',arrow_length_ratio=.06,linewidth=2)
            ax.text(q[0]*.74,q[1]*.74,.12,r'$s$',fontsize=13,color='#227b74')
            ax.text(q[0]+.08,q[1]+.08,p[2]*.53,r'$z$',fontsize=13,color='#9c5421')
            ax.set_title(r'Cylindrical: $(s,\phi,z)$',pad=10)
        else:
            ax.plot([0,q[0]],[0,q[1]],[0,0],color='#a4adb4',ls='--')
            ax.quiver(0,0,0,*p,color='#224f78',arrow_length_ratio=.045,linewidth=2)
            ax.text(*(p*.64+np.array([.05,-.12,.03])),r'$r$',fontsize=13,color='#224f78')
            a=np.linspace(0,theta,60);rad=.7
            ax.plot(rad*np.sin(a)*np.cos(phi),rad*np.sin(a)*np.sin(phi),rad*np.cos(a),color='#227b74',lw=1.6)
            ax.text(.84*np.sin(theta/2)*np.cos(phi),.84*np.sin(theta/2)*np.sin(phi),.84*np.cos(theta/2),r'$\theta$',fontsize=13,color='#227b74')
            ax.set_title(r'Spherical: $(r,\theta,\phi)$',pad=10)
        ax.set(xlim=(-.15,2.4),ylim=(-.15,2.4),zlim=(-.15,2.4))
        ax.set_box_aspect((1,1,1));ax.view_init(elev=22,azim=-55);ax.set_axis_off()
    fig.text(.5,.04,'Q is the horizontal projection of P; the polar angle θ is measured from positive z.',ha='center',fontsize=11,color='#334f60')
    fig.subplots_adjust(left=.01,right=.99,bottom=.1,top=.92,wspace=.02)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'codex-wiki polar coordinate sketch'})
    plt.close(fig)


if __name__=='__main__':
    main()
