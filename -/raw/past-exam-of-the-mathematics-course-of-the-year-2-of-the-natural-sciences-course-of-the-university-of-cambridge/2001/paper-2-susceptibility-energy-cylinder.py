"""Degenerate susceptibility energy surface; Python 3.14, numpy 2.3, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    e0=np.array([1,-1,2])/np.sqrt(6)
    e1=np.array([-2,0,1])/np.sqrt(5)
    e6=np.array([1,5,2])/np.sqrt(30)
    t=np.linspace(0,2*np.pi,121)
    q0=np.linspace(-1.25,1.25,35)
    angle,axis=np.meshgrid(t,q0)
    points=axis[...,None]*e0+np.cos(angle)[...,None]*e1+np.sin(angle)[...,None]/np.sqrt(6)*e6
    fig=plt.figure(figsize=(9.5,4.9),dpi=120,layout='constrained')
    grid=fig.add_gridspec(1,2,width_ratios=[1.25,1])
    ax=fig.add_subplot(grid[0],projection='3d')
    ax.plot_surface(points[...,0],points[...,1],points[...,2],color='#3a89b3',alpha=.40,linewidth=0,antialiased=True)
    for pos in [-1.25,1.25]:
        ring=pos*e0+np.cos(t)[:,None]*e1+np.sin(t)[:,None]/np.sqrt(6)*e6
        ax.plot(*ring.T,color='#1b608a',lw=1.2)
    line=np.array([-1.65,1.65])[:,None]*e0
    ax.plot(*line.T,color='0.25',ls='--',lw=1.4)
    ax.text(*(1.55*e0),r'$e_0$',color='0.15')
    ax.set(xlabel=r'$H_1$',ylabel=r'$H_2$',zlabel=r'$H_3$',xlim=(-1.7,1.7),ylim=(-1.7,1.7),zlim=(-1.7,1.7),xticks=[-1,0,1],yticks=[-1,0,1],zticks=[-1,0,1],title=r'$\mathcal{E}=1$: an elliptic cylinder')
    ax.set_box_aspect((1,1,1))
    ax.view_init(elev=23,azim=-48)
    cross=fig.add_subplot(grid[1])
    cross.fill(np.cos(t),np.sin(t)/np.sqrt(6),color='#d7e9f3')
    cross.plot(np.cos(t),np.sin(t)/np.sqrt(6),color='#1b608a',lw=2)
    cross.axhline(0,color='0.7',lw=.8)
    cross.axvline(0,color='0.7',lw=.8)
    cross.annotate('',xy=(1,0),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':'#ae5b28','lw':1.5})
    cross.annotate('',xy=(0,1/np.sqrt(6)),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':'#ae5b28','lw':1.5})
    cross.text(.50,.06,'1',ha='center',color='#ae5b28')
    cross.text(.07,.24,r'$1/\sqrt{6}$',color='#ae5b28')
    cross.set(xlim=(-1.18,1.18),ylim=(-.7,.7),xlabel=r'$q_1$ (along $e_1$)',ylabel=r'$q_6$ (along $e_6$)',xticks=[-1,0,1],yticks=[-.5,0,.5],title=r'Cross-section: $q_1^2+6q_6^2=1$')
    cross.set_aspect('equal')
    cross.grid(alpha=.15)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
