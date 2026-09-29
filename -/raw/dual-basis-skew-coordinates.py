"""Show how two dual measurements recover a vector's skew-basis coordinates."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    basis=np.array([[1.,1.],[0.,1.]])
    dual=np.linalg.inv(basis)
    v=np.array([3.,1.])
    coefficients=dual @ v
    assert np.allclose(dual @ basis,np.eye(2))
    assert np.allclose(coefficients,[2,1])
    assert np.allclose(basis @ coefficients,v)
    old_row=np.array([2.,-1.]);new_row=old_row @ basis
    assert np.allclose(new_row,[2,1])
    assert old_row @ v==new_row @ coefficients==5
    assert np.allclose(basis.T @ v,[3,4])
    fig,axes=plt.subplots(1,2,figsize=(11,5.8),dpi=120,facecolor='white')
    x=np.linspace(-.4,3.7,200)
    for j,ax in enumerate(axes):
        row=dual[j]
        for c in [-1,0,1,2,3]:
            y=(row[0]*x-c)/(-row[1])
            focus=c==coefficients[j]
            ax.plot(x,y,color='#2b709f' if focus else '#cbd4dc',
                    lw=2.3 if focus else 1.1,ls='-' if focus else '--')
        for vec,label,color in [(basis[:,0],r'$b_1$','#3a7252'),
                                (basis[:,1],r'$b_2$','#8c5a9d'),(v,r'$v$','#2b709f')]:
            ax.annotate('',xy=vec,xytext=(0,0),
                        arrowprops={'arrowstyle':'->','color':color,'lw':2.3})
            offset=(-.12,.15) if label==r'$b_1$' else (-.18,.05)
            ax.text(vec[0]+offset[0],vec[1]+offset[1],label,color=color,fontsize=14)
        ax.plot([0,2,3],[0,0,1],color='#c67b2f',lw=2,ls=':',zorder=4)
        ax.scatter(*v,s=60,color='#2b709f',zorder=5)
        ax.axhline(0,color='#8d9ba7',lw=.7);ax.axvline(0,color='#8d9ba7',lw=.7)
        ax.set(xlim=(-.4,3.7),ylim=(-.4,3.2),aspect='equal',xlabel='x',ylabel='y')
        ax.spines[['top','right']].set_visible(False)
        formula=r'$b_1^*(x,y)=x-y$' if j==0 else r'$b_2^*(x,y)=y$'
        ax.set_title(formula,fontsize=16,pad=12)
        ax.text(.5,-.25,rf'$b_{j+1}^*(3,1)={int(coefficients[j])}$',
                ha='center',transform=ax.transAxes,fontsize=16,color='#2b709f')
        label=rf'$b_{j+1}^*={int(coefficients[j])}$'
        ax.text(2.68,.51 if j==0 else 1.1,label,fontsize=12,color='#2b709f',
                bbox={'facecolor':'white','edgecolor':'none','pad':2})
    fig.suptitle('Dual measurements recover coefficients, even for a skew basis',fontsize=17,y=.975)
    fig.text(.5,.03,r'$v=(3,1)=2b_1+b_2$; blue lines are equal-measurement sets.',
             ha='center',fontsize=14)
    fig.subplots_adjust(left=.065,right=.965,bottom=.26,top=.83,wspace=.28)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
