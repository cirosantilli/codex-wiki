"""Original BT atlas and numerically traced unstable cycle.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; writes basename PNG to CWD.
Caller-supplied MPLCONFIGDIR is preserved. No SciPy dependency.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def flow(z,lam,mu):
    x,y=z;return np.array([y,-lam+mu*y+x*x+x*y])
def unstable_cycle(lam,mu):
    z=np.array([-np.sqrt(lam)+.01,0.]);h=-.03;tail=[]
    for j in range(100000):
        k1=flow(z,lam,mu);k2=flow(z+h*k1/2,lam,mu);k3=flow(z+h*k2/2,lam,mu);k4=flow(z+h*k3,lam,mu)
        z=z+h*(k1+2*k2+2*k3+k4)/6
        if not np.isfinite(z).all() or abs(z).max()>2:raise RuntimeError('Backward cycle integration escaped')
        if j>96500:tail.append(z.copy())
    return np.array(tail)

def main():
    fig=plt.figure(figsize=(12,6.2),constrained_layout=True);gs=fig.add_gridspec(2,4)
    ax=fig.add_subplot(gs[0,:]);l=np.linspace(0,.018,500);hop=np.sqrt(l);hom=5/7*hop
    ax.fill_between(l,-.1,hom,color='#d9e8df');ax.fill_between(l,hom,hop,color='#ffe0b0');ax.fill_between(l,hop,.18,color='#eddde9')
    ax.axvspan(-.004,0,color='#d9e3ee');ax.axvline(0,color='black',lw=1.3,label='saddle-node: λ=0')
    ax.plot(l,hop,color='#9d4273',lw=1.8,label='Hopf: μ=√λ')
    ax.plot(l,hom,color='#b4772f',ls='--',lw=1.8,label='homoclinic: μ∼(5/7)√λ')
    ax.text(-.003,.11,'I',fontsize=13);ax.text(.008,-.035,'II',fontsize=13);ax.text(.012,.093,'III',fontsize=13);ax.text(.008,.145,'IV',fontsize=13)
    ax.set(xlim=(-.004,.018),ylim=(-.08,.18),xlabel='λ',ylabel='μ',title='Local unfolding; dashed homoclinic curve is its leading asymptote')
    ax.legend(loc='upper left',bbox_to_anchor=(.13,1),fontsize=8)
    cases=[(-.01,0,'I: passage'),(.01,.035,'II: stable focus'),(.01,.09,'III: unstable cycle'),(.01,.13,'IV: unstable focus')]
    xs=np.linspace(-.38,.23,180);ys=np.linspace(-.17,.17,160);X,Y=np.meshgrid(xs,ys)
    for i,(lam,mu,title) in enumerate(cases):
        ax=fig.add_subplot(gs[1,i]);ax.streamplot(xs,ys,Y,-lam+mu*Y+X*X+X*Y,density=.75,linewidth=.55,arrowsize=.8,color='#547897')
        if lam>0:
            ss=np.sqrt(lam);ax.plot([-ss,ss],[0,0],'ko',ms=4);ax.annotate('focus',(-ss,0),xytext=(-10,-17),textcoords='offset points',fontsize=8);ax.annotate('saddle',(ss,0),xytext=(1,7),textcoords='offset points',fontsize=8)
        if i==2:
            cycle=unstable_cycle(lam,mu);ax.plot(cycle[:,0],cycle[:,1],color='#b04a3e',lw=1.6)
        ax.set(xlim=(xs[0],xs[-1]),ylim=(ys[0],ys[-1]),xlabel='x',ylabel='y',title=title)
    fig.savefig('paper-65-bogdanov-takens.png',dpi=150,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
