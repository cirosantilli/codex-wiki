"""Stipulated FLRW curves; no observations. Python 3.14, NumPy 2.3, Matplotlib 3.10.

Integrals use NumPy Gauss-Legendre quadrature. An independent composite Simpson
rule and closed-form matter-only/Milne distances check normalization and curvature.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt

C_KM_S = 299792.458
H0_KM_S_MPC = 70.0
MODELS = [(0.3,0.7,'Flat matter + vacuum; q₀ = −0.55','#17658a','-'),
          (0.3,0.0,'Open matter only; q₀ = 0.15','#ad5318','-'),
          (1.0,0.0,'Einstein–de Sitter; q₀ = 0.50','#754d91','-'),
          (0.0,0.0,'Milne (empty, coasting); q₀ = 0','#555e67','--')]


def expansion(z, om, ol):
    return np.sqrt(om*(1+z)**3+(1-om-ol)*(1+z)**2+ol)


def transverse(chi, ok):
    if abs(ok)<1e-14:
        return chi
    if ok>0:
        return np.sinh(np.sqrt(ok)*chi)/np.sqrt(ok)
    return np.sin(np.sqrt(-ok)*chi)/np.sqrt(-ok)


def distance(z, om, ol, order=64):
    z=np.asarray(z,dtype=float)
    x,w=np.polynomial.legendre.leggauss(order)
    chi=z/2*np.sum(w/expansion(z[...,None]*(x+1)/2,om,ol),axis=-1)
    return C_KM_S/H0_KM_S_MPC*(1+z)*transverse(chi,1-om-ol)


def independent_simpson(z, om, ol, intervals=65536):
    # Composite Simpson has a different sampling grid and weighting from Gauss.
    grid=np.linspace(0,z,intervals+1)
    f=1/expansion(grid,om,ol)
    chi=z/(3*intervals)*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())
    return C_KM_S/H0_KM_S_MPC*(1+z)*transverse(chi,1-om-ol)


def check_models():
    largest_relative_error=0.0
    rows=[]
    for z in [.01,.05,.1,.5,1.0,1.2]:
        for om,ol,*_ in MODELS:
            dl=float(distance(z,om,ol)); independent=float(independent_simpson(z,om,ol))
            err=abs(dl-independent)/dl
            largest_relative_error=max(largest_relative_error,err)
            assert err<2e-12,(z,om,ol,err)
            if ol==0:
                # Mattig formula; the Milne limit is evaluated separately.
                analytic=C_KM_S/H0_KM_S_MPC*(z+z*z/2) if om==0 else C_KM_S/H0_KM_S_MPC*2/om**2*(om*z+(om-2)*(np.sqrt(1+om*z)-1))
                assert abs(dl-analytic)/dl<2e-10,(z,om,dl,analytic)
            if z==.5:
                rows.append({'z':z,'Omega_m':om,'Omega_Lambda':ol,'dL_Mpc':dl,'mu_mag':float(5*np.log10(dl)+25)})
    r=float(distance(.5,.3,.7)/distance(.5,.3,0))
    # Low-z Taylor approximation must approach the full relation cubically.
    errors=[]
    for z in [.01,.005,.0025]:
        approx=C_KM_S/H0_KM_S_MPC*(z+.775*z*z)
        errors.append(abs(approx-float(distance(z,.3,.7))))
    assert all(7.9<a/b<8.1 for a,b in zip(errors[:-1],errors[1:])),errors
    return {'Gauss_vs_Simpson_max_relative_error':largest_relative_error,
            'matter_only_checks':'Mattig formula including Einstein-de Sitter; exact Milne limit',
            'z_0_5':rows,'distance_ratio_flat_to_open':r,'flux_ratio_flat_to_open':r**-2,
            'cosmography_absolute_errors_Mpc':errors}


def main():
    checks=check_models()
    z=np.linspace(.01,1.2,360)
    fig,(ax,res)=plt.subplots(2,1,figsize=(11,8),dpi=100,sharex=True,
                              gridspec_kw={'height_ratios':[2,1]},facecolor='white')
    reference=distance(z,.3,0)
    for om,ol,label,color,style in MODELS:
        dl=distance(z,om,ol)
        ax.plot(z,5*np.log10(dl)+25,label=label,color=color,ls=style,lw=2.3)
        res.plot(z,5*np.log10(dl/reference),color=color,ls=style,lw=2.3)
    for panel in (ax,res):
        panel.set_facecolor('white');panel.spines[['top','right']].set_visible(False)
        panel.grid(alpha=.18);panel.axvline(.5,color='#9ba6ae',lw=1,ls=':')
    ax.set(ylabel='Distance modulus μ (mag)',ylim=(33,45),xlim=(0,1.2))
    ax.legend(loc='lower right',frameon=False,fontsize=10.5)
    ax.text(.025,.95,r'$H_0=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$; radiation neglected',transform=ax.transAxes,va='top',fontsize=11)
    res.set(ylabel='μ − μ(open matter) (mag)',xlabel='Redshift z',ylim=(-.41,.34))
    delta=5*np.log10(distance(.5,.3,.7)/distance(.5,.3,0))
    res.annotate(f'z = 0.5: Δμ = {delta:.5f} mag',xy=(.5,delta),xytext=(.66,.09),
                 arrowprops={'arrowstyle':'->','color':'#17658a'},color='#17658a',fontsize=11)
    fig.suptitle('How assumed expansion histories separate in brightness',fontsize=18,x=.07,ha='left',y=.97,weight='bold')
    fig.text(.07,.915,'Calculated FLRW models only • no survey measurements or fitted parameters',fontsize=12,color='#596875')
    fig.text(.07,.025,'Same standardized absolute magnitude in all models; a common H₀ change shifts every μ equally.',fontsize=11)
    fig.subplots_adjust(left=.095,right=.97,top=.875,bottom=.105,hspace=.08)
    fig.savefig(Path(__file__).stem+'.png',facecolor='white',dpi=100)
    plt.close(fig)
    print(json.dumps(checks,indent=2))


if __name__=='__main__':
    main()
