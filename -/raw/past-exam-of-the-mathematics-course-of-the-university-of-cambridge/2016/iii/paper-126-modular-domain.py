"""Draw the standard SL2(Z) fundamental domain; write opaque PNG only to cwd.
Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    fig,ax=plt.subplots(figsize=(6.2,4.3),dpi=100,facecolor='white')
    x=np.linspace(-.5,.5,500)
    y=np.sqrt(1-x*x)
    ax.fill_between(x,y,3.1,color='#e4eff7')
    ax.plot(x,y,color='#a65d2b',lw=2.2)
    ax.plot([-.5,-.5],[np.sqrt(3)/2,3.1],color='#337ca1',lw=2.2)
    ax.plot([.5,.5],[np.sqrt(3)/2,3.1],color='#337ca1',lw=2.2)
    ax.annotate('',xy=(.48,2.3),xytext=(-.48,2.3),arrowprops=dict(arrowstyle='<->',color='#337ca1',lw=1.6))
    ax.text(0,2.4,r'$T:\ \tau\mapsto\tau+1$',ha='center',fontsize=11)
    ax.annotate('',xy=(.19,1.02),xytext=(-.19,1.02),arrowprops=dict(arrowstyle='<->',color='#a65d2b',lw=1.4))
    ax.text(0,1.21,r'$S:\ \tau\mapsto-1/\tau$',ha='center',fontsize=11)
    ax.annotate('cusp at infinity',xy=(0,3.03),xytext=(0,2.76),ha='center',arrowprops=dict(arrowstyle='->',lw=1.3),fontsize=11)
    ax.scatter([0,-.5,.5],[1,np.sqrt(3)/2,np.sqrt(3)/2],s=25,c='#333333',zorder=5)
    ax.text(.05,.91,r'$i$',fontsize=11)
    ax.text(-.60,.71,r'$\rho$',fontsize=11)
    ax.text(.46,.71,r'$\rho+1$',fontsize=11)
    ax.set_xlim(-.95,.95);ax.set_ylim(.58,3.18)
    ax.set_xticks([-.5,0,.5],['−1/2','0','1/2']);ax.set_yticks([1,2,3])
    ax.set_xlabel(r'$\operatorname{Re}\tau$');ax.set_ylabel(r'$\operatorname{Im}\tau$')
    ax.set_title(r'$|\operatorname{Re}\tau|\leq\frac{1}{2},\quad |\tau|\geq1$',fontsize=13)
    ax.spines[['top','right']].set_visible(False)
    fig.subplots_adjust(left=.13,right=.96,bottom=.14,top=.87)
    fig.savefig(Path.cwd()/'paper-126-modular-domain.png',facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
