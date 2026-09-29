"""Solve and plot a stationary GP vortex in a radial lattice.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes only an opaque PNG basename to caller CWD; honors caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np

def tridiagonal(lower, diagonal, upper, rhs):
    """Thomas elimination for the finite-difference Newton correction."""
    b=diagonal.copy(); d=rhs.copy(); c=upper.copy()
    for j in range(1,len(b)):
        scale=lower[j]/b[j-1]
        b[j]-=scale*c[j-1]; d[j]-=scale*d[j-1]
    answer=np.empty_like(d);answer[-1]=d[-1]/b[-1]
    for j in range(len(b)-2,-1,-1):answer[j]=(d[j]-c[j]*answer[j+1])/b[j]
    return answer

def solve_profile(depth=.6, period=4., outer=32., step=.025):
    n=round(outer/step); r=np.linspace(0,outer,n+1); h=r[1]
    potential=depth*np.sin(np.pi*r/period)**2
    lower=np.zeros_like(r);upper=np.zeros_like(r);base=np.zeros_like(r)
    lower[1:-1]=h**-2-1/(2*r[1:-1]*h)
    upper[1:-1]=h**-2+1/(2*r[1:-1]*h)
    base[1:-1]=-2/h**2-1/r[1:-1]**2+1-potential[1:-1]
    lower[-1]=-1; base[-1]=1; base[0]=1
    def residual(f):
        out=np.zeros_like(f)
        out[1:-1]=lower[1:-1]*f[:-2]+upper[1:-1]*f[2:]+base[1:-1]*f[1:-1]-f[1:-1]**3
        out[0]=f[0];out[-1]=f[-1]-f[-2]
        return out
    f=np.tanh(r/np.sqrt(2))*np.sqrt(np.maximum(1-potential,.1))
    for iteration in range(50):
        res=residual(f); norm=np.max(np.abs(res))
        if norm<2e-10:break
        diagonal=base.copy();diagonal[1:-1]-=3*f[1:-1]**2
        correction=tridiagonal(lower,diagonal,upper,-res)
        weight=1.
        for attempt in range(30):
            candidate=f+weight*correction
            if np.min(candidate[1:])>0 and np.max(np.abs(residual(candidate)))<norm:
                f=candidate;break
            weight*=.5
        else:raise RuntimeError('Newton line search failed')
    else:raise RuntimeError('Newton iteration did not converge')
    return r,f,potential,float(np.max(np.abs(residual(f))))

def main():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    r,f,potential,res=solve_profile()
    r0,f0,_,res0=solve_profile(depth=0)
    assert max(res,res0)<2e-10
    fig,(ax,bx)=plt.subplots(2,1,figsize=(8.1,5.8),sharex=True,gridspec_kw={'height_ratios':[3,1]},constrained_layout=True)
    ax.plot(r,f,lw=2,color='#176580',label='Radial lattice: computed unit vortex')
    ax.plot(r0,f0,lw=1.3,ls='--',color='0.45',label='Zero-lattice vortex reference')
    ax.set(xlim=(0,20),ylim=(0,1.08),ylabel=r'Amplitude $R/\sqrt{\mu/U}$',title='Stationary vortex in a radial optical lattice')
    ax.text(6,.25,r'$\mathcal{N}=1$, $d=4\ell_0$, $sE_R/\mu=0.6$',fontsize=11)
    ax.legend(loc='lower right',fontsize=9)
    bx.plot(r,potential,color='#a05c22',lw=1.8)
    bx.set(ylim=(0,.7),xlabel=r'Radius $r/\ell_0$',ylabel=r'$V/\mu$')
    ax.grid(alpha=.18);bx.grid(alpha=.18)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white',transparent=False)

if __name__=='__main__':main()
