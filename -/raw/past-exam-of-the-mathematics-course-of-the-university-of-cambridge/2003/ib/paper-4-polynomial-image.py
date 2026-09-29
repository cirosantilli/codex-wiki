#!/usr/bin/env python3
"""Polynomial image of the unit circle; pinned root NumPy/Matplotlib.
Write an opaque basename PNG to CWD, preserving supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    t=np.linspace(0,2*np.pi,3601)
    z=np.exp(1j*t);w=z**5+z
    fig,ax=plt.subplots(figsize=(6.3,5.6),layout='constrained',facecolor='white')
    ax.axhline(0,color='#999999',lw=.8);ax.axvline(0,color='#dddddd',lw=.8)
    ax.plot(w.real,w.imag,color='#1d6099',lw=1.6)
    for theta in np.linspace(.08,2*np.pi+.08,16,endpoint=False):
        z0=np.exp(1j*theta);z1=np.exp(1j*(theta+.045));v0=z0**5+z0;v1=z1**5+z1
        ax.annotate('',xy=(v1.real,v1.imag),xytext=(v0.real,v0.imag),arrowprops={'arrowstyle':'->','color':'#1d6099','lw':1.2})
    for value in [-2,-1,0,1,2]:
        ax.scatter([value],[0],s=24,color='#ac4718',zorder=5)
        ax.annotate(str(value),xy=(value,0),xytext=(0,9),textcoords='offset points',ha='center',fontsize=10)
    ax.text(-2.15,-2.18,'Origin: four visits; +1 and −1: two visits each',fontsize=9)
    ax.set(xlabel='Real part',ylabel='Imaginary part',title=r'Image $p(e^{i\theta})=e^{5i\theta}+e^{i\theta}$, $0\leq\theta\leq2\pi$',xlim=(-2.3,2.3),ylim=(-2.3,2.3))
    ax.set_aspect('equal');ax.set_facecolor('white')
    fig.savefig('paper-4-polynomial-image.png',dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
