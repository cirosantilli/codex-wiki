"""Finite reservoir sketches and exact leading wall signal, cwd output.

The post-reflection depth sketches conserve volume and match the untouched
fan, but are not asserted to solve the full characteristic interaction.
Python 3.14; NumPy/Matplotlib. Leave supplied MPLCONFIGDIR unchanged.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def depth_profile(t):
    x=np.linspace(-1,6*t,1600)
    xi=x/t
    h=np.where(xi<=-1,1,((6-xi)/7)**2)
    if t>1:
        xr=6*t-7*t**(5/7)
        edge=t**(-4/7)
        mask=x<xr
        frac=(x[mask]+1)/(xr+1)
        def candidate(wall):
            out=h.copy();out[mask]=wall+(edge-wall)*frac**2
            return out
        lo=edge;hi=1.
        for _ in range(70):
            mid=(lo+hi)/2
            if np.trapezoid(candidate(mid)**3,x)>1:hi=mid
            else:lo=mid
        h=candidate((lo+hi)/2)
    return x,h

fig,axes=plt.subplots(1,2,figsize=(11,4.8),dpi=140,facecolor='white')
for t,color in [(.5,'#245b8c'),(1.5,'#ba7522'),(3.,'#3e8460')]:
    x,h=depth_profile(t)
    axes[0].plot(x,h,color=color,label=f'$t/t_1={t:g}$')
axes[0].axvline(-1,color='#444444',lw=2)
axes[0].set_xlim(-1.3,18.5);axes[0].set_ylim(0,1.1)
axes[0].set_xlabel(r'$x/\ell$');axes[0].set_ylabel(r'Depth $h/H$')
axes[0].set_title('Finite-volume depletion sketches');axes[0].legend(frameon=False)
axes[0].text(-.8,.05,'wall',fontsize=9)
t=np.linspace(1,3,250);xr=6*t-7*t**(5/7)
axes[1].plot([-1,-1],[0,3],color='#444444',lw=2,label='Impermeable wall')
axes[1].plot([0,-1],[0,1],color='#245b8c',label='Incident head')
axes[1].plot(xr,t,color='#ba7522',lw=2,label='Leading reflected signal')
axes[1].plot([0,18],[0,3],color='#3e8460',lw=2,label='Unaffected dry tip')
axes[1].fill_betweenx(t,-1,xr,color='#fff0db')
axes[1].scatter([-1],[1],color='#ba7522')
axes[1].set_xlim(-1.3,18.5);axes[1].set_ylim(0,3)
axes[1].set_xlabel(r'$x/\ell$');axes[1].set_ylabel(r'$t/t_1$, $t_1=\ell/c_0$')
axes[1].set_title('Exact leading boundaries in the $x$–$t$ plane')
axes[1].legend(frameon=False,fontsize=8,loc='upper left')
for ax in axes:ax.spines[['top','right']].set_visible(False)
fig.text(.5,.02,'After reflection, profiles behind the leading signal are schematic; the front and signal paths are exact.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.045,1,1))
fig.savefig(Path.cwd()/'paper-76-finite-reservoir.png',facecolor='white',transparent=False)
plt.close(fig)
