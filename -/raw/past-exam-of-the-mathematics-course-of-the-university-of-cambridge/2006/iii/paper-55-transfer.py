"""Original qualitative transfer diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory: writes paper-55-transfer.png to caller CWD.
"""
import os
from pathlib import Path
import tempfile
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'codex-wiki-paper-55-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.geomspace(.003,1,600)
xstar=1/30  # Illustrative background: equality well before string domination.
fig,axes=plt.subplots(1,2,figsize=(9.4,3.7),layout='constrained',facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.axvspan(x[0],xstar,color='#eeeeee',alpha=1)
    ax.axvline(xstar,color='#777777',linestyle=':',linewidth=1.2)
    ax.set_xscale('log')
    ax.set_xlim(x[0],1.1)
    ax.set_xlabel(r'Comoving wavenumber $k/k_{\rm eq}$')
    ax.grid(True,which='major',alpha=.2)
    ax.text(.006,.12 if ax is axes[0] else .68,'No eventual\nHubble entry',transform=ax.get_xaxis_transform(),fontsize=9,color='#555555')
    ax.text(xstar,.97,r'$k_*$',transform=ax.get_xaxis_transform(),ha='center')
    ax.text(1,.97,r'$k_{\rm eq}$',transform=ax.get_xaxis_transform(),ha='center')
for ax,y in zip(axes,[np.ones_like(x),x*x]):
    ax.plot(x[x<xstar],y[x<xstar],color='#165e96',linestyle='--',linewidth=2)
    ax.plot(x[x>=xstar],y[x>=xstar],color='#165e96',linewidth=2.5)
axes[0].set_ylim(0,1.3)
axes[0].set_ylabel(r'Shape transfer $T(k)$')
axes[0].set_title(r'After factoring out $k^2D_+(\eta)$',fontsize=11)
axes[0].text(.5,.55,'Post-equality entrants:\nconstant shape',transform=axes[0].transAxes,fontsize=10)
axes[1].set_yscale('log')
axes[1].set_ylim(6e-6,2)
axes[1].set_ylabel('Density / primordial curvature\n(normalized at equality wavenumber)')
axes[1].set_title(r'At fixed late time: $T_\delta\propto k^2$',fontsize=11)
axes[1].text(.55,.18,r'$D_+\to5/2$'+'\nCommon freezing factor',transform=axes[1].transAxes,fontsize=10)
fig.suptitle('Barotropic matter–string model: two transfer conventions',fontsize=12)
fig.savefig(Path('paper-55-transfer.png'),dpi=130,facecolor='white',transparent=False)
