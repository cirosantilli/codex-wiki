"""Exact diffusion profiles and phase-diagram trajectory; root NumPy/Matplotlib.
Python 3.14. Opaque PNG basename output to caller CWD; MPLCONFIGDIR unchanged.
"""
from math import erfc, exp, log, sqrt, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def logerfc(z):
    if z<20:
        return log(erfc(z))
    zz=z*z
    return -zz-log(z)-.5*log(pi)+log(1-1/(2*zz)+3/(4*zz*zz)-15/(8*zz**3))

def inverse_F(z):
    if z < -20:
        return 0.0
    if z>20:
        zz=z*z
        return 1/(1-1/(2*zz)+3/(4*zz*zz)-15/(8*zz**3))
    return 1/(sqrt(pi)*z*exp(z*z)*erfc(z))

delta,eps,k,ell,m,Cs,Ts,Tl=.03,.05,.3,100.,1.,1.,-4.,5.
def concentration(lam):
    if abs(lam)<1e-10:return eps*Cs/(1+k*eps)
    a=inverse_F(-lam/eps)
    return Cs*a/((1-k)+k*a-inverse_F(lam))
def residual(lam):
    Ta=-m*concentration(lam);z=delta*lam
    return (Ta-Ts)/erfc(-z)-(Tl-Ta)/erfc(z)-sqrt(pi)*z*exp(z*z)*ell
lo,hi=-3.,0.
assert residual(lo)*residual(hi)<0
for _ in range(65):
    mid=(lo+hi)/2
    if residual(mid)>0:lo=mid
    else:hi=mid
lam=(lo+hi)/2;Ca=concentration(lam);Ta=-m*Ca
# Coordinate X=x/sqrt(D_l*t), front2lambda. Log ratios avoid erfc underflow.
front=2*lam
left=np.unique(np.r_[np.linspace(-180,front,600),front-np.geomspace(1e-7,1,350),front])
right=np.unique(np.r_[np.linspace(front,180,600),front+np.geomspace(1e-7,12,350)])
left.sort();right.sort()
Tlft=Ts+(Ta-Ts)*np.exp([logerfc(-delta*x/2)-logerfc(-delta*lam) for x in left])
Trgt=Tl+(Ta-Tl)*np.exp([logerfc(delta*x/2)-logerfc(delta*lam) for x in right])
Clft=Cs+(k*Ca-Cs)*np.exp([logerfc(-x/(2*eps))-logerfc(-lam/eps) for x in left])
Crgt=Ca*np.exp([logerfc(x/2)-logerfc(lam) for x in right])
fig,axes=plt.subplots(1,3,figsize=(13,4.6),layout='constrained')
axes[0].plot(left,Tlft,color='#315b9c',label='solid')
axes[0].plot(right,Trgt,color='#c9653e',label='liquid')
axes[0].axvline(front,color='.5',ls=':',lw=1)
axes[0].set(xlabel=r'$X=x/\sqrt{D_lt}$',ylabel='Temperature',title='Broad thermal layers',xlim=(-150,150))
axes[0].legend(fontsize=8)
axes[1].plot(left,Clft,color='#315b9c')
axes[1].plot(right,Crgt,color='#c9653e')
axes[1].plot([front,front],[k*Ca,Ca],ls=':',color='.4')
axes[1].axvline(front,color='.5',ls=':',lw=.8)
axes[1].set(xlabel=r'$X=x/\sqrt{D_lt}$',ylabel='Concentration',title='Thin solid / wider liquid solute layers',xlim=(front-.12,3.5),ylim=(-.02,1.05))
axes[1].annotate('solid diffusion layer',xy=(front-.006,.7),xytext=(front+.25,.9),arrowprops={'arrowstyle':'->','color':'.3'},fontsize=8)
cs=np.linspace(0,1.3,200)
axes[2].plot(cs,-m*cs/k,'k--',lw=1,label='solidus')
axes[2].plot(cs,-m*cs,'k:',lw=1,label='liquidus')
axes[2].plot(Clft,Tlft,color='#315b9c',lw=2,label='solid path')
axes[2].plot(Crgt,Trgt,color='#c9653e',lw=2,label='liquid path')
axes[2].plot([k*Ca,Ca],[Ta,Ta],color='#578752',ls='--',lw=1.5,label='interface tie line')
axes[2].plot([k*Ca,Ca],[Ta,Ta],'o',color='#578752',ms=4)
axes[2].annotate('superheated solid',xy=(.65,Ta+.02),xytext=(.57,1.1),arrowprops={'arrowstyle':'->','color':'.3'},fontsize=8)
axes[2].set(xlabel='Concentration',ylabel='Temperature',title='Trajectory through phase diagram',xlim=(-.03,1.15),ylim=(-4.4,5.4))
axes[2].legend(fontsize=7,loc='upper right')
for ax in axes:ax.grid(alpha=.15)
fig.suptitle(r'Melting example: $T_l+T_s=1>0$, $\delta=0.03$, $\epsilon=0.05$'+rf'   ($\lambda={lam:.3f}$)',fontsize=11)
fig.savefig('paper-77-alloy-profiles.png',dpi=135,facecolor='white',transparent=False)
print(f'Exact profile parameters: lambda={lam:.12g}, Ca={Ca:.12g}, Ta={Ta:.12g}, residual={residual(lam):.3g}')
