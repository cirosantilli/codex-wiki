"""Original dimensionless potential curves. Python 3.14, NumPy, Matplotlib; PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

def main():
    x=np.linspace(2,30,2400)
    fig,axs=plt.subplots(1,3,figsize=(11.5,4.0),sharex=True,sharey=True)
    for ax,L in zip(axs,[10.,12.,16.]):
        u=-1/x+L/(2*x*x)-L/x**3;un=-1/x+L/(2*x*x)
        ax.plot(x,u,label='Schwarzschild',color='#236994',lw=2)
        ax.plot(x,un,'--',label='Newtonian',color='#a46732',lw=1.7)
        ax.axhline(0,color='.75',lw=.8);ax.axvline(2,color='.45',ls=':',lw=1)
        ax.set(xlim=(2,30),ylim=(-.16,.07),xlabel=r'$r/(GM/c^2)$',title=rf'$\ell^2={L:g}$')
        ax.grid(alpha=.18)
        if L==12:
            ax.scatter([6],[-1/18],s=40,color='#84222a',zorder=5)
            ax.annotate('Marginal stability',(6,-1/18),xytext=(10,-.11),arrowprops={'arrowstyle':'->'},fontsize=10)
        if L>12:
            disc=np.sqrt(L*L-12*L)
            for xx,word,offset in [((L-disc)/2,'Unstable maximum',(7,.025)),((L+disc)/2,'Stable minimum',(16,-.11))]:
                yy=-1/xx+L/(2*xx**2)-L/xx**3
                ax.scatter([xx],[yy],s=35,color='#84222a',zorder=5)
                ax.annotate(word,(xx,yy),xytext=offset,arrowprops={'arrowstyle':'->'},fontsize=9)
        ax.legend(loc='lower right',fontsize=9)
    axs[0].set_ylabel(r'$U/c^2$')
    fig.suptitle('Chosen angular momenta; exterior region only',fontsize=13)
    fig.text(.5,.015,r'Vertical range magnifies the orbital extrema; $U(2GM/c^2)/c^2=-1/2$ lies below the plot.',ha='center',fontsize=10)
    fig.tight_layout(rect=(0,.06,1,.96));fig.savefig('paper-1-effective-potential.png',dpi=160,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
