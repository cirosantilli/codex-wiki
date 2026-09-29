"""Qualitative matching diagram, not a computed solution of specified kinetics."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def g(u):
    return (u-2)**3-3*(u-2)+5

def bezier(points):
    p = np.asarray(points);t = np.linspace(0, 1, 120)[:, None]
    return (1-t)**3*p[0]+3*(1-t)**2*t*p[1]+3*(1-t)*t*t*p[2]+t**3*p[3]

def arrow(ax, xy, color):
    j=len(xy)//2
    ax.annotate('', xy=xy[j+5], xytext=xy[j-5], arrowprops=dict(arrowstyle='->', color=color, lw=1.7))

def main():
    u=np.linspace(.18, 3.6, 500)
    ub=.5;uc=2+(1.5+np.sqrt(1.25))/2;ud=3.12
    roots=np.roots([1,0,-2,7-(ud+g(ud))]);ua=2+min(roots.real)
    b=np.array([ub,g(ub)]);c=np.array([uc,g(uc)]);d=np.array([ud,g(ud)]);a=np.array([ua,g(ua)])
    fig, ax=plt.subplots(figsize=(7.0, 4.8), layout='constrained')
    ax.plot(u,g(u),color='#777',lw=1.6,label='Nullcline V = g(U)')
    peak=np.array([1.3,g(1.3)]);trough=np.array([2.9,g(2.9)])
    paths=[np.vstack([bezier([b,[.72,6.7],[1.08,g(1.3)],peak]),bezier([peak,[1.85,g(1.3)],[3.1,4.1],c])]),np.vstack([bezier([d,[3.05,3.031],[2.98,g(2.9)],trough]),bezier([trough,[2.2,g(2.9)],[.7,4.9],a])])]
    for j,xy in enumerate(paths):
        ax.plot(xy[:,0],xy[:,1],'--',color='#a34722',lw=1.8,label='Required fast connections (schematic)'if j==0 else None)
        arrow(ax,xy,'#a34722')
    for j,(left,right)in enumerate([(uc,ud),(ua,ub)]):
        vals=np.linspace(left,right,80);xy=np.c_[vals,g(vals)]
        ax.plot(xy[:,0],xy[:,1],color='#087a70',lw=3,label='Slow portions on outer branches'if j==0 else None)
        arrow(ax,xy,'#087a70')
    offsets={'A':(-19,-13),'B':(-16,9),'C':(9,9),'D':(10,-15)}
    for name,point in zip('ABCD',[a,b,c,d]):
        ax.scatter(*point,color='#222',s=22,zorder=5);ax.annotate(name,point,xytext=offsets[name],textcoords='offset points',fontsize=11)
    ax.set(xlim=(.05,3.8),ylim=(1.7,8.1),xlabel='U',ylabel='V',title='Spike matching: B → C → D → A → B')
    ax.text(.04,.04,'Dashed paths indicate connections to be found by shooting.\nNo numerical speed or kinetic function is specified.',transform=ax.transAxes,fontsize=8.5,bbox=dict(facecolor='white',edgecolor='none',alpha=.9))
    ax.grid(alpha=.15);ax.legend(loc='upper right',fontsize=8)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white');plt.close(fig)

if __name__=='__main__':
    main()
