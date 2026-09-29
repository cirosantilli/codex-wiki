"""Construct outgoing elastic-collision velocity diagrams. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

plt.rcParams.update({'font.size': 13, 'figure.facecolor': 'white'})
m1, m2, incoming_speed = 2., 1., 1.
angle = np.deg2rad(70.)
V = np.array([m1/(m1+m2)*incoming_speed, 0.])
unit = np.array([np.cos(angle), np.sin(angle)])
cm = [m2/(m1+m2)*incoming_speed*unit, -m1/(m1+m2)*incoming_speed*unit]
lab = [velocity+V for velocity in cm]
fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), layout='constrained')
for ax, velocities, title, labels in zip(axes, [lab, cm], ['Laboratory frame', 'Centre-of-mass frame'], [(r'$\mathbf{v}_1$', r'$\mathbf{v}_2$'), (r'$\mathbf{v}_1^*$', r'$\mathbf{v}_2^*$')]):
    ax.set_aspect('equal')
    ax.set_xlim(-0.8, 1.1)
    ax.set_ylim(-0.85, 0.75)
    ax.axis('off')
    ax.set_title(title, fontsize=17)
    ax.annotate('', xy=(1.02, 0), xytext=(-0.72, 0), arrowprops={'arrowstyle':'->','color':'#999999','linestyle':'--'})
    ax.text(0.42, 0.06, 'initial direction', fontsize=11, color='#666666')
    for velocity, color, label in zip(velocities, ['#a23c27','#205c96'], labels):
        ax.annotate('', xy=velocity, xytext=(0,0), arrowprops={'arrowstyle':'-|>','color':color,'lw':2.7,'mutation_scale':16})
        offset = np.array([0.04, 0.07 if velocity[1]>0 else -0.09])
        ax.text(*(velocity+offset), label, color=color, fontsize=18, ha='center')
    ax.scatter([0],[0],s=22,color='black',zorder=5)
axes[0].add_patch(Arc((0,0),0.45,0.45,theta1=-55,theta2=0,color='#205c96',lw=1.6))
axes[0].text(0.25,-0.14,r'$\theta_2=55^\circ$',fontsize=13,color='#205c96')
axes[1].add_patch(Arc((0,0),0.4,0.4,theta1=0,theta2=70,color='#a23c27',lw=1.6))
axes[1].text(0.18,0.20,r'$\theta^*=70^\circ$',fontsize=13,color='#a23c27')
fig.suptitle('Elastic collision: outgoing velocities for a 2:1 mass ratio',fontsize=16)
fig.supxlabel(r'Velocities in units of $u_1$; laboratory boost $\mathbf{V}=(2u_1/3,0)$',fontsize=13)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
