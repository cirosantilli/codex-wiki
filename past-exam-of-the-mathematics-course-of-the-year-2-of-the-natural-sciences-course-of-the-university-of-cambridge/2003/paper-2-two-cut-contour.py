"""Original positively oriented contour for the two exterior square-root cuts."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(7.1,6.0),dpi=120,layout='constrained')
    radius=3.0;eps=.12
    cutoff=np.arcsin(eps/radius)
    endpoint=np.sqrt(radius*radius-eps*eps)
    blue='#227ca6';orange='#bc682a'
    for low,high in [(cutoff,np.pi-cutoff),(np.pi+cutoff,2*np.pi-cutoff)]:
        theta=np.linspace(low,high,900)
        ax.plot(radius*np.cos(theta),radius*np.sin(theta),color=blue,lw=1.6)
    for sign in [-1,1]:
        ax.plot([sign,sign*endpoint],[eps,eps],color=blue,lw=1.6)
        ax.plot([sign,sign*endpoint],[-eps,-eps],color=blue,lw=1.6)
        ax.plot([sign,sign*3.26],[0,0],color=orange,lw=2.3)
        ax.scatter([sign],[0],color=orange,s=28,zorder=6)
    for center,angles in [(1,np.linspace(-np.pi/2,-3*np.pi/2,150)),(-1,np.linspace(np.pi/2,-np.pi/2,150))]:
        ax.plot(center+eps*np.cos(angles),eps*np.sin(angles),color=blue,lw=1.6)
    for start,end in [((1.45,eps),(2.02,eps)),((2.02,-eps),(1.45,-eps)),((-2.02,eps),(-1.45,eps)),((-1.45,-eps),(-2.02,-eps))]:
        ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':blue,'lw':1.7})
    for angle in [1.3,4.45]:
        ax.annotate('',xy=(radius*np.cos(angle+.12),radius*np.sin(angle+.12)),xytext=(radius*np.cos(angle-.12),radius*np.sin(angle-.12)),arrowprops={'arrowstyle':'->','color':blue,'lw':1.7})
    ax.scatter([0],[0],marker='x',color='#842b58',s=45,zorder=7)
    ax.annotate('Simple pole\nresidue 1',xy=(0,0),xytext=(.28,-1.0),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
    ax.text(-2.35,.68,r'Left lips: $2iI_R$',ha='center',fontsize=10)
    ax.text(2.05,.68,r'Right lips: $2iI_R$',ha='center',fontsize=10)
    ax.text(-1,-.43,r'$-1$',ha='center')
    ax.text(1,-.43,r'$1$',ha='center')
    ax.text(0,2.5,'Outer arc: counterclockwise',ha='center',color=blue,fontsize=10)
    ax.axhline(0,color='0.7',lw=.7,zorder=0)
    ax.axvline(0,color='0.7',lw=.7,zorder=0)
    ax.set(xlim=(-3.42,3.42),ylim=(-3.37,3.37),xticks=[-3,-1,0,1,3],yticks=[-3,-1,0,1,3],xlabel='Re(z)',ylabel='Im(z)',title=r'Two-cut contour for $1/(z\sqrt{1-z^2})$')
    ax.set_aspect('equal')
    ax.grid(alpha=.12)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
