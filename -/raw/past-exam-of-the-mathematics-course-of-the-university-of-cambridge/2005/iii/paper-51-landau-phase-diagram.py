"""Original sextic Landau diagrams. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Caller may set MPLCONFIGDIR; output is always in caller CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 9), facecolor='white', layout='constrained')
ax = fig.add_subplot(221)
u = np.linspace(-1.2, 0, 180)
rt = 3*u*u/16
ax.fill_between(u, -.35, rt, color='#f5dddd', label='Ordered minima ±M')
ax.fill_between(u, rt, .55, color='#e2edf6', label='Disordered minimum M=0')
ax.fill_between([0, 1], [-.35, -.35], [0, 0], color='#f5dddd')
ax.fill_between([0, 1], [0, 0], [.55, .55], color='#e2edf6')
ax.plot(u, rt, color='#b22222', lw=2.5, label='First order: r=3u²/16')
ax.plot([0, 1], [0, 0], color='#16713d', lw=2.5, label='Continuous: r=0')
ax.scatter([0], [0], marker='*', s=150, color='black', zorder=5)
ax.annotate('Tricritical point', (0,0), (.22,.24), arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Quartic control u', ylabel='Quadratic control r', title='Zero-field section (h=0, v=1)', xlim=(-1.2,1), ylim=(-.35,.55))
ax.legend(fontsize=8, loc='upper left'); ax.grid(alpha=.2)

ax = fig.add_subplot(222, projection='3d')
u = np.linspace(-1.2, -.015, 40)[:,None]
z = np.linspace(0, 1, 45)[None,:]
b = np.sqrt(-3*u/(2*(2+z+2*z*z)))
a = z*b; s=a+b; p=a*b
r=(s**4-s*s*p+3*p*p)/3
h=s**3*p/3
for sign in [1,-1]:
    ax.plot_surface(np.broadcast_to(u,r.shape), r, sign*h, color='#e39242', alpha=.6, linewidth=0)
    ax.plot(u[:,0], r[:,-1], sign*h[:,-1], color='#6e2391', lw=2.5)
# Ordered zero-field coexistence sheet below the transition boundary.
us=np.linspace(-1.2,1,45); lower=np.linspace(0,1,12)
upper=np.where(us<0,3*us**2/16,0)
rs=-.25+(upper[:,None]+.25)*lower[None,:]
ax.plot_surface(np.broadcast_to(us[:,None],rs.shape),rs,np.zeros_like(rs),color='#578bc3',alpha=.28)
ax.plot(np.linspace(0,1,30), np.zeros(30),np.zeros(30), color='#16713d', lw=3)
ax.plot(np.linspace(-1.2,0,40),3*np.linspace(-1.2,0,40)**2/16,np.zeros(40),color='#b22222',lw=2.5)
ax.scatter([0],[0],[0],marker='*',s=100,color='black')
ax.set(xlabel='u',ylabel='r',zlabel='h',title='Three controls: orange first-order wings')
ax.text2D(.03,.9,'Purple: ordinary critical edges\nBlue: ordered ±M coexistence\nStar: tricritical point',transform=ax.transAxes,fontsize=8)
ax.view_init(elev=24,azim=-60)

x=np.linspace(-1.45,1.45,500)
ax=fig.add_subplot(223)
for r,c in [(.3,'#286c9c'),(0,'#777777'),(-.3,'#b22222')]:
    ax.plot(x,r*x*x/2+x**4/4+x**6/6,label=f'r={r:g}',color=c)
ax.set(xlabel='Order parameter M',ylabel='f(M)',title='Continuous onset: u=1, h=0',ylim=(-.06,.65))
ax.legend();ax.grid(alpha=.2)
ax=fig.add_subplot(224)
for r,c in [(.25,'#286c9c'),(3/16,'#777777'),(.12,'#b22222')]:
    ax.plot(x,r*x*x/2-x**4/4+x**6/6,label=f'r={r:g}',color=c)
ax.axhline(0,color='black',lw=.6)
for v in [-np.sqrt(3/4),0,np.sqrt(3/4)]:ax.scatter([v],[0],color='black',s=20)
ax.set(xlabel='Order parameter M',ylabel='f(M)',title='First-order coexistence: u=−1, h=0',ylim=(-.03,.09),xlim=(-1.2,1.2))
ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.savefig('paper-51-landau-phase-diagram.png',dpi=100,facecolor='white',transparent=False)
