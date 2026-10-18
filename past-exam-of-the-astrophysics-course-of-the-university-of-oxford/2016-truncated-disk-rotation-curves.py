from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def elliptic_ke_from_complement(b):
    # b=sqrt(1-k^2), evaluated geometrically without cancellation near a ring.
    a=np.ones_like(b)
    total=(1-b*b)/2
    weight=1.
    for _ in range(18):
        c=(a-b)/2
        total=total+weight*c*c
        a,b=(a+b)/2,np.sqrt(a*b)
        weight*=2
    K=np.pi/(2*a)
    E=K*(1-total)
    return K,E


def disk_speed_squared(r,sigma0,rt,nodes,weights):
    if r==0:return 0.
    if r==rt:return np.nan
    if r<rt:
        s=np.r_[(nodes+1)*r/2,r+(nodes+1)*(rt-r)/2]
        w=np.r_[weights*r/2,weights*(rt-r)/2]
    else:
        s=(nodes+1)*rt/2;w=weights*rt/2
    f=s*sigma0*np.exp(-s)
    K,E=elliptic_ke_from_complement(np.abs(r-s)/(r+s))
    if r<rt:
        fr=r*sigma0*np.exp(-r)
        # Subtract the known logarithmic K singularity analytically as well.
        coeff=fr/(2*r)
        regular=f*K/(r+s)+(f*E-fr)/(r-s)+coeff*np.log(np.abs(r-s))
        log_integral=r*(1-np.log(r))+(rt-r)*(1-np.log(rt-r))
        val=np.sum(w*regular)+fr*np.log(r/(rt-r))+coeff*log_integral
    else:
        val=np.sum(w*f*(K/(r+s)+E/(r-s)))
    return 2*val


plt.rcParams.update({'font.size':11,'axes.titlesize':13,'axes.labelsize':12})
nodes,weights=np.polynomial.legendre.leggauss(260)
rt=5.;ft=1-6*np.exp(-5);sigma0=1/(2*np.pi*ft)
r=np.r_[0,np.linspace(.003,4.97,340),5.,np.linspace(5.03,12,260)]
vd2=np.array([disk_speed_squared(v,sigma0,rt,nodes,weights) for v in r])
f=lambda x:1-(1+x)*np.exp(-x)
modified=np.sqrt(np.where(r<5,f(r)/ft,1.))
newton=np.sqrt(1+vd2)
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.6),dpi=125,facecolor='white',gridspec_kw={'width_ratios':[1.3,1]})
for a in (ax,bx):
    a.plot(r,modified,color='#2268a3',lw=2.5,label='Modified enclosed-mass law')
    a.plot(r,newton,color='#b13939',lw=2.2,label='Newtonian disk + singular halo')
    a.set_ylim(0,1.3);a.set_xlabel(r'$r/R_d$');a.set_ylabel(r'$V_c/V_\infty$')
    a.spines[['top','right']].set_visible(False);a.grid(alpha=.15)
ax.axvline(5,color='0.6',ls=':',lw=1);ax.text(5.2,.55,'Sharp disk edge',fontsize=10,color='0.35')
ax.set_xlim(0,12);ax.set_title('Global curves: unit stellar mass normalization')
ax.legend(loc='lower right',fontsize=9,frameon=True,facecolor='white')
bx.set_xlim(0,1);bx.set_title('Central behavior')
bx.plot(r,np.sqrt(np.maximum(vd2,0)),color='0.4',lw=1.5,ls='--',label='Stellar disk alone')
bx.legend(loc='lower right',fontsize=8.5,frameon=True,facecolor='white')
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
