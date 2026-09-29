"""Original cap geometry; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from the mirrored _media directory; output is always in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white'})
theta = np.deg2rad(55)
radius = 1.0
centre_y = -np.cos(theta)
foot = np.sin(theta)
height = 1 + centre_y
fig, ax = plt.subplots(figsize=(7.2, 4.5), layout='constrained')
angle = np.linspace(0, 2*np.pi, 700)
ax.plot(np.cos(angle), centre_y + np.sin(angle), '--', color='0.66', lw=1.2)
top_x = np.linspace(-foot, foot, 400)
top_y = centre_y + np.sqrt(1-top_x**2)
ax.fill_between(top_x, 0, top_y, color='#cceafa')
ax.plot(top_x, top_y, color='#12628f', lw=2.5)
ax.axhline(0, color='0.25', lw=2)
ax.text(-1.22, -.10, 'glass', color='0.25')
ax.plot([0, foot], [centre_y, 0], color='#12628f', lw=1.4)
ax.plot(0, centre_y, 'o', color='0.35', ms=4)
ax.text(.48, centre_y/2-.22, '$R$', color='#12628f', fontsize=13)
ax.annotate('', xy=(foot, -.18), xytext=(0, -.18), arrowprops={'arrowstyle':'<->', 'color':'#994e13'})
ax.text(foot/2, -.24, '$s$', ha='center', va='top', color='#994e13', fontsize=13)
ax.annotate('', xy=(1.16, height), xytext=(1.16, 0), arrowprops={'arrowstyle':'<->', 'color':'#6a3c87'})
ax.plot([0,1.19], [height,height], ':', color='0.65', lw=1)
ax.text(1.21, height/2, '$h$', color='#6a3c87', fontsize=13)
# Tangent points up and left into the droplet: 180-theta degrees from +x.
ax.plot([foot, foot-.39*np.cos(theta)], [0, .39*np.sin(theta)], color='0.35', lw=1)
ax.add_patch(Arc((foot,0), .45,.45, theta1=125,theta2=180,color='#b03636',lw=1.4))
ax.text(foot-.30,.065,'$\\theta$',color='#b03636',fontsize=12)
ax.text(-1.22,-1.38,'$s=R\\sin\\theta$\n$h=R(1-\\cos\\theta)$',va='center',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','alpha':.94})
ax.set(xlim=(-1.35,1.4), ylim=(-1.7,.66), aspect='equal')
ax.set_title('Spherical cap: three different length conventions',pad=10)
ax.axis('off')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
