"""Original side-view construction; Python 3.14, numpy 2.3, matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5.2), dpi=130, facecolor='white')
ax.set_facecolor('white')

def arrow(a, b, **kw):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='->', lw=2, **kw))

def mirror(p, angle, label, offset):
    d = .42*np.array([np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))])
    p = np.array(p)
    ax.plot([p[0]-d[0], p[0]+d[0]], [p[1]-d[1], p[1]+d[1]], color='#4b5563', lw=5, solid_capstyle='butt')
    ax.text(*(p+np.array(offset)), label, fontsize=11)

# x points forwards; z points upwards. All faces are ordinary plane mirrors.
mirror((0, 0), 135, 'Existing flip mirror', (-1.75, -.45))
mirror((0, 2), 67.5, 'Added mirror 1\nface at 67.5°', (-1.7, .0))
mirror((1, 3), 112.5, 'Added mirror 2\nface at 112.5°', (.45, -.05))
ax.plot([1.9,1.9],[-.42,.42], color='#337ab7', lw=3)
ax.text(1.9,-.65,'Camera lens',ha='center',fontsize=11)
for a,b in [((3,0),(1.95,0)),((1.85,0),(.08,0)),((0,.05),(0,1.95)),((.03,2.03),(.97,2.97)),((.92,3),(-2.1,3))]:
    arrow(a,b,color='#d97706')
ax.plot([-.62,.62],[.95,.95], color='#64748b',lw=3)
ax.text(.75,.88,'Matt screen',fontsize=11)
arrow((.10,1.15),(.65,1.15),color='#1d4ed8')
ax.text(.72,1.12,'Screen top → forwards',fontsize=10,color='#1d4ed8')
ax.text(-2.25,3.05,'Eye',ha='center',fontsize=12)
arrow((-2.28,3.12),(-2.28,3.64),color='#1d4ed8')
ax.text(-2.12,3.58,'Image top ↑',fontsize=10,color='#1d4ed8')
arrow((2.3,2.0),(2.95,2.0),color='black')
arrow((2.3,2.0),(2.3,2.65),color='black')
ax.text(2.85,1.76,'+x forwards',ha='center',fontsize=10)
ax.text(2.32,2.73,'+z up',ha='center',fontsize=10)
ax.text(-2.48,-.9,'Orange: light path. Blue: image-top orientation.\nThe eye looks forwards; left–right reversal remains.',fontsize=10)
ax.set_title('Two added reflections preserve vertical erection',fontsize=14,pad=12)
ax.set_xlim(-2.7,3.35); ax.set_ylim(-1.08,3.95)
ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
