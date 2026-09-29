"""Specific-energy sketch; Python 3.14 and the root-pinned dependencies.

Write the PNG basename to caller CWD, respecting MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    h=np.linspace(.32,3.8,600)
    energy=h+1/(2*h*h)
    fig,ax=plt.subplots(figsize=(5.6,4.1),dpi=140,facecolor='white')
    ax.plot(h,energy,color='#176dab',lw=2)
    ax.axvline(1.,color='#7b858e',ls='--',lw=.8)
    ax.axhline(1.5,color='#7b858e',ls='--',lw=.8)
    ax.scatter([1],[1.5],color='#252e37',s=32,zorder=3)
    ax.text(.35,4.4,'Supercritical\nF > 1',fontsize=10,color='#176dab')
    ax.text(2.55,3.6,'Subcritical\nF < 1',fontsize=10,color='#176dab')
    ax.annotate('Critical minimum',(1,1.5),xytext=(1.8,2.1),fontsize=10,
                arrowprops={'arrowstyle':'->','color':'#555e66'})
    ax.set(xlim=(0,4),ylim=(1,5.5),xlabel=r'Depth $h/h_c$',ylabel=r'Specific energy $E/h_c$',
           title='Specific energy at fixed discharge and width')
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-83-specific-energy.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
