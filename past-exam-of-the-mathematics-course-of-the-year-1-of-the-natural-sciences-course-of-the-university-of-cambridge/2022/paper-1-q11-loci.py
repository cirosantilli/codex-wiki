"""Generate the PNG in cwd. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7; dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/nst-2022-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,2*np.pi,600)
z=-1-1j+8*np.exp(1j*t)
u=1.5*z+0.5*z.conjugate()
v=u+4+3j
w=1j*v
fig,axes=plt.subplots(2,2,figsize=(7.9,7.3),layout='constrained',facecolor='white')
for ax,curve,title,centre in zip(axes.flat,[z,u,v,w],
        ['(b): $z$, radius 8','(c)(i): $u$, semiaxes 16 and 8','(c)(ii): $v$, translated','(c)(iii): $w$, rotated'],
        [-1-1j,-2-1j,2+2j,-2+2j]):
    ax.plot(curve.real,curve.imag,color='#17679a',linewidth=2)
    ax.plot(centre.real,centre.imag,'o',color='#b3472d',markersize=4)
    ax.annotate(f'({centre.real:g}, {centre.imag:g})',(centre.real,centre.imag),xytext=(5,5),textcoords='offset points',fontsize=9)
    ax.axhline(0,color='gray',linewidth=0.7)
    ax.axvline(0,color='gray',linewidth=0.7)
    ax.set(xlim=(-21,21),ylim=(-21,21),xlabel='real part',ylabel='imaginary part',title=title)
    ax.set_aspect('equal')
    ax.grid(alpha=0.16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=125,facecolor='white')
plt.close(fig)
