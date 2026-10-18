"""Original Mohr tangency and lower-hemisphere reverse double couple.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; basename PNG to CWD.
Compression positive; arbitrary stress scale, zero cohesion and pore pressure.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({'font.size':10})
    fig,axes=plt.subplots(1,3,figsize=(11.5,4.3),layout='constrained')
    phi=np.arctan(.5);delta=np.pi/4-phi/2
    C=1.;R=np.sin(phi);a=np.linspace(0,2*np.pi,721)
    ax=axes[0];ax.plot(C+R*np.cos(a),R*np.sin(a),color='#175b89')
    s=np.linspace(0,1.65,100);ax.plot(s,.5*s,'k--');ax.plot(s,-.5*s,'k--')
    sn=C*np.cos(phi)**2;tau=.5*sn
    ax.plot([C,sn],[0,tau],color='#a42f21');ax.plot(sn,tau,'o',color='#a42f21')
    ax.axhline(0,color='0.5',lw=.7)
    ax.text(.03,.95,'|τ| = 0.5 σ′ₙ\n2θ = 90° + φ = 116.565°',transform=ax.transAxes,va='top',fontsize=9)
    ax.text(C-R,-.12,'σ′₃',ha='center');ax.text(C+R,-.12,'σ′₁',ha='center')
    ax.set(xlim=(0,1.7),ylim=(-.8,.8),xlabel='Effective normal stress σ′ₙ',ylabel='Shear stress τ',title='Tangency at first failure');ax.set_aspect('equal')
    ax=axes[1]
    for sign in (-1,1): ax.plot([-1,1],sign*np.tan(delta)*np.array([-1,1]),color='#a42f21',lw=2)
    for aa,bb in [((-1.5,0),(-1,0)),((1.5,0),(1,0)),((0,-1.2),(0,-.85)),((0,1.2),(0,.85))]:
        ax.annotate('',xy=bb,xytext=aa,arrowprops={'arrowstyle':'->'})
    ax.text(-1.55,.25,'N');ax.text(1.5,.25,'S');ax.text(-.8,1.18,'σ₃ vertical; σ₂ E-W')
    ax.text(-1.55,-1.55,'σ₁ horizontal N-S\nConjugate fault dips = 31.72°')
    ax.set(xlim=(-1.8,1.8),ylim=(-1.7,1.6),title='Ideal new thrust faults');ax.set_aspect('equal');ax.axis('off')
    ax=axes[2];q=np.linspace(-1,1,501);xx,yy=np.meshgrid(q,q);rr=np.sqrt(xx*xx+yy*yy)
    takeoff=2*np.arcsin(np.minimum(rr,1)/np.sqrt(2));az=np.arctan2(xx,yy)
    rays=np.array([np.sin(takeoff)*np.sin(az),np.sin(takeoff)*np.cos(az),np.cos(takeoff)])
    # Coordinates east,north,down. E-W strike, south-dipping plane, up-dip slip.
    n=np.array([0,np.sin(delta),np.cos(delta)]);slip=np.array([0,np.cos(delta),-np.sin(delta)])
    M=-(np.outer(slip,n)+np.outer(n,slip))
    radiation=np.einsum('iab,ij,jab->ab',rays,M,rays);radiation=np.ma.masked_where(rr>1,radiation)
    ax.contourf(xx,yy,radiation,levels=[-2,0,2],colors=['white','#283f54'])
    ax.contour(xx,yy,radiation,levels=[0],colors='black',linewidths=.9)
    ax.add_patch(Circle((0,0),1,fill=False,color='black'))
    ax.text(0,1.08,'N',ha='center');ax.text(1.1,0,'E')
    ax.text(0,-1.34,'Dark = P-wave compression\nLower hemisphere; equal area',ha='center',fontsize=9)
    ax.set(xlim=(-1.2,1.3),ylim=(-1.55,1.2),title='Plausible thrust focal mechanism');ax.set_aspect('equal');ax.axis('off')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
