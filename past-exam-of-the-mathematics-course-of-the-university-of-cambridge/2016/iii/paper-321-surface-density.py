from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    fig,axs=plt.subplots(1,2,figsize=(9,4.8),dpi=100,facecolor='white')
    x=np.geomspace(1e-4,2e2,1300)
    for tau,color in [(1,'#196c9f'),(2,'#c77a13')]:
        sigma=x**(-2.5)*np.exp(-1/(tau*np.sqrt(x)))
        axs[0].semilogx(x,sigma,color=color,label=f'τ = {tau}')
        axs[1].loglog(x,sigma,color=color,label=f'τ = {tau}')
    axs[0].set(xlim=(.001,1),xlabel='dimensionless radius x',ylabel='surface density Σ / Σ₀',title='The peak grows and moves inward')
    axs[1].set(xlim=(.02,200),ylim=(1e-6,1e3),xlabel='dimensionless radius x',title='The outer tail is proportional to x⁻⁵ᐟ²')
    for ax in axs:ax.set_facecolor('white');ax.grid(alpha=.17);ax.legend(framealpha=1,facecolor='white')
    fig.suptitle('Finite mass does not imply finite angular momentum',fontsize=14);fig.tight_layout();fig.savefig(Path.cwd()/'paper-321-surface-density.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
