"""Original flavour topology; Python 3.14, NumPy and Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def line(ax,a,b,label='',anti=False):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#24486a',lw=1.7)
    x=np.array(a)+.42*(np.array(b)-a);y=np.array(a)+.62*(np.array(b)-a)
    ax.add_patch(FancyArrowPatch(y if anti else x,x if anti else y,arrowstyle='-|>',mutation_scale=11,color='#24486a'))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.055,label,ha='center',fontsize=13)

def wave(ax,a,b,label):
    a,b=np.array(a),np.array(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d);t=np.linspace(0,1,220)
    z=a[None,:]+t[:,None]*d+.013*np.sin(14*np.pi*t)[:,None]*n
    ax.plot(z[:,0],z[:,1],color='#a34e24',lw=1.5);ax.text(*(a+b)/2+.04*n,label,fontsize=12,ha='center')

def main():
    fig,ax=plt.subplots(figsize=(8,4.3));ax.set(xlim=(-.02,1.45),ylim=(-.16,1.05));ax.axis('off')
    v=(.33,.78);w=(.55,.38)
    line(ax,(.02,.78),v,r'$c$');line(ax,v,(.91,.78),r'$q$')
    wave(ax,v,w,r'$W^{+*}$');line(ax,w,(.91,.48),r'$u$');line(ax,w,(.91,.24),r'$\bar q\,{}^\prime$',True)
    line(ax,(.02,.02),(.91,.02),r'$\bar u\ \mathrm{(spectator)}$',True)
    ax.text(1.01,.79,r'$q\bar u:$ negative meson',fontsize=11)
    ax.text(1.01,.43,r'$u\bar q\,{}^\prime:$ positive meson',fontsize=11)
    ax.text(.05,.98,r'External $W$ emission; time increases to the right',fontsize=13,weight='bold')
    ax.text(.05,-.12,r'$(q,q^\prime)=(s,d),(d,d),(s,s),(d,s)$ give the four channels.',fontsize=11)
    fig.tight_layout();fig.savefig('paper-1-charm-topology.png',dpi=160,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
