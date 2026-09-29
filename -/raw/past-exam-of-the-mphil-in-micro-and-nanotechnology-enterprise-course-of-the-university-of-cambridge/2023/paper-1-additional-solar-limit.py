"""Original radiative detailed-balance example, Python 3.14/numpy/matplotlib.

6000 K sun, 300 K cell, angular radius 0.00465 rad, one emitting hemisphere.
A step absorber and one collected electron per absorbed photon are assumed.
Output is a PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

KB_EV=8.617333262145179e-5
SUN_T=6000.0
CELL_T=300.0
SUN_RADIUS=0.00465

def bose_tail(x):
    """Integral x..infinity of t^2/(exp(t)-1), using its convergent series."""
    x=np.asarray(x,dtype=float)
    n=np.arange(1,401,dtype=float).reshape((-1,)+(1,)*x.ndim)
    return np.sum(np.exp(-n*x)*(x*x/n+2*x/n**2+2/n**3),axis=0)

def radiative_voltage(gap):
    """Common photon-radiance factors cancel from the photocurrent/dark ratio."""
    gap=np.asarray(gap,dtype=float)
    solar=np.pi*np.sin(SUN_RADIUS)**2*(KB_EV*SUN_T)**3*bose_tail(gap/(KB_EV*SUN_T))
    dark=np.pi*(KB_EV*CELL_T)**3*bose_tail(gap/(KB_EV*CELL_T))
    return KB_EV*CELL_T*np.log1p(solar/dark)

gaps=np.linspace(1.0,2.5,400)
voltage=radiative_voltage(gaps)
deficit=gaps-voltage
points=np.array([1.31,1.73,2.32])
pv=radiative_voltage(points)
fig,axes=plt.subplots(1,2,figsize=(10,4.6),layout='constrained')
fig.patch.set_facecolor('white')
ax=axes[0]
ax.plot(gaps,gaps,'--',color='#929ba3',label=r'$E_g/q$')
ax.plot(gaps,voltage,color='#2f758a',lw=2,label='Radiative open circuit')
ax.scatter(points,pv,c='#ad5936',zorder=3)
for x,y,label in zip(points,pv,['CsSnI$_3$','CsPbI$_3$','CsPbBr$_3$']):
    ax.annotate(label,xy=(x,y),xytext=(x-.18,y-.18),fontsize=10,
                arrowprops={'arrowstyle':'-','color':'#ad5936','lw':.7})
ax.set(xlabel='Band gap (eV)',ylabel='Voltage (V)',ylim=(.55,2.6),title='Declared blackbody / step-absorber model')
ax.legend(loc='upper left',fontsize=9)
ax=axes[1]
a=ax.plot(gaps,deficit,color='#2f758a',lw=2,label='Absolute deficit (V)')
ax.scatter(points,points-pv,c='#ad5936',zorder=3)
ax.set(xlabel='Band gap (eV)',ylabel=r'$E_g/q-V_{OC}$ (V)',ylim=(.23,.36),title='Absolute loss rises slowly; fractional loss falls')
right=ax.twinx()
b=right.plot(gaps,100*deficit/gaps,'--',color='#92568b',lw=1.8,label='Fraction of gap voltage (%)')
right.set(ylabel='Deficit / gap voltage (%)',ylim=(8,30))
ax.legend(a+b,[v.get_label() for v in a+b],loc='upper center',fontsize=8.5)
for ax in axes:
    ax.set_xlim(1,2.5)
    ax.grid(alpha=.18)
fig.savefig('paper-1-additional-solar-limit.png',dpi=160,facecolor='white')
plt.close(fig)
