#!/usr/bin/env python3
"""Cylinder equipotentials; Python3.14/NumPy2.3.5/Matplotlib3.10.7.
Write an opaque PNG to caller CWD; honor caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    x=np.linspace(-3.6,3.6,801)
    y=np.linspace(-2.8,2.8,621)
    X,Y=np.meshgrid(x,y)
    R2=X*X+Y*Y
    phi=np.ma.masked_where(R2<=1,X*(1+1/np.maximum(R2,1e-20)))
    fig,ax=plt.subplots(figsize=(7.0,5.4),layout='constrained',facecolor='white')
    curves=ax.contour(X,Y,phi,levels=np.arange(-3.5,3.51,.5),colors='#225f96',linewidths=.9)
    ax.clabel(curves,levels=[-3,-2,-1,0,1,2,3],inline=True,fontsize=8)
    ax.add_patch(Circle((0,0),1,facecolor='#eeeeee',edgecolor='black',linewidth=1.3,zorder=3))
    ax.text(0,0,'Cylinder',ha='center',va='center',fontsize=10,zorder=4)
    ax.scatter([-1,1],[0,0],s=20,color='#b04d18',zorder=5)
    ax.annotate('Uniform flow',xy=(3.2,2.45),xytext=(1.7,2.45),va='center',arrowprops={'arrowstyle':'->','lw':1.3})
    ax.set(xlabel='x/a',ylabel='y/a',title=r'Equipotentials: $\phi/(Ua)=(r/a+a/r)\cos\theta$')
    ax.set_aspect('equal');ax.set_facecolor('white')
    fig.savefig('paper-4-cylinder-potentials.png',dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
