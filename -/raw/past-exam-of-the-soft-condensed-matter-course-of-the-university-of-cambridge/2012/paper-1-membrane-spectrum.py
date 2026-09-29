"""Original dimensionless membrane modes and quadratic stiffness; PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

def main():
 plt.rcParams.update({'font.size':10})
 fig,ax=plt.subplots(1,2,figsize=(8.3,3.7),layout='constrained')
 x=np.linspace(0,1,600)
 for n in [1,2,4]:ax[0].plot(x,.12*np.sin(2*np.pi*n*x),label=f'{n} cycles',lw=1.5)
 ax[0].set(xlabel='Position / period',ylabel='Height (common amplitude)',title='Equal amplitudes, different curvature');ax[0].legend(fontsize=8,loc='lower right');ax[0].set_ylim(-.18,.18)
 q=np.logspace(-2,2,500)
 ax[1].loglog(q,q*q,label='Tension term',ls='--');ax[1].loglog(q,q**4,label='Bending term',ls=':');ax[1].loglog(q,q*q+q**4,c='black',label='Total stiffness')
 ax[1].axvline(1,c='.5',lw=.7);ax[1].set(xlabel=r'$q\sqrt{\kappa/\sigma}$',ylabel='Normalized mode stiffness',title='Variance is inverse stiffness');ax[1].legend(fontsize=8)
 for a in ax:a.grid(alpha=.2);a.spines[['top','right']].set_visible(False)
 fig.savefig('paper-1-membrane-spectrum.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
