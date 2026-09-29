"""Dark and illuminated characteristics using the ideal model of Q12."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
vt=1.380649e-23*300/1.602176634e-19
iph=1.602176634e-19*(87*.04**2)*412e-9/(6.62607015e-34*299792458)
i0=1e-4/np.expm1(.466/vt);voc=vt*np.log1p(iph/i0)
v=np.linspace(-.07,voc+.02,1800);dark=i0*np.expm1(v/vt);light=dark-iph
# Bisection of dPout/dV=0, no nonstandard dependency.
a,b=0.,voc
for _ in range(70):
 m=(a+b)/2;value=i0*np.expm1(m/vt)-iph+m*i0*np.exp(m/vt)/vt
 if value>0:b=m
 else:a=m
vmp=(a+b)/2;imp=i0*np.expm1(vmp/vt)-iph
fig,ax=plt.subplots(figsize=(7,4.7),layout='constrained')
ax.plot(v,dark*1000,label='dark',color='.4');ax.plot(v,light*1000,label='illuminated',color='#245c9f')
ax.fill([0,vmp,vmp,0],[0,0,imp*1000,imp*1000],color='#f2be68',alpha=.4,label='maximum-power rectangle')
ax.plot(vmp,imp*1000,'o',color='#b45309');ax.annotate('MPP',(vmp,imp*1000),(.39,-28),arrowprops={'arrowstyle':'->'})
ax.annotate(r'$V_{oc}$',(voc,0),(.55,15),arrowprops={'arrowstyle':'->'});ax.text(.025,-iph*1000+2,r'$-I_{ph}$')
ax.axhline(0,color='.25',lw=.7);ax.axvline(0,color='.25',lw=.7)
ax.set(xlabel='Terminal voltage (V)',ylabel='Current into positive terminal (mA)',ylim=(-53,45),title='Photovoltaic generation in quadrant IV');ax.legend(loc='upper left',fontsize=9);ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white');plt.close(fig)
