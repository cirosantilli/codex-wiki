"""Original particle-flow diagrams; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
fig = plt.figure(figsize=(11, 8.2), layout='constrained')
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1])
a = fig.add_subplot(gs[0, :])
b = fig.add_subplot(gs[1, 0])
c = fig.add_subplot(gs[1, 1])

def fermion(ax, p, q, reverse=False, label=None, offset=(0, 0)):
    p, q = np.array(p, float), np.array(q, float)
    ax.plot([p[0], q[0]], [p[1], q[1]], color='#1c3450', lw=1.7)
    lo, hi = (0.60, 0.42) if reverse else (0.42, 0.60)
    ax.annotate('', xy=p+hi*(q-p), xytext=p+lo*(q-p), arrowprops={'arrowstyle': '-|>', 'color': '#1c3450', 'lw': 1.4})
    if label:
        m = (p+q)/2 + offset
        ax.text(*m, label, ha='center', va='center', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':0.5})

def boson(ax, p, q, label, offset=(0, .14)):
    p, q = np.array(p, float), np.array(q, float)
    d = q-p
    n = np.array([-d[1], d[0]])/np.linalg.norm(d)
    t = np.linspace(0, 1, 250)
    wave = p[None,:]+t[:,None]*d+.045*np.sin(16*np.pi*t)[:,None]*n
    ax.plot(wave[:,0], wave[:,1], color='#a1451b', lw=1.3)
    ax.text(*((p+q)/2 + offset), label, color='#793112', ha='center', va='center', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':0.5})

for ax in (a, b, c):
    ax.axis('off')
    ax.set_ylim(-1.5, 1.5)

a.set_xlim(-.3, 10.5)
a.set_title(r'(a) $e^+e^-\to\tau^+\tau^-$, followed by two three-body decays', loc='left', pad=12)
fermion(a,(0,1),(1,0),label=r'$e^-$',offset=(-.18,.13))
fermion(a,(0,-1),(1,0),True,label=r'$e^+$',offset=(-.18,-.13))
boson(a,(1,0),(2.7,0),r'$\gamma^*,Z^*$',offset=(0,.25))
fermion(a,(2.7,0),(4.2,.8),True,label=r'$\tau^+$',offset=(-.1,.22))
fermion(a,(2.7,0),(4.2,-.8),label=r'$\tau^-$',offset=(-.1,-.22))
fermion(a,(4.2,.8),(6.1,1.28),True,label=r'$\bar\nu_\tau$',offset=(0,.16))
fermion(a,(4.2,-.8),(6.1,-1.28),label=r'$\nu_\tau$',offset=(0,-.16))
boson(a,(4.2,.8),(7.1,.65),r'$W^{+*}$',offset=(0,-.24))
boson(a,(4.2,-.8),(7.1,-.65),r'$W^{-*}$',offset=(0,.24))
fermion(a,(7.1,.65),(9.6,1.25),True,label=r'$\mu^+$',offset=(0,.16))
fermion(a,(7.1,.65),(9.6,.1),label=r'$\nu_\mu$',offset=(0,-.16))
fermion(a,(7.1,-.65),(9.6,-.1),label=r'$e^-$',offset=(0,.16))
fermion(a,(7.1,-.65),(9.6,-1.25),True,label=r'$\bar\nu_e$',offset=(0,-.16))

b.set_xlim(-.25,6.8)
b.set_title(r'(b) $s$ channel: one diagram for each $V=\gamma,Z$',loc='left',pad=12,fontsize=11)
fermion(b,(0,1),(1,0),label=r'$e^-$',offset=(-.2,.12))
fermion(b,(0,-1),(1,0),True,label=r'$e^+$',offset=(-.2,-.12))
boson(b,(1,0),(2.5,0),r'$V^*$',offset=(0,.22))
boson(b,(2.5,0),(4,.8),r'$W^-$',offset=(-.1,.26))
boson(b,(2.5,0),(4,-.8),r'$W^+$',offset=(-.1,-.26))
fermion(b,(4,.8),(6.3,1.25),label=r'$e^-$',offset=(0,.16))
fermion(b,(4,.8),(6.3,.3),True,label=r'$\bar\nu_e$',offset=(0,-.18))
fermion(b,(4,-.8),(6.3,-.3),True,label=r'$\mu^+$',offset=(0,.18))
fermion(b,(4,-.8),(6.3,-1.25),label=r'$\nu_\mu$',offset=(0,-.16))

c.set_xlim(-.25,5.5)
c.set_title(r'(c) $t$ channel: electron-neutrino exchange',loc='left',pad=12,fontsize=11)
fermion(c,(0,1.1),(2,.8),label=r'$e^-$',offset=(0,.22))
fermion(c,(0,-1.1),(2,-.8),True,label=r'$e^+$',offset=(0,-.22))
fermion(c,(2,.8),(2,-.8),label=r'$\nu_e$',offset=(-.4,0))
boson(c,(2,.8),(4.8,1.1),r'$W^-$',offset=(0,.22))
boson(c,(2,-.8),(4.8,-1.1),r'$W^+$',offset=(0,-.22))
c.text(3.5,0,r'Same $W$ decays'+'\nas in panel (b)',ha='center',va='center',fontsize=11)
fig.supxlabel('Arrows show fermion-number flow. Wavy lines represent gauge bosons.',fontsize=11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white')
plt.close(fig)
