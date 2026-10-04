"""Draw original parabolic Dirichlet regions; Python 3.14 / root pyproject deps.
Writes an opaque PNG basename to caller CWD; honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def arc(center, first, last):
    theta = np.linspace(first, last, 240)
    return center + np.exp(1j * theta)


ur = arc(1+1j, 1.5*np.pi, np.pi)
ul = arc(-1+1j, 0, -.5*np.pi)
ll = arc(-1-1j, .5*np.pi, 0)
lr = arc(1-1j, np.pi, .5*np.pi)
left_boundary = np.exp(1j*np.linspace(.5*np.pi, 1.5*np.pi, 240))
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.6), layout='constrained', facecolor='white')
for ax in axes:
    theta = np.linspace(0, 2*np.pi, 700)
    ax.plot(np.cos(theta), np.sin(theta), color='.35', lw=1.0)
    ax.set_aspect('equal')
    ax.set_xlim(-1.14, 1.14)
    ax.set_ylim(-1.15, 1.15)
    ax.axis('off')
    ax.plot(0, 0, 'o', ms=3.5, color='black')
    ax.text(-.09, -.13, '0', fontsize=10)
    for point, label, off in [(1,'1',(.06,-.02)), (1j,'i',(-.02,.07)), (-1,'−1',(-.16,-.02)), (-1j,'−i',(-.04,-.12))]:
        ax.plot(point.real, point.imag, 'o', mfc='white', mec='.2', ms=5)
        ax.text(point.real+off[0], point.imag+off[1], label, fontsize=11)

boundary = np.concatenate([ur, left_boundary, lr])
axes[0].add_patch(Polygon(np.column_stack([boundary.real,boundary.imag]), fc='#dfeaf5', ec='none'))
for a in [ur,lr]:
    axes[0].plot(a.real, a.imag, color='#2166ac', lw=2.3)
axes[0].text(-.38,.25,r'$D_A$',fontsize=17,color='#174875')
axes[0].text(.39,.61,r'$A$',fontsize=12,color='#2166ac')
axes[0].text(.39,-.64,r'$A^{-1}$',fontsize=12,color='#2166ac')
axes[0].set_title('Cyclic region: two geodesic sides',fontsize=12,pad=9)
boundary = np.concatenate([ur,ul,ll,lr])
axes[1].add_patch(Polygon(np.column_stack([boundary.real,boundary.imag]), fc='#e3efe3', ec='none'))
for a in [ur,lr]:
    axes[1].plot(a.real,a.imag,color='#2166ac',lw=2.3)
for a in [ul,ll]:
    axes[1].plot(a.real,a.imag,color='#d97716',lw=2.3)
axes[1].text(0,.13,r'$P=D_A\cap D_B$',fontsize=11,color='#255c2d',ha='center')
axes[1].text(.40,.61,r'$A$',fontsize=12,color='#2166ac')
axes[1].text(.40,-.64,r'$A^{-1}$',fontsize=12,color='#2166ac')
axes[1].text(-.64,.61,r'$B^{-1}$',fontsize=12,color='#d97716')
axes[1].text(-.64,-.64,r'$B$',fontsize=12,color='#d97716')
axes[1].set_title('Four-sided region: three cusp classes',fontsize=12,pad=9)
fig.savefig('paper-11-dirichlet-regions.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
