"""Generate circle-exponential-oscillator.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
All curves are analytic; matching colored samples share the same angle.
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    angles=np.linspace(0,2*np.pi,600)
    samples=np.array([0,np.pi/3,np.pi/2,np.pi,3*np.pi/2])
    colors=['#2878ad','#c05a2a','#24805e','#8655a4','#ad4459']
    assert np.allclose(np.exp(1j*angles),np.cos(angles)+1j*np.sin(angles))
    assert np.isclose(np.cos(np.pi/3),.5)
    fig,axes=plt.subplots(1,2,figsize=(10.5,4.9),dpi=120,facecolor="white",
                          gridspec_kw={'width_ratios':[1,1.5]})
    axes[0].plot(np.cos(angles),np.sin(angles),color='#536778',lw=1.7)
    for phi,color in zip(samples,colors):
        axes[0].scatter(np.cos(phi),np.sin(phi),s=50,c=color,zorder=4)
        axes[1].scatter([phi,phi],[np.cos(phi),np.sin(phi)],s=35,c=color,zorder=4)
    phi=np.pi/3;x,y=np.cos(phi),np.sin(phi)
    axes[0].plot([0,x],[0,y],color=colors[1],lw=2)
    axes[0].plot([x,x],[0,y],'--',color='#aaaaaa',lw=1)
    axes[0].plot([0,x],[y,y],'--',color='#aaaaaa',lw=1)
    axes[0].text(x+.07,y+.08,r'$e^{i\pi/3}$',fontsize=12,color=colors[1])
    axes[0].text(x,-.22,r'$\cos(\pi/3)=1/2$',ha='center',fontsize=10)
    axes[0].text(-.23,y,r'$\sqrt{3}/2$',ha='right',fontsize=10)
    axes[0].set(xlim=(-1.35,1.35),ylim=(-1.3,1.3),aspect='equal',
                xlabel='Real part',ylabel='Imaginary part',title=r'$z(\theta)=e^{i\theta}$ on the unit circle')
    axes[1].plot(angles,np.cos(angles),color='#2878ad',lw=2,label=r'Cosine: $\operatorname{Re}z$')
    axes[1].plot(angles,np.sin(angles),color='#c05a2a',lw=2,label=r'Sine: $\operatorname{Im}z$')
    axes[1].set(xlim=(0,2*np.pi),ylim=(-1.25,1.25),xlabel=r'Angle $\theta$ (radians)',
                ylabel='Coordinate',title='The coordinates oscillate as the point rotates')
    axes[1].set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'])
    axes[1].legend(loc='lower left',fontsize=10,framealpha=.9)
    for ax in axes:
        ax.axhline(0,color='#bbbbbb',lw=.8);ax.axvline(0,color='#bbbbbb',lw=.8)
        ax.grid(alpha=.14);ax.set_facecolor('white')
    fig.suptitle('Geometry, algebra, and differential equations describe the same motion',fontsize=15)
    fig.text(.5,.026,'Matching colors mark the same angle. Both coordinates satisfy '+r'$x^{\prime\prime}(\theta)+x(\theta)=0$'+'.',ha='center',fontsize=10)
    fig.tight_layout(rect=(0,.07,1,.925))
    fig.savefig(Path.cwd()/'circle-exponential-oscillator.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
