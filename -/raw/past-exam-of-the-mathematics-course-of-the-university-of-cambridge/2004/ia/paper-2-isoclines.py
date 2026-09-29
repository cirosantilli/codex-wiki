"""Original IA 2004 Paper 2 Q1 sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes an opaque PNG basename to the caller's working directory. Honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout='constrained', facecolor='white')
x = np.linspace(-2.2, 2.2, 1200)
for ax in axes:
    ax.set(xlim=(-2.2, 2.2), ylim=(-4, 4), xlabel='x', ylabel='y')
    ax.axhline(0, color='0.75', lw=.6)
    ax.axvline(0, color='0.75', lw=.6)
    ax.grid(alpha=.13)
    ax.plot(x, -2*x, '--', color='0.5', lw=1, label='Excluded: y = −2x')
    for m in [-2+np.sqrt(5), -2-np.sqrt(5)]:
        ax.plot(x, m*x, color='black', lw=1.1)
ax=axes[0]
for k in [0, -1, 1]:
    ax.plot(x, (1-2*k)/(2+k)*x, ':', lw=1.4, label=f'Isocline k = {k}')
xx, yy = np.meshgrid(np.linspace(-2.1, 2.1, 19), np.linspace(-3.8, 3.8, 23))
den=2*xx+yy
valid=np.abs(den)>.15
f=np.divide(xx-2*yy, den, out=np.zeros_like(xx), where=valid)
norm=np.hypot(1, f)
ax.quiver(xx[valid], yy[valid], (1/norm)[valid], (f/norm)[valid], color='0.4', angles='xy', scale_units='xy', scale=5.5, width=.0025)
ax.set_title('Constant-slope lines; arrows increase x')
ax.scatter([0],[0],facecolors='white',edgecolors='black',s=28,zorder=5)
ax.legend(fontsize=7, loc='lower left')
ax=axes[1]
for sign in [-1, 1]:
    ax.plot(x,-2*x+sign*np.sqrt(5*x*x+1),color='#1668a7',lw=1.6,label='C = +1' if sign==1 else None)
for side in [-1,1]:
    branch=side*np.linspace(1/np.sqrt(5),2.2,900)
    for sign in [-1,1]:
        vals=-2*branch+sign*np.sqrt(np.maximum(5*branch*branch-1,0))
        ax.plot(branch,vals,color='#c04c2d',lw=1.6,label='C = −1' if side==1 and sign==1 else None)
    ax.scatter([branch[0]],[-2*branch[0]],facecolors='white',edgecolors='#c04c2d',s=35,zorder=6)
# Arrows tangent to the graphs, always towards increasing x.
for c, points, color in [(1,[-1.5,-.1,.9],'#1668a7'),(-1,[.8,1.5],'#c04c2d')]:
    for a in points:
        b=a+.12
        ya=-2*a+np.sqrt(5*a*a+c)
        yb=-2*b+np.sqrt(5*b*b+c)
        ax.annotate('',xy=(b,yb),xytext=(a,ya),arrowprops={'arrowstyle':'->','color':color,'lw':1.5})
ax.scatter([0],[1],color='#1668a7',s=28,zorder=6)
ax.annotate('(0, 1)',(0,1),xytext=(8,10),textcoords='offset points',fontsize=9)
ax.set_title('Solution curves: y² + 4xy − x² = C')
ax.legend(fontsize=8,loc='lower left')
fig.savefig('paper-2-isoclines.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
