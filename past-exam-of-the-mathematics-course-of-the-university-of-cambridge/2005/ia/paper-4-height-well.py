"""Original height-well sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Outputs paper-4-height-well.png to caller CWD; honors MPLCONFIGDIR.
The radial-speed example uses g=1, L^2=2, and hence A=L^2+2g=4.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 4.1), facecolor='white')
r = np.linspace(.45, 10, 1500)
height = 1/r**2-1/r
ax1.plot(r, height, color='#1864ab', lw=2)
ax1.axhline(0, color='#9ba6ad', lw=.8)
ax1.scatter([1, 2], [0, -.25], s=30, color='#1864ab', zorder=5)
ax1.annotate('Minimum $(2,-1/4)$', xy=(2,-.25), xytext=(3.4,.6), fontsize=9,
             arrowprops=dict(arrowstyle='->',color='#1864ab'))
ax1.annotate('Diverges at $r=0$', xy=(.49,2.12), xytext=(2,2.4), fontsize=9,
             arrowprops=dict(arrowstyle='->',color='#1864ab'))
ax1.set(xlim=(0,10), ylim=(-.45,3.1), xlabel='$r$', ylabel='$h(r)$', title='Height profile')

rr = np.linspace(.65, 13, 2000)
g=1;A=4
for r0, color, label in [(2.5,'#1864ab','Bounded: $r_0=2.5$'),
                         (2.,'#2b8a3e','Marginal: $r_0=2$'),
                         (1.5,'#d95f02','Escape: $r_0=1.5$')]:
    energy=A/(2*r0*r0)-g/r0
    f=2*energy+2*g/rr-A/rr**2
    ax2.plot(rr,np.where(f>=0,f,np.nan),color=color,lw=2,label=label)
    ax2.plot(rr,np.where(f<0,f,np.nan),color=color,lw=1.2,ls='--',alpha=.65)
    ax2.scatter([r0],[0],color=color,s=26,zorder=5)
ax2.scatter([4],[0],marker='x',color='#343a40',s=50,zorder=6)
ax2.annotate('Circular release $r_0=4$',xy=(4,0),xytext=(5.4,-.23),fontsize=8.5,
             arrowprops=dict(arrowstyle='->',color='#343a40'))
ax2.axhline(0,color='#9ba6ad',lw=.8)
ax2.set(xlim=(0,13),ylim=(-.38,.8),xlabel='$r$',ylabel=r'$\dot r^2$',title='Radial-speed law: $g=1$, $L^2=2$')
ax2.legend(fontsize=8,loc='upper right',frameon=False)
ax2.text(.4,-.34,'Dashed: inaccessible negative values',fontsize=8,color='#68737d')
for ax in (ax1,ax2):ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig('paper-4-height-well.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
