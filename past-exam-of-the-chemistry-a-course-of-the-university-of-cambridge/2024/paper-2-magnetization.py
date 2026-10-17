"""Original full four-state magnetization; magnetic moment remains the printed 2 muB."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

kb=1.380649e-23;muB=9.2740100657e-24
mu=2*muB;B=1.;theta=172.65322530047203
T=np.linspace(.2,600,2200)
# Evaluate each absolute level weight directly, avoiding cosh overflow at low T.
wplus=np.exp(-(theta-mu*B/kb)/T);wminus=np.exp(-(theta+mu*B/kb)/T)
m=(wplus-wminus)/(2+wplus+wminus)
fig,ax=plt.subplots(figsize=(7.7,4.8),facecolor='white')
ax.plot(np.r_[0,T],np.r_[0,m*1e3],color='#245f8a',lw=2)
peak=np.argmax(m)
ax.scatter(T[peak],m[peak]*1e3,color='#a34f26',zorder=3)
ax.annotate('Thermal population first wins;\nthen alignment is lost (~135 K peak)',xy=(T[peak],m[peak]*1e3),xytext=(245,1.95),fontsize=10,arrowprops={'arrowstyle':'->'})
ax.text(15,.24,'Nonmagnetic ground\nmanifold at low T',fontsize=10)
ax.set(xlabel='Temperature (K)',ylabel='M / (Nμ/V), multiplied by 10³',title='NO model: fixed B = 1 T, μ = 2μB, excitation gap = 120 cm⁻¹',xlim=(0,600),ylim=(0,2.5))
ax.grid(alpha=.2)
fig.text(.5,.015,'Full thermal ensemble. The excited-only Curie law must not be extended to T = 0.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.04,1,1))
fig.savefig('paper-2-magnetization.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
