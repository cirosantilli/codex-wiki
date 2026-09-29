"""Cubic potential and its phase portrait. Python 3.14; root pyproject dependencies.

Write only the PNG basename to the caller's working directory. Matplotlib honours
any MPLCONFIGDIR supplied by the caller.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def potential(x):
    return 3*x*x-2*x*x*x

def main():
    fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained',facecolor='white')
    left,right=axes
    x=np.linspace(-1.1,2.4,1200)
    left.plot(x,potential(x),color='#172b4d',lw=2)
    left.axhline(0,color='#999999',lw=.7)
    left.axhline(1,color='#bb3333',lw=.9,ls='--',label='Barrier energy 1')
    left.axvline(0,color='#bbbbbb',lw=.6)
    left.scatter([0,1,1.5],[0,1,0],color='#172b4d',zorder=4)
    left.annotate('Minimum (0, 0)',(0,0),xytext=(-.8,-1.1),arrowprops={'arrowstyle':'->','color':'#444444'})
    left.annotate('Maximum (1, 1)',(1,1),xytext=(.1,2.1),arrowprops={'arrowstyle':'->','color':'#444444'})
    left.annotate('(1.5, 0)',(1.5,0),xytext=(1.6,.8))
    left.set(xlim=(-1.1,2.4),ylim=(-3.5,3),xlabel='Position x',ylabel='Potential V(x)',title='Cubic potential V = 3x² − 2x³')
    left.grid(alpha=.15)
    left.legend(loc='lower left',frameon=False)
    xs=np.linspace(-1.15,2.35,1000)
    vs=np.linspace(-3,3,700)
    xx,vv=np.meshgrid(xs,vs)
    energy=vv**2/2+potential(xx)
    levels=[-.6,0,.25,.6,1.7,2.5]
    cs=right.contour(xx,vv,energy,levels=levels,colors=['#999999','#777777','#2962a3','#2962a3','#777777','#999999'],linewidths=1)
    right.clabel(cs,inline=True,fmt=lambda e:f'E={e:g}',fontsize=8)
    sep=np.linspace(-.5,2.35,1100)
    speed=np.abs(sep-1)*np.sqrt(2*(2*sep+1))
    right.plot(sep,speed,color='#bb3333',lw=1.8,label='E = 1 separatrix')
    right.plot(sep,-speed,color='#bb3333',lw=1.8)
    qx,qv=np.meshgrid(np.linspace(-.9,2.1,12),np.linspace(-2.6,2.6,11))
    dx=qv;dv=6*qx*(qx-1)
    norm=np.hypot(dx,dv)
    right.quiver(qx,qv,dx/np.maximum(norm,1e-9),dv/np.maximum(norm,1e-9),angles='xy',scale_units='xy',scale=6,color='#788899',alpha=.35,width=.0025)
    right.scatter([0],[0],s=40,color='#2962a3',zorder=5)
    right.scatter([1],[0],s=45,marker='x',color='#bb3333',zorder=5)
    right.annotate('Centre',(0,0),xytext=(-.6,.2))
    right.annotate('Saddle',(1,0),xytext=(1.1,.25))
    right.axhline(0,color='#bbbbbb',lw=.5)
    right.set(xlim=(-1.15,2.35),ylim=(-3,3),xlabel='Position x',ylabel='Velocity v',title='Energy trajectories: E = v²/2 + V(x)')
    right.legend(loc='lower left',fontsize=9,frameon=False)
    right.grid(alpha=.12)
    fig.savefig(Path('paper-4-potential-phase.png'),dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':
    main()
