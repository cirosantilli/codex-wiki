"""Original atom-mapped ring transformations; Python 3.14/numpy/matplotlib.

Outputs only its PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt

BLUE='#24659a'; ORANGE='#b66a21'; GREEN='#28794b'

def line(ax,a,b,order=1,color='#555',ls='-'):
    a=np.array(a,float);b=np.array(b,float)
    v=b-a;v/=np.linalg.norm(v)
    off=np.array([-v[1],v[0]])*.045
    for d in ([0] if order==1 else [-1,1]):
        u=a+d*off;w=b+d*off
        ax.plot([u[0],w[0]],[u[1],w[1]],color=color,lw=1.6,ls=ls,zorder=1)

def atom(ax,p,label,color=BLUE):
    ax.text(*p,label,ha='center',va='center',fontsize=12,color=color,
            bbox={'facecolor':'white','edgecolor':'none','pad':1},zorder=4)

def polygon(n):
    theta=np.arange(n)*2*np.pi/n+np.pi/2
    return np.column_stack([np.cos(theta),np.sin(theta)])

def skeleton(ax,pts,labels,orders=None):
    orders=orders or {}
    for i in range(len(pts)):line(ax,pts[i],pts[(i+1)%len(pts)],orders.get(i,1))
    for p,l in zip(pts,labels):atom(ax,p,l)

def title(ax,heading,foot):
    ax.set_title(heading,fontsize=11,pad=15)
    ax.text(.5,-.04,foot,ha='center',va='top',fontsize=9,transform=ax.transAxes)
    ax.set(xlim=(-2.2,2.2),ylim=(-1.8,1.9));ax.set_aspect('equal');ax.axis('off')

def draw():
    fig,axs=plt.subplots(2,3,figsize=(13,8.5),layout='constrained')
    p=polygon(6)
    a=axs[0,0];skeleton(a,p,list('ABCDEF'),{5:2})
    for i in [0,5]:
        q=p[i]+np.array([-.25 if i==5 else .25,.55]);line(a,p[i],q);atom(a,q,'Me',ORANGE)
    for i in [2,3]:
        q=p[i]+np.array([0,-.55]);line(a,p[i],q,ls='--');atom(a,q,'CN',GREEN)
    title(a,'Q8: stereospecific cycloaddition','A=F derives from the diene; C–CN and D–CN are cis')
    a=axs[0,1]
    x=np.linspace(-1.9,1.9,6);pts=np.column_stack([x,np.array([.2,-.15,.2,-.15,.2,-.15])])
    for i in range(5):line(a,pts[i],pts[i+1])
    for i,p0 in enumerate(pts):atom(a,p0,list('ABCDEF')[i])
    for i in [0,5]:atom(a,pts[i]+[0,.7],'O=C–Me',ORANGE)
    for i in [2,3]:line(a,pts[i],pts[i]+[0,-.65],ls='--');atom(a,pts[i]+[0,-.75],'CN',GREEN)
    a.annotate('',pts[5]+[0,.2],pts[1]+[0,.2],arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=-.65','color':BLUE,'lw':1.6})
    title(a,'Q8: open A=F by reductive ozonolysis','B enolate attacks carbonyl F: form the B–F bond')
    a=axs[0,2];p5=polygon(5);skeleton(a,p5,list('BCDEF'),{4:2})
    for i in [1,2]:
        q=p5[i]+np.array([-.55 if i==1 else -.15,-.45]);line(a,p5[i],q,ls='--');atom(a,q,'CN',GREEN)
    q=p5[0]+[.1,.65];line(a,p5[0],q);atom(a,q,'C(A)(=O)Me',ORANGE)
    q=p5[4]+[.65,.35];line(a,p5[4],q);atom(a,q,'Me',ORANGE)
    title(a,'Q8: dehydration gives B=F','A remains in the acetyl group; no carbon is discarded')
    # The five lowercase atoms are the retained original cyclopentadiene ring.
    pr=polygon(5)*.95
    for col in [0,1]:
        a=axs[1,col];skeleton(a,pr,list('abcde'))
        pa=pr[0];pd=pr[3]
        f=np.array([1.35,.75]);g=np.array([1.25,-.6])
        if col==0:
            line(a,pa,f);line(a,f,g);line(a,g,pd)
            atom(a,f,'f: C=O',ORANGE);atom(a,g,'g: CH₂',ORANGE)
            title(a,'Q12(b): ketone after Nef reaction and H₂','The a–f–g–d bridge lies on one face of ring abcde')
        else:
            o=np.array([.8,1.45])
            line(a,pa,o);line(a,o,f);line(a,f,g);line(a,g,pd)
            atom(a,o,'O',GREEN);atom(a,f,'f: C=O',ORANGE);atom(a,g,'g: CH₂',ORANGE)
            title(a,'Q12(b): Baeyer–Villiger insertion at a–f','O enters the bridge; the five-carbon ring survives')
    a=axs[1,2];skeleton(a,pr,list('abcde'))
    q=pr[0]+[.55,.6];line(a,pr[0],q,ls='--');atom(a,q,'OH',GREEN)
    q=pr[3]+[1.15,-.15];line(a,pr[3],q,ls='--');atom(a,q,'g: CH₂–f: CHO',ORANGE)
    a.text(0,-1.50,'HWE: CHO → CH=CHCO₂R (E)',ha='center',fontsize=10,color=BLUE)
    title(a,'Q12(b): lactol opens to the aldehyde','Same-face attachments at a and d give cis-1,3 substitution')
    fig.savefig('paper-1-ring-transformations.png',dpi=155,facecolor='white');plt.close(fig)

if __name__=='__main__':draw()
