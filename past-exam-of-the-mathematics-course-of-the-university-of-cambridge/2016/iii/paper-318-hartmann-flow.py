#!/usr/bin/env python3
"""Original required sketches. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the intended _media directory: the opaque PNG is written to cwd only.
Dependencies are those already declared in the repository pyproject.toml.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    plt.rcParams.update({'font.size':10,'axes.titlesize':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,axes=plt.subplots(1,3,figsize=(11.5,3.5),dpi=120,layout='constrained')
    H=np.linspace(0,15,700)
    q=np.empty_like(H);small=H<0.05
    q[small]=1-H[small]**2/15+2*H[small]**4/315
    q[~small]=3*(H[~small]/np.tanh(H[~small])-1)/H[~small]**2
    axes[0].plot(H,q,color='#155c9c',lw=2,label='Exact flux')
    hs=np.linspace(3,15,300)
    axes[0].plot(hs,3*(1/hs-1/hs**2),'--',color='#b35d14',label='Large-$H$ limit')
    axes[0].set(xlabel='Hartmann number $H$',ylabel='$Q/Q(0)$',title='Flux at fixed pressure gradient',xlim=(0,15),ylim=(0,1.05));axes[0].legend(frameon=False,fontsize=9)
    z=np.linspace(-1,1,1001);hh=20.
    u=(1/np.tanh(hh))*(1-np.cosh(hh*z)/np.cosh(hh))
    b=-z+np.sinh(hh*z)/np.sinh(hh)
    axes[1].plot(z,u,color='#155c9c',lw=2);axes[1].axhline(1,color='0.5',ls=':',lw=1)
    axes[1].set(xlabel='$z/L$',ylabel='$u/U_c$',title='Nearly uniform velocity, $H=20$',xlim=(-1,1),ylim=(0,1.12))
    axes[1].annotate('Hartmann layers',xy=(0.97,0.45),xytext=(-0.45,0.25),arrowprops={'arrowstyle':'->','color':'0.35'},fontsize=9)
    axes[2].plot(z,b,color='#155c9c',lw=2);axes[2].plot(z,-z,ls='--',color='#b35d14',lw=1,label='Core approximation')
    axes[2].axhline(0,color='0.65',lw=0.7)
    axes[2].set(xlabel='$z/L$',ylabel='$b/B_s$',title='Odd induced magnetic field, $H=20$',xlim=(-1,1),ylim=(-1.05,1.05));axes[2].legend(frameon=False,fontsize=8)
    for ax in axes:ax.grid(alpha=0.18)
    fig.savefig('paper-318-hartmann-flow.png',dpi=120,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
