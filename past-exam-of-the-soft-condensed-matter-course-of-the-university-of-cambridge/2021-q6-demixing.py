"""Original FH coexistence/free energies; Python 3.14, NumPy 2.3,
Matplotlib 3.10, mpmath 1.3. Output is always in cwd.
Binodals solve common-tangent equations at high precision; no source figure is used.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
mp.mp.dps=40
N=mp.mpf(300)
phi_c=1/(1+mp.sqrt(N))
chi_c=(1+1/mp.sqrt(N))**2/2
TC=298.15
thigh=303.15/TC
tlow=293.15/TC

def coexistence(t):
    t=mp.mpf(str(t));chi=chi_c/t
    aa=2*chi*N-(N-1)
    dd=mp.sqrt(aa*aa-8*chi*N)
    slo=(aa-dd)/(4*chi*N)
    shi=(aa+dd)/(4*chi*N)
    def g(p):
        return p/N*mp.log(p)+(1-p)*mp.log(1-p)+chi*p*(1-p)
    def gp(p):
        return (mp.log(p)+1)/N-mp.log(1-p)-1+chi*(1-2*p)
    def eq(m,h):
        return ((gp(m)-gp(h))/(h-m),((g(h)-g(m))/(h-m)-gp(m))/(h-m))
    lo,hi=mp.findroot(eq,(slo*.45,shi*1.5),tol=mp.mpf('1e-30'),maxsteps=80)
    if not 0<lo<slo<shi<hi<1:
        raise ValueError('Incorrect common-tangent branch')
    if max(abs(v) for v in eq(lo,hi))>mp.mpf('1e-25'):
        raise ValueError('Common-tangent residual too large')
    return tuple(map(float,(lo,hi,slo,shi)))

temp=np.linspace(.92,.9998,85)
bounds=np.array([coexistence(t) for t in temp])
temp=np.r_[temp,1.]
bounds=np.vstack([bounds,np.full(4,float(phi_c))])
lo,hi,slo,shi=coexistence(tlow)

def g(p,t):
    return p/float(N)*np.log(p)+(1-p)*np.log1p(-p)+float(chi_c)/t*p*(1-p)

def gp(p,t):
    return (np.log(p)+1)/float(N)-np.log1p(-p)-1+float(chi_c)/t*(1-2*p)

# Subtract affine references from physical free energies in units k_B*T_c:
# the common tangent at low T, and the tangent at phi_c at high T.
slope=tlow*gp(lo,tlow)
intercept=tlow*g(lo,tlow)-slope*lo
p=np.linspace(.00005,.16,800)
f_low=tlow*g(p,tlow)-slope*p-intercept
slope_high=thigh*gp(float(phi_c),thigh)
intercept_high=thigh*g(float(phi_c),thigh)-slope_high*float(phi_c)
f_high=thigh*g(p,thigh)-slope_high*p-intercept_high
fig,axs=plt.subplots(1,3,figsize=(12,4.0),layout='constrained')
ax=axs[0]
ax.fill_betweenx(temp,bounds[:,0],bounds[:,1],color='#edf4fb')
ax.fill_betweenx(temp,bounds[:,2],bounds[:,3],color='#fae4dc')
for i in [0,1]:
    ax.plot(bounds[:,i],temp,color='#21679a',lw=1.8,label='binodal' if i==0 else None)
for i in [2,3]:
    ax.plot(bounds[:,i],temp,'--',color='#b34d3a',lw=1.6,label='spinodal' if i==2 else None)
ax.plot(float(phi_c),1,'o',color='0.2',ms=4)
ax.text(.066,1.001,'critical point',fontsize=9)
for t,label in [(thigh,'30°C'),(tlow,'20°C')]:
    ax.axhline(t,color='0.5',ls=':',lw=1)
    ax.text(.247,t+.0008,label,ha='right',fontsize=9)
ax.text(.07,.942,'unstable',color='#9b3b2a',fontsize=9)
ax.text(.135,.97,'metastable',color='#376482',fontsize=8)
ax.set(xlim=(0,.25),ylim=(.92,1.025),xlabel=r'Polymer volume fraction $\phi$',ylabel=r'$T/T_c$',title=r'Coexistence near criticality ($N=300$)')
ax.legend(loc='lower right',frameon=False,fontsize=9)
axs[1].plot(p,1e4*f_high,color='#286fa0',lw=2)
axs[1].text(.065,.10,'convex',color='#286fa0')
axs[1].set(title=r'$T_1=30^\circ\mathrm{C}>T_c$',xlabel=r'$\phi$',ylabel=r'$10^4\,\widetilde f/(k_BT_c)$',xlim=(0,.16))
axs[2].plot(p,1e4*f_low,color='#b34d3a',lw=2)
axs[2].plot([lo,hi],[0,0],'o-',color='0.2',ms=4,lw=1.3)
for sp in [slo,shi]:
    axs[2].axvline(sp,color='#b34d3a',ls=':',lw=1)
axs[2].text(.043,.055,r'$f^{\prime\prime}<0$',color='#b34d3a',fontsize=10)
axs[2].text(.055,-.021,'common tangent',ha='center',fontsize=8)
axs[2].set(title=r'$T_2=20^\circ\mathrm{C}<T_c$',xlabel=r'$\phi$',ylabel=r'$10^4\,\widetilde f/(k_BT_c)$',xlim=(0,.16),ylim=(-.035,.45))
for ax in axs:
    ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
