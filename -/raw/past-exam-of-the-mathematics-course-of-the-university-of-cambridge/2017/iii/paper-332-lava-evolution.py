"""Original figure; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from the intended output directory; the PNG is written to CWD.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B, R, STE = 4.0, 20.0, 0.1

def evolution(ratio, n=40000, final_scaled_time=4.0):
    # Integrate in s=sqrt(tau); the initial h~sqrt(2 STE)*s removes
    # the infinite initial dh/dtau. Classical RK4, uniform s steps.
    s = np.linspace(0, np.sqrt(final_scaled_time/B), n+1)
    h = np.zeros(n+1)
    def rhs(v, height):
        if v == 0:
            return np.sqrt(2*STE)
        flux = R*(1+(ratio-1)*np.exp(-B*v*v))
        return 2*STE*(v/height-v*flux)
    for j in range(n):
        ds=s[j+1]-s[j]
        k1=rhs(s[j],h[j])
        k2=rhs(s[j]+ds/2,h[j]+ds*k1/2)
        k3=rhs(s[j]+ds/2,h[j]+ds*k2/2)
        k4=rhs(s[j+1],h[j]+ds*k3)
        h[j+1]=h[j]+ds*(k1+2*k2+2*k3+k4)/6
    tau=s*s
    theta_ratio=1+(ratio-1)*np.exp(-B*tau)
    return B*tau, theta_ratio, R*h

def main():
    assert sys.version_info[:2] == (3,14)
    assert matplotlib.__version__.split('+')[0] == '3.10.7'
    assert np.__version__ == '2.3.5'
    fig, axes=plt.subplots(1,2,figsize=(9.6,4.4),dpi=100,facecolor='white')
    for ratio,color,label in [(0.5,'#1976b5','Cool initial lava'),(1,'#555555','Constant temperature'),(1.5,'#c54436','Hot initial lava')]:
        x,temp,thick=evolution(ratio)
        axes[0].plot(x,temp,color=color,label=label,lw=2)
        axes[1].plot(x,thick,color=color,lw=2)
    for ax in axes:
        ax.set_facecolor('white'); ax.axhline(1,color='#777777',ls=':',lw=1)
        ax.set_xlabel(r'$B\tau$'); ax.grid(alpha=.18); ax.set_xlim(0,4)
    axes[0].set_ylabel(r'$\theta/\theta_*$'); axes[0].set_title('Temperature relaxation')
    axes[1].set_ylabel(r'$h/h_*=R h$'); axes[1].set_title('Crust growth and possible remelting')
    axes[0].legend(fontsize=8,loc='lower right')
    fig.suptitle(r'$B=4,\ R=20,\ \mathrm{Ste}=0.1$; initially no crust',fontsize=11)
    fig.tight_layout(rect=(0,0,1,.93))
    fig.savefig('paper-332-lava-evolution.png',facecolor='white',transparent=False,dpi=100)
    plt.close(fig)
if __name__ == '__main__':
    main()
