"""Bloch-ball mixtures and the Pauli-state octahedron; output PNG to cwd."""
from pathlib import Path
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def setup(ax):
    u=np.linspace(0,2*np.pi,33);v=np.linspace(0,np.pi,17)
    ax.plot_wireframe(np.outer(np.cos(u),np.sin(v)),np.outer(np.sin(u),np.sin(v)),np.outer(np.ones_like(u),np.cos(v)),color='#b7bec5',linewidth=.45,alpha=.48)
    for j,label in enumerate(['x','y','z']):
        end=np.zeros(3);end[j]=1.19
        ax.plot(*np.array([-end,end]).T,color='#777777',linewidth=.7)
        # Vertex and state labels below identify the directions.
    ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),zlim=(-1.25,1.25))
    ax.set_box_aspect((1,1,1),zoom=1.55);ax.set_proj_type('ortho');ax.set_axis_off();ax.view_init(20,-45)


def main():
    plt.rcParams.update({'font.size':12,'savefig.facecolor':'white'})
    fig=plt.figure(figsize=(10.2,4.8),layout='constrained');left=fig.add_subplot(121,projection='3d');right=fig.add_subplot(122,projection='3d')
    for ax in [left,right]:setup(ax)
    left.plot([0,0],[0,0],[-1,1],color='#b23a33',linewidth=4)
    left.scatter([0,0],[0,0],[-1,1],color='#b23a33',s=45,depthshade=False)
    left.scatter([0],[0],[.4],color='#222222',s=35,depthshade=False)
    left.text(.08,.05,1.08,r'$|0\rangle$',fontsize=12);left.text(.08,.05,-1.15,r'$|1\rangle$',fontsize=12)
    left.text(.3,.15,.45,r'$p_0=0.7$',fontsize=11)
    left.set_title('All standard-basis mixtures')
    vertices=[];labels=[r'$+X$',r'$-X$',r'$+Y$',r'$-Y$',r'$+Z$',r'$-Z$']
    for j in range(3):
        for sign in [1,-1]:
            point=np.zeros(3);point[j]=sign;vertices.append(point)
    vertices=np.array(vertices)
    faces=[]
    for signs in itertools.product([0,1],repeat=3):faces.append(vertices[[signs[0],2+signs[1],4+signs[2]]])
    right.add_collection3d(Poly3DCollection(faces,facecolors='#2878a8',edgecolors='#12537d',linewidth=.8,alpha=.25))
    right.scatter(*vertices.T,color='#12537d',s=28,depthshade=False)
    for pt,label in zip(vertices,labels):right.text(*(pt*1.12),label,fontsize=11,color='#154c71')
    magic=np.array([1/np.sqrt(2),1/np.sqrt(2),0]);right.scatter(*magic,color='#d58c12',s=60,depthshade=False)
    right.text2D(.42,.02,'Gold: T-gate resource',transform=right.transAxes,fontsize=10,color='#8a5600')
    right.set_title('Pauli mixtures form an octahedron')
    fig.savefig(Path.cwd()/'2021-bloch-mixtures.png',dpi=100,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
