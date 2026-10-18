"""Original threshold-model solutions; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
T=9.;t=np.linspace(-.5,13.5,2400)
KYZ=.25;KYY1=.55;KI=.45
tr=-np.log1p(-KYZ);t1=-np.log1p(-KYY1);tb=t1-np.log1p(-KI)
off1=T+np.log(1/KYY1)
y=np.where(t<0,0,np.where(t<T,-np.expm1(-np.maximum(t,0)),np.exp(-(t-T))))
y1=np.where(t<t1,0,np.where(t<T,-np.expm1(-np.maximum(t-t1,0)),np.where(t<off1,1,np.exp(-(t-off1)))))
z_a=np.where(t<tb,0,np.where(t<T,-np.expm1(-np.maximum(t-tb,0)),np.exp(-(t-T))))
zmin=KYZ*np.exp(-(tb-tr))
z_b=np.where(t<0,0,np.where(t<tr,-np.expm1(-np.maximum(t,0)),np.where(t<tb,KYZ*np.exp(-(t-tr)),np.where(t<T,1+(zmin-1)*np.exp(-(t-tb)),np.exp(-(t-T))))))
fig,axes=plt.subplots(2,1,figsize=(9,6.8),sharex=True,layout='constrained')
for a,z,title in zip(axes,[z_a,z_b],['(a) AND-gated activation','(b) Transient repression, then relief']):
    a.plot(t,y,label='Y',lw=2)
    a.plot(t,y1,label='Y1',lw=2)
    a.plot(t,z,label='Z',lw=2.4)
    a.axvspan(0,T,color='0.6',alpha=.10)
    a.axvline(T,color='0.4',ls='--')
    a.set(ylabel='concentration / C',ylim=(-.05,1.18),title=title)
    a.text(T+.1,1.07,'OFF')
    a.text(.1,1.07,'ON')
    a.legend(loc='lower left',ncol=3)
axes[0].annotate('Z production starts',xy=(tb,0),xytext=(tb+.8,.35),arrowprops={'arrowstyle':'->'})
axes[1].plot([tr,tb],[KYZ,zmin],'ko',ms=4)
axes[1].annotate('temporary minimum',xy=(tb,zmin),xytext=(tb+1.3,.35),arrowprops={'arrowstyle':'->'})
axes[1].set(xlabel=r'time $\alpha t$')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
