"""Original model displacement with explicit zero-lag qualification."""
import numpy as np
import matplotlib.pyplot as plt

def main():
 plt.rcParams.update({'font.size':10})
 fig,ax=plt.subplots(1,2,figsize=(8.4,3.9),layout='constrained')
 x=np.linspace(0,4,400);ax[0].plot(x,1+x,c='#286fa3',lw=2)
 ax[0].scatter([0],[1],facecolor='white',edgecolor='#286fa3',s=55,zorder=5);ax[0].scatter([0],[0],c='black',s=25,zorder=5)
 ax[0].annotate('Model intercept A',(0,1),(.65,.7),arrowprops={'arrowstyle':'->'},fontsize=8)
 ax[0].annotate('True zero-lag displacement = 0',(0,0),(.5,.17),arrowprops={'arrowstyle':'->'},fontsize=8)
 ax[0].set(xlabel=r'$t/\tau$',ylabel=r'$\langle\Delta r^2\rangle/A$',title='Linear-axis model extrapolation',ylim=(-.15,5.2))
 z=np.logspace(-3,3,500);ax[1].loglog(z,1+z,c='#286fa3',lw=2,label='Model: 1 + t/τ');ax[1].loglog(z,np.ones_like(z),'--',c='.5',lw=1,label='Elastic scale');ax[1].loglog(z,z,':',c='.3',lw=1,label='Long-time slope one')
 ax[1].set(xlabel=r'$t/\tau$',ylabel=r'$\langle\Delta r^2\rangle/A$',title='Resolved elastic and viscous regimes',ylim=(.7,2e3));ax[1].legend(fontsize=8)
 for a in ax:a.spines[['top','right']].set_visible(False);a.grid(alpha=.2)
 fig.savefig('paper-1-maxwell-creep.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
