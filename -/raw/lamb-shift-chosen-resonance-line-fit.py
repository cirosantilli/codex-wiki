"""Original synthetic resonance fit, NOT historical data.
Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Run from _media.
Analytic-Jacobian least squares uses only numpy; known independent noise SD.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

A_SLOPE = 20.0  # MHz/mT, stipulated exactly for this local linear model
DRIVE = 1300.0  # MHz
SIGMA = .004  # chosen detector signal units, independent noise SD
B = np.linspace(2, 18, 65)  # mT

def signal_and_jacobian(p, field):
    c, amp, centre, width = p
    z = 2*(field-centre)/width
    den = 1+z*z
    y = c-amp/den
    jac = np.column_stack((np.ones_like(field), -1/den,
                           -4*amp*z/(width*den**2),
                           -2*amp*z*z/(width*den**2)))
    return y, jac

def calculate():
    true = np.array([1., .25, 10., 5.])
    clean,_ = signal_and_jacobian(true,B)
    observed = clean + np.random.default_rng(1947).normal(0,SIGMA,B.size)
    p=np.array([.99,.23,9.8,4.8])
    for _ in range(30):
        pred,jac=signal_and_jacobian(p,B)
        step=np.linalg.lstsq(jac,observed-pred,rcond=None)[0]
        p+=step
        if np.max(abs(step))<1e-12:break
    pred,jac=signal_and_jacobian(p,B)
    cov=SIGMA**2*np.linalg.inv(jac.T@jac)
    s_centre=np.sqrt(cov[2,2])
    intercept=DRIVE-A_SLOPE*p[2]
    # Calibration error is common to the whole scan; not independent noise per point.
    fit_sd=A_SLOPE*s_centre
    offset_sd=A_SLOPE*.020
    gain_sd=A_SLOPE*p[2]*.001
    combined=np.sqrt(fit_sd**2+offset_sd**2+gain_sd**2+.100**2)
    out={'model':'synthetic, not historical measurements','seed':1947,'signal_units':'chosen arbitrary detector units','sample_count':int(B.size),'drive_MHz':DRIVE,'slope_MHz_per_mT':A_SLOPE,'noise_SD':SIGMA,'true_parameters':true.tolist(),'fit_parameters':p.tolist(),'centre_fit_SD_mT':float(s_centre),'zero_field_intercept_MHz':float(intercept),'fit_SD_MHz':float(fit_sd),'offset_SD_mT':.020,'gain_fraction_SD':.001,'drive_SD_MHz':.100,'combined_SD_MHz':float(combined),'chi_square':float(np.sum(((observed-pred)/SIGMA)**2)),'degrees_of_freedom':int(B.size-4)}
    return p,observed,out

def main():
    p,observed,out=calculate()
    fig,(ax,ay)=plt.subplots(1,2,figsize=(10.5,4.7),facecolor='white',layout='constrained')
    fig.suptitle('Chosen resonance model: line centre and magnetic calibration',fontsize=15)
    fine=np.linspace(2,18,700)
    ax.scatter(B,observed,s=12,color='#40515d',label='Synthetic samples (seed 1947)')
    ax.plot(fine,signal_and_jacobian(p,fine)[0],color='#245a81',lw=2,label='Four-parameter fit')
    ax.axvline(p[2],ls=':',color='#ac4c12')
    ax.set(xlabel='Magnetic field B (mT)',ylabel='Detector current (chosen signal units)',ylim=(.72,1.025))
    ax.text(.04,.06,f'Chosen FWHM: 100 MHz = 5 mT\nFit centre: {p[2]:.3f} ± {out["centre_fit_SD_mT"]:.3f} mT',transform=ax.transAxes,fontsize=10)
    ax.legend(loc='upper left',fontsize=9)
    f=np.linspace(0,13,200)
    ay.plot(f,out['zero_field_intercept_MHz']+A_SLOPE*f,color='#245a81',lw=2)
    ay.axhline(DRIVE,color='#ac4c12',ls='--',label='Chosen drive: 1300 MHz')
    ay.scatter([p[2]],[DRIVE],color='#ac4c12',s=35,zorder=4)
    ay.scatter([0],[out['zero_field_intercept_MHz']],color='#245a81',s=35,zorder=4)
    ay.set(xlabel='Magnetic field B (mT)',ylabel='Transition frequency (MHz)',xlim=(-.6,13),ylim=(1075,1375))
    ay.text(.04,.65,r'$\nu_{\mathrm{res}}(B)=\nu_0+aB$'+'\n'+r'$a=20$ MHz/mT (chosen)',transform=ay.transAxes,fontsize=11)
    ay.text(.04,.09,f'Intercept: {out["zero_field_intercept_MHz"]:.2f} MHz\nFit SD: {out["fit_SD_MHz"]:.2f} MHz\nWith calibration: {out["combined_SD_MHz"]:.2f} MHz',transform=ay.transAxes,fontsize=10,bbox=dict(facecolor='white',edgecolor='none',alpha=.93,pad=3))
    ay.legend(loc='upper left',fontsize=9)
    for axis in (ax,ay):
        axis.spines[['top','right']].set_visible(False);axis.grid(alpha=.18)
    fig.supxlabel('Original toy calculation; linear branch neglects hyperfine mixing. No historical trace or measured Lamb value.',fontsize=10)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
    plt.close(fig)
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
