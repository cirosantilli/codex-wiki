"""Oxford 2015 geometric modelling Q2: uniform quadratic spline join.

Run from any directory; writes geometric-modelling-2015-spline.png there.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='gmod-spline-mpl-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 250)
F = np.column_stack((-2*(1-t)**2, 2*t*(1-t)))
E = np.column_stack((2*t*t, -2*t+2*t*t))
controls = np.array([[-4,-1],[0,1],[0,-1],[4,1]])
fig, axes = plt.subplots(1,2,figsize=(9,4.25),layout='constrained')
for ax in axes:
    ax.axhline(0,color='.75',lw=.8)
    ax.axvline(0,color='.75',lw=.8)
    ax.plot(*F.T,color='#126ab0',lw=2.5,label='F, u in [0,1]')
    ax.plot(*E.T,color='#d15b20',lw=2.5,label='E, u in [1,2]')
    ax.set(xlabel='x',ylabel='y')
    ax.set_aspect('equal')
    ax.grid(alpha=.15)
axes[0].plot([-2,0,0],[0,1,0],'o--',color='#126ab0',alpha=.6,lw=1)
axes[0].plot([0,0,2],[0,-1,0],'o--',color='#d15b20',alpha=.6,lw=1)
for p,label,offset in [((-2,0),'A',(-12,7)),((0,1),'B',(7,2)),((0,-1),'−B',(7,-1)),((2,0),'−A',(4,7))]:
    axes[0].annotate(label,p,xytext=offset,textcoords='offset points',fontsize=10)
axes[0].annotate('',(0,-.38),(0,.25),arrowprops=dict(arrowstyle='->',lw=2,color='#277044'))
axes[0].annotate('join: tangent (0, −2)',(0,0),xytext=(-1.9,-.75),arrowprops=dict(arrowstyle='-',color='.4'),fontsize=9)
axes[0].set(xlim=(-2.35,2.35),ylim=(-1.23,1.23),title='Bézier handles and common tangent')
axes[0].legend(loc='lower right',fontsize=8)
axes[1].plot(*controls.T,'o--',color='#7e549e',lw=1.4,ms=5,label='de Boor control polygon')
for i,p in enumerate(controls):
    axes[1].annotate(f'D{i}',p,xytext=(5,6 if i!=2 else -14),textcoords='offset points',fontsize=10)
axes[1].set(xlim=(-4.65,4.65),ylim=(-1.5,1.5),title='Four shared uniform B-spline handles')
axes[1].legend(loc='upper left',fontsize=8)
fig.savefig('geometric-modelling-2015-spline.png',dpi=125,facecolor='white',transparent=False,bbox_inches='tight',pad_inches=.12)
plt.close(fig)
