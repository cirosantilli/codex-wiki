"""Original exchange diagrams and the polarized antimuon projection."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(2, 2, figsize=(11.4, 7.8), layout='constrained')

def line(ax, a, b, reverse=False):
    a, b = np.array(a), np.array(b)
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#283b50', lw=1.8)
    if reverse:
        a, b = b, a
    ax.annotate('', a + .63 * (b-a), a + .39 * (b-a), arrowprops={'arrowstyle': '->', 'color': '#283b50', 'lw': 1.8})

def diagram(ax, labels, boson, anti=False):
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.05, 1.15))
    ax.axis('off')
    a, b = (-.2, .44), (-.2, -.44)
    for start, end, rev in [((-1.05,.8),a,False),(a,(.75,.8),False),((-1.05,-.8),b,anti),(b,(.75,-.8),anti)]:
        line(ax, start, end, rev)
    t = np.linspace(-.44, .44, 180)
    ax.plot(-.2 + .045*np.sin((t+.44)*2*np.pi*8/.88), t, color='#9d3f48', lw=1.5)
    ax.text(.0, -.02, boson, color='#9d3f48', va='center', fontsize=15)
    for xy, text in zip([(-1.15,.84),(.9,.84),(-1.15,-.86),(.9,-.86)], labels):
        ax.text(*xy, text, ha='center', va='center', fontsize=15)
    ax.annotate('time', (.85,1.04), (-.8,1.04), ha='right', va='center', fontsize=10, color='0.4', arrowprops={'arrowstyle':'->','color':'0.5'})

diagram(axes[0,0], [r'$e^-$',r'$\nu_e$',r'$\mu^+$',r'$\bar\nu_\mu$'],r'$W^-$',anti=True)
axes[0,0].set_title('Allowed charged-current exchange', weight='bold')
diagram(axes[0,1], [r'$e^-$',r'$e^-$',r'$\mu^-$',r'$\mu^-$'],r'$\gamma, Z$')
axes[0,1].set_title(r'$\mu^-$: elastic neutral exchange remains', weight='bold')
diagram(axes[1,0], [r'$e^-$',r'$\nu_e$',r'$u$',r'$d$'],r'$W^-$')
axes[1,0].set_title('Proton target: quark-level charge flow', weight='bold')
ax=axes[1,1]
t=np.linspace(0,np.pi,500)
ax.plot(t/np.pi, (1-np.cos(t))/2, lw=2.5, color='#1764a2')
ax.set(xlim=(0,1), ylim=(0,1.08), xticks=[0,.5,1], xticklabels=['0',r'$\pi/2$',r'$\pi$'],xlabel=r'Antimuon rest-spin angle $\theta$ to incoming electron',ylabel=r'$\sigma(\theta)/[(4/5)\sigma_0]$')
ax.set_title('High-energy spin selection',weight='bold')
ax.grid(alpha=.2)
fig.suptitle('Arrows on fermion lines show fermion-number flow\nThe positive antimuon and outgoing antineutrino have reversed arrows',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
