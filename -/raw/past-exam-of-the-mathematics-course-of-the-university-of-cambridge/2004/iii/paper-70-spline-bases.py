"""Original CAGD sketches; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes paper-70-spline-bases.png to caller CWD; preserves caller MPLCONFIGDIR.
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def beta(x):
    t=np.abs(np.asarray(x))
    return np.where(t<=.5,.75-t*t,np.where(t<=1.5,.5*(1.5-t)**2,0.))


def chaikin(points):
    q=.75*points[:-1]+.25*points[1:]
    r=.25*points[:-1]+.75*points[1:]
    return np.stack([q,r],axis=1).reshape(-1,2)


def main():
    fig,(ax,bx)=plt.subplots(1,2,figsize=(12,4.7))
    rows=np.array([[0,0,0,1/6],[1/6,1/3,2/3,2/3],[2/3,2/3,1/3,1/6],[1/6,0,0,0]])
    colors=['#245b82','#c47629','#34764c','#936aab'];t=np.linspace(0,1,160)
    basis=np.array([math.comb(3,i)*t**i*(1-t)**(3-i) for i in range(4)])
    for j,row in enumerate(rows):
        ax.plot(j+t,row@basis,color=colors[j],lw=2.5)
        ax.plot(j+np.arange(4)/3,row,'o--',color=colors[j],alpha=.6,ms=4)
    ax.set_xlim(-.1,4.1);ax.set_ylim(-.03,.76);ax.set_xticks(range(5))
    ax.set_title('Cubic cardinal B-spline: four Bézier pieces')
    ax.set_xlabel('Unit-spaced knot coordinate');ax.set_ylabel('Basis value')
    ax.text(.15,.7,'Dashed: graph control polygons',fontsize=9)
    p=np.column_stack([np.arange(-4,5),np.array([0,0,0,0,1,0,0,0,0])]).astype(float)
    for iteration in range(8):
        if iteration in [0,1,3,7]:
            bx.plot(*p.T,label=f'{iteration} refinements',lw=1.4,alpha=.8)
        p=chaikin(p)
    x=np.linspace(-2,2,600);bx.plot(x,beta(x),'k--',lw=2,label='Exact quadratic limit')
    bx.set_xlim(-1.8,1.8);bx.set_ylim(-.03,1.08);bx.set_xticks([-1.5,-.5,0,.5,1.5])
    bx.set_xlabel('Coordinate relative to varied control vertex');bx.set_ylabel('Influence weight')
    bx.set_title('Chaikin impulse: support width 3, limit C¹')
    bx.legend(fontsize=8)
    for axis in [ax,bx]:axis.spines[['top','right']].set_visible(False)
    fig.tight_layout();fig.savefig('paper-70-spline-bases.png',dpi=110,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
