"""Original illustrative quark topologies, not a hadronic rate calculation."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def line(ax,a,b,label='',anti=False):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#24486a',lw=1.8)
    x=np.array(a)+.4*(np.array(b)-a);y=np.array(a)+.65*(np.array(b)-a)
    ax.add_patch(FancyArrowPatch(y if anti else x,x if anti else y,arrowstyle='-|>',mutation_scale=11,color='#24486a'))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.045,label,ha='center',fontsize=12)

def wave(ax,a,b,label):
    a,b=np.array(a),np.array(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d);t=np.linspace(0,1,190);z=a+t[:,None]*d+.012*np.sin(14*np.pi*t)[:,None]*n
    ax.plot(z[:,0],z[:,1],color='#a34e24',lw=1.4);ax.text(*((a+b)/2+.05*n),label,fontsize=12,ha='center')

def main():
    fig,axs=plt.subplots(1,3,figsize=(12,4.1))
    for ax in axs:ax.set(xlim=(-.05,1.05),ylim=(-.3,1.08));ax.axis('off')
    ax=axs[0];v=(.3,.78);w=(.5,.47)
    line(ax,(0,.78),v,'$s$');line(ax,v,(1,.78),'$u$');wave(ax,v,w,'$W^{-*}$');line(ax,w,(1,.58),r'$\bar u$',True);line(ax,w,(1,.25),'$d$')
    line(ax,(0,.12),(1,.12),'$u$');line(ax,(0,-.08),(1,-.08),'$s$')
    ax.set_title(r'Nonleptonic $\Xi^0$ decay',fontsize=12);ax.text(0,-.27,r'$\pi^0:\ u\bar u;\quad\Lambda:\ dus$',fontsize=12)
    ax=axs[1];a=(.32,.7);b=(.32,.2);k=(.68,.7)
    line(ax,(0,.7),a,'$s$');line(ax,a,k,'$u$');line(ax,k,(1,.7),'$u$');wave(ax,k,(.97,1),r'$\gamma$')
    line(ax,(0,.2),b,'$u$');line(ax,b,(1,.2),'$d$');wave(ax,a,b,'$W^{-*}$');line(ax,(0,-.08),(1,-.08),'$s$')
    ax.set_title(r'Weak radiative $\Xi^0$ decay',fontsize=12);ax.text(0,-.27,'One photon attachment shown',fontsize=10)
    ax=axs[2];v=(.5,.65)
    line(ax,(0,.65),v,'$q$');line(ax,v,(1,.65),'$q$');wave(ax,v,(.95,1),r'$\gamma$');line(ax,(0,.18),(1,.18),r'$\bar q$',True)
    ax.text(0,.42,r'$\eta^\prime$',fontsize=13);ax.text(.85,.42,r'$\rho^0$',fontsize=13)
    ax.set_title('Radiative meson transition',fontsize=12);ax.text(0,-.27,'Also emit from the antiquark',fontsize=10)
    fig.text(.5,.015,'Flavour-flow representatives; binding is implicit. Radiative amplitudes require all allowed attachments.',ha='center',fontsize=10)
    fig.tight_layout(rect=(0,.05,1,1));fig.savefig('paper-1-hyperon-and-rho.png',dpi=160,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
