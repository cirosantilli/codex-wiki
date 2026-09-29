"""Qualitative present solar profiles; no fitted stellar-model values."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r = np.linspace(0,1,501)
x1 = .34 + .36*(1-np.exp(-(r/.24)**2))
x1[r >= .70] = x1[np.searchsorted(r,.70)]
x3 = .06 + .94*np.exp(-((r-.30)/.13)**2)
x3[r >= .70] = x3[np.searchsorted(r,.70)]
fig, axes = plt.subplots(2,1,figsize=(6.8,5.4),sharex=True,layout='constrained')
axes[0].plot(r,x1,lw=2.5,color='#17609c')
axes[0].set_ylabel(r'Hydrogen mass fraction $X_1$')
axes[0].set_ylim(.27,.78)
axes[0].annotate('Core depletion',xy=(.05,.355),xytext=(.25,.40),arrowprops={'arrowstyle':'->'})
axes[1].plot(r,x3,lw=2.5,color='#a23b27')
axes[1].set_ylabel(r'$X_3/\max(X_3)$')
axes[1].annotate('Off-centre maximum',xy=(.3,1),xytext=(.44,.8),arrowprops={'arrowstyle':'->'})
axes[1].set_ylim(0,1.14)
axes[1].set_xlabel(r'Radius $r/R_\odot$')
for ax in axes:
    ax.axvspan(.70,1,color='#d8e6d8',alpha=.55)
    ax.set_xlim(0,1)
    ax.grid(alpha=.2)
axes[0].text(.74,.46,'Mixed\nenvelope')
axes[0].set_title('Qualitative present-day solar abundance profiles')
fig.savefig(Path('paper-63-solar-abundances.png'),dpi=135,facecolor='white')
