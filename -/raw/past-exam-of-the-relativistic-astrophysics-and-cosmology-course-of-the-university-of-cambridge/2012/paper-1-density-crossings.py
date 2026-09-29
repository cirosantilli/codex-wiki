"""Original density scalings using the supplied CMB-only radiation model; PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

def main():
    G=6.67430e-11;c=299792458.;H=72000/(1e6*3.086e16)
    rho=3*H**2/(8*np.pi*G);og=7.566e-16*2.73**4/(c*c*rho)
    xx=np.geomspace(1,1e5,1100)
    fig,ax=plt.subplots(figsize=(8,4.6))
    ax.loglog(xx,.3*xx**3,label='Matter',color='#236994',lw=2)
    ax.loglog(xx,og*xx**4,label='CMB photons only',color='#a46b21',lw=2)
    ax.loglog(xx,np.full_like(xx,.7),label='Vacuum',color='#8e3a73',lw=2)
    for x,y,text,offset in [((.7/.3)**(1/3),.7,'Matter = vacuum',(2.5,7)),((.7/og)**.25,.7,'Photons = vacuum',(18,.01)),(.3/og,.3*(.3/og)**3,'Matter = photons',(80,1e11))]:
        ax.scatter([x],[y],s=36,color='black',zorder=6)
        ax.annotate(text,(x,y),xytext=offset,arrowprops={'arrowstyle':'->','color':'.3'},fontsize=10)
    ax.set(xlim=(1,1e5),ylim=(1e-5,1e16),xlabel=r'$1+z$',ylabel=r'$\rho_i(z)/\rho_{\mathrm{crit},0}$',title='Density crossings need not change the dominant component')
    ax.grid(alpha=.16,which='major');ax.legend(loc='upper left')
    fig.tight_layout();fig.savefig('paper-1-density-crossings.png',dpi=160,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
