"""Original isolated-line model; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
Ts=300.;Tt=200.;x=2/7;nu0=667.;c2=1.438775
pt=(Tt/Ts)**(1/x)
def B(T):return 1/np.expm1(c2*nu0/T)
b0=B(Ts)
nodes,weights=np.polynomial.legendre.leggauss(140)
yunit=(nodes+1)/2;wy=weights/2
mu_nodes,mu_weights=np.polynomial.legendre.leggauss(40)
mu=(mu_nodes+1)/2;wmu=mu_weights/2
s=np.linspace(-2.3,2.3,301);ss=np.abs(s)
exact=[]
for d in ss:
 if d<1e-10:exact.append(B(Tt)/b0);continue
 ys=1/(d*d*mu);upper=np.minimum(ys,32.)
 yy=upper[:,None]*yunit[None,:]
 pp=d*np.sqrt(mu[:,None]*yy)
 temp=np.maximum(Ts*pp**x,Tt)
 intensity=b0*np.exp(-ys)+upper*np.sum(wy[None,:]*B(temp)*np.exp(-yy),axis=1)
 exact.append(2*np.sum(wmu*mu*intensity)/b0)
Trad=np.maximum(Ts*np.minimum(ss,1)**x,Tt)
approx=B(Trad)/b0
fig,(a,b)=plt.subplots(1,2,figsize=(11.8,4.8),layout='constrained')
a.plot(s,exact,lw=2,label='Formal transfer integral + angular average')
a.plot(s,approx,'--',lw=2,label=r'Optical-depth-one estimate')
a.axhline(B(Tt)/b0,color='0.5',ls=':');a.text(-2.2,B(Tt)/b0+.025,'Stratospheric radiance floor',fontsize=10)
for v in [-1,1]:a.axvline(v,color='0.8',ls=':')
a.set(xlabel=r'Wavenumber offset $(\nu-\nu_0)/w$',ylabel=r'$F_\nu/[\pi B_{\nu_0}(T_s)]$',title='Cold core and progressively warmer wings',ylim=(0,1.05),xlim=(-2.3,2.3))
a.legend(loc='lower right',fontsize=8)
b.plot(s,np.minimum(ss,1),lw=2)
b.axhline(pt,color='#c96d24',ls='--',label='Tropopause pressure')
b.axhline(1,color='0.5',ls=':',label='Surface pressure')
b.fill_between(s,0,pt,color='#4477aa',alpha=.12)
b.text(0,pt/2,'isothermal stratosphere',ha='center',va='center',fontsize=10)
b.text(-1.55,.65,'troposphere',ha='center')
b.set(xlabel=r'Wavenumber offset $(\nu-\nu_0)/w$',ylabel=r'$p_{\rm rad}/p_s$',title='Vertical optical-depth-one sampling level',ylim=(1.08,0),xlim=(-2.3,2.3))
b.legend(loc='lower center',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
