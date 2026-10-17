"""Original pressure fit; axes use numerical rate constants in the stated units."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p=np.array([100.,300.,700.,1000.])
k=np.array([5.09,6.24,9.40,12.8])*1e-4
y=np.log(k);slope,intercept=np.polyfit(p,y,1)
fig,(ax,res)=plt.subplots(2,1,figsize=(7.3,6),sharex=True,gridspec_kw={'height_ratios':[3,1]},facecolor='white')
grid=np.linspace(0,1050,200)
ax.plot(grid,intercept+slope*grid,color='#245f8a',label='Least-squares line')
ax.scatter(p,y,color='#a34f26',zorder=3,label='Given rate data')
ax.set(ylabel='ln(rate numerical value)',title='Activation volume from a logarithmic pressure fit')
ax.text(.04,.91,'Slope = 0.00102471 atm⁻¹\nΔV‡ = −24.65 cm³ mol⁻¹ at 293.15 K',transform=ax.transAxes,va='top',fontsize=11)
ax.legend(loc='lower right');ax.grid(alpha=.18)
res.axhline(0,color='gray',lw=1);res.scatter(p,(y-intercept-slope*p)*1e3,color='#a34f26')
res.set(xlabel='Pressure (atm)',ylabel='Residual × 10³',ylim=(-1,1));res.grid(alpha=.18)
fig.text(.5,.01,'Rate numerical values use dm³ mol⁻¹ s⁻¹; changing these units does not change the slope.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.035,1,1))
fig.savefig('paper-2-pressure-kinetics.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
