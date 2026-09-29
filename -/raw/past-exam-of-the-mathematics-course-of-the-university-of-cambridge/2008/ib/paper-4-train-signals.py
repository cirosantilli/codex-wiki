"""Train/platform spacetime diagrams; write an opaque PNG to the caller's cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Units c=L=1. These illustrative speeds satisfy 0<v<u<c.
v, u = 0.45, 0.8
gamma = 1 / np.sqrt(1-v*v)
t = np.linspace(-0.35, 1.5, 400)
t_a = (1-u*v)/(2*(u-v))
t_b = (1+u*v)/(2*(u+v))
tp_a = 1/(2*gamma*(u-v))
tp_b = 1/(2*gamma*(u+v))
fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.1), facecolor='white')
red, green, blue, grey = '#b23b32', '#23804f', '#205da8', '#777777'
for ax in axes:
    ax.set_facecolor('white')
    ax.axhline(0, color='#bbbbbb', lw=0.8)
    ax.axvline(0, color='#bbbbbb', lw=0.8)
    ax.grid(alpha=0.14)
    ax.set_xlim(-1.05, 1.18)
    ax.set_ylim(-0.35, 1.5)
    ax.set_aspect('equal', adjustable='box')
    ax.scatter([0], [0], color='black', s=26, zorder=6)
    ax.annotate('O: emission', (0, 0), xytext=(7, -34), textcoords='offset points', fontsize=9)

ax = axes[0]
ax.set_title('Train frame S', fontsize=13)
ax.set_xlabel('x / L')
ax.set_ylabel('ct / L')
for x, name in [(-0.5, 'B'), (0.5, 'A')]:
    ax.plot(np.full_like(t, x), t, color=red, lw=2)
    ax.text(x+0.025, 1.42, name, color=red, fontsize=11)
ax.plot(-v*t, t, color=green, lw=2)
ax.text(-v*1.35-0.12, 1.35, 'C', color=green, fontsize=11)
for sign in [-1, 1]:
    ax.plot(-v*t+sign/(2*gamma**2), t, color=grey, lw=1.3, ls='--')
# The station simultaneous alignment events lie on t' = 0, i.e. t = -vx.
xx = np.linspace(-0.85, 0.95, 2)
ax.plot(xx, -v*xx, color='#a15ba8', lw=1.2, ls=':')
ax.text(0.63, -v*0.63+0.06, "t' = 0", color='#85448d', fontsize=9)
ax.scatter([-0.5, 0.5], [v/2, -v/2], marker='s', color=grey, s=24, zorder=5)
for x, time, name in [(0.5, t_a, r'$R_A$'), (-0.5, t_b, r'$R_B$')]:
    ax.plot([0, x], [0, time], color=blue, lw=2.1)
    ax.scatter([x], [time], color=blue, s=30, zorder=6)
    ax.annotate(name, (x, time), xytext=(7 if x>0 else -25, 5), textcoords='offset points', fontsize=11)
ax.annotate('', xy=(1/(2*gamma**2), 0), xytext=(-1/(2*gamma**2), 0), arrowprops={'arrowstyle':'<->', 'color':grey})
ax.text(-0.29, -0.14, r'platform: $L/\gamma^2$', color=grey, fontsize=9)

ax = axes[1]
ax.set_title("Station frame S'", fontsize=13)
ax.set_xlabel("x' / L")
ax.set_ylabel("ct' / L")
for sign, name in [(-1, 'B'), (1, 'A')]:
    ax.plot(v*t+sign/(2*gamma), t, color=red, lw=2)
    ax.text(v*1.35+sign/(2*gamma)+0.025, 1.35, name, color=red, fontsize=11)
    ax.plot(np.full_like(t, sign/(2*gamma)), t, color=grey, lw=1.3, ls='--')
ax.plot(np.zeros_like(t), t, color=green, lw=2)
ax.text(0.03, 1.42, 'C', color=green, fontsize=11)
ax.scatter([-1/(2*gamma), 1/(2*gamma)], [0, 0], marker='s', color=grey, s=24, zorder=5)
for x, time, name in [(u*tp_a, tp_a, r'$R_A$'), (-u*tp_b, tp_b, r'$R_B$')]:
    ax.plot([0, x], [0, time], color=blue, lw=2.1)
    ax.scatter([x], [time], color=blue, s=30, zorder=6)
    ax.annotate(name, (x, time), xytext=(6 if x>0 else -28, 5), textcoords='offset points', fontsize=11)
ax.annotate('', xy=(1/(2*gamma), 0), xytext=(-1/(2*gamma), 0), arrowprops={'arrowstyle':'<->', 'color':grey})
ax.text(-0.28, -0.14, r'platform: $L/\gamma$', color=grey, fontsize=9)

handles = [Line2D([0],[0],color=red,lw=2,label='Train endpoints A, B'),
           Line2D([0],[0],color=green,lw=2,label='Station midpoint C'),
           Line2D([0],[0],color=blue,lw=2,label='Signals and receptions'),
           Line2D([0],[0],color=grey,lw=1.3,ls='--',label='Platform endpoints'),
           Line2D([0],[0],color=grey,marker='s',lw=0,label='Endpoint alignment events')]
fig.legend(handles=handles,loc='lower center',ncol=3,frameon=False,fontsize=9,bbox_to_anchor=(0.5,0.04))
fig.suptitle('Same emission, reception and alignment events in two inertial frames',fontsize=14,y=0.97)
fig.text(0.5,0.015,'Illustration: v = 0.45c, u = 0.80c. Distances and times use the train proper length L.',ha='center',fontsize=9)
fig.subplots_adjust(left=0.07,right=0.97,bottom=0.22,top=0.87,wspace=0.27)
fig.savefig(Path.cwd()/'paper-4-train-signals.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
