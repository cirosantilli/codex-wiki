from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    Omega=1.;beta=1.85;alpha=(beta**2-3)/beta;Q0=.2;axlen=np.sqrt(2*Q0/(beta*(2-beta)));aylen=np.sqrt(2*Q0/(alpha*(2-beta)))
    x=np.linspace(-axlen*1.2,axlen*1.2,220);y=np.linspace(-aylen*1.08,aylen*1.08,260);X,Y=np.meshgrid(x,y);Q=Q0-(2-beta)*(beta*X*X+alpha*Y*Y)/2;qm=np.ma.masked_where(Q<0,Q)
    fig,ax=plt.subplots(figsize=(6.2,4.6),dpi=100,facecolor='white');ax.set_facecolor('white')
    im=ax.pcolormesh(X,Y,qm/Q0,cmap='Blues',shading='auto',vmin=0,vmax=1);theta=np.linspace(0,2*np.pi,400);ax.plot(axlen*np.cos(theta),aylen*np.sin(theta),color='#b54a1f',lw=2.2,label='vacuum boundary Q = 0')
    # Flow arrows are tangent to ellipses, including the material outer boundary.
    for scale in [.5,.86]:
        ang=np.linspace(0,2*np.pi,12,endpoint=False);xx=scale*axlen*np.cos(ang);yy=scale*aylen*np.sin(ang);u=alpha*yy;v=-beta*xx;speed=np.hypot(u,v)
        ax.quiver(xx,yy,u/speed,v/speed,color='#162d48',angles='xy',scale_units='xy',scale=3,width=.006)
    ax.set(xlabel='radial coordinate x',ylabel='azimuthal coordinate y',xlim=(-1.9,1.9),ylim=(-aylen*1.15,aylen*1.15));ax.set_aspect('equal');ax.set_title('A bounded polytropic patch: √3 Ω < β < 2 Ω',fontsize=12)
    ax.legend(loc='upper left',fontsize=9,facecolor='white',framealpha=1);fig.colorbar(im,ax=ax,label='enthalpy Q / Q₀',shrink=.8);fig.tight_layout();fig.savefig(Path.cwd()/'paper-321-elliptical-patch.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
