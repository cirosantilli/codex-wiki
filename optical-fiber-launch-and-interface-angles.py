"""Draw meridional guidance and the two distinct incidence-angle conventions.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is written to the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle

plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
n1, n2 = 1.50, 1.48
na = np.sqrt(n1*n1-n2*n2)
theta_max = np.arcsin(na)
phi_max = np.arccos(n2/n1)
critical = np.pi/2-phi_max
fig = plt.figure(figsize=(11, 7.4), dpi=100)
grid = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.1], hspace=0.33, wspace=0.25)
ax = fig.add_subplot(grid[0, :])
ax.add_patch(Rectangle((0, -1.45), 22, 2.9, facecolor='#e8eff8', edgecolor='none'))
ax.add_patch(Rectangle((0, -0.5), 22, 1, facecolor='#fff3d1', edgecolor='#8b7742', lw=1.5))
ax.axhline(0, color='#777777', ls='--', lw=1)
phi = np.arcsin(np.sin(np.deg2rad(10))/n1)
wall = 0.5/np.tan(phi)
xray = [0, wall, 3*wall, 5*wall, 22]
yray = [0, 0.5, -0.5, 0.5, 0.5-(22-5*wall)*np.tan(phi)]
ax.plot(xray, yray, color='#006b83', lw=2.6)
ax.annotate('', (0,0), (-5,-5*np.tan(np.deg2rad(10))), arrowprops={'arrowstyle':'->','color':'#006b83','lw':2.6})
ax.text(-4.8, 1.1, 'Air: launch into core', fontsize=12)
ax.text(2, 1.05, r'Cladding: $n_2=1.48$', color='#365983')
ax.text(13, 0.15, r'Core: $n_1=1.50$', color='#71521c')
ax.text(14, -1.1, 'Accepted ray: 10° in air; 6.65° inside', color='#006b83')
ax.text(22, -0.18, 'axis', ha='right', color='#555555')
ax.set_xlim(-5.5, 22.5); ax.set_ylim(-1.65, 1.65)
ax.set_aspect('equal'); ax.axis('off')
ax.set_title('A meridional ray remains in a plane through the fibre axis', loc='left', pad=18)

left = fig.add_subplot(grid[1,0]); right=fig.add_subplot(grid[1,1])
# The enlarged angle panels use equal x/y scales and the actual boundary angles.
left.add_patch(Rectangle((0,-1.5),3,3,facecolor='#fff3d1',edgecolor='none'))
left.axvline(0,color='#8b7742',lw=1.5)
left.plot([-2.7,2.7],[0,0],color='#777777',ls='--')
left.plot([-2.7,0],[-2.7*np.tan(theta_max),0],color='#cf681c',lw=2.5)
left.plot([0,2.7],[0,2.7*np.tan(phi_max)],color='#cf681c',lw=2.5)
left.add_patch(Arc((0,0),2.4,2.4,theta1=180,theta2=180+np.rad2deg(theta_max),color='#cf681c',lw=1.5))
left.add_patch(Arc((0,0),3.4,3.4,theta1=0,theta2=np.rad2deg(phi_max),color='#cf681c',lw=1.5))
left.text(-2.65,-1.1,r'$\theta_{\max}=14.13^\circ$',color='#9a4c10')
left.text(0.5,0.8,r'$\phi_{\max}=9.37^\circ$',color='#9a4c10')
left.text(-2.65,1,'Air: $n_0=1$');left.text(0.5,1.3,'Core')
left.text(-0.12,1.3,'end face',rotation=90,ha='right',va='top',fontsize=10)
left.set_title('Entrance: angles to the axis',loc='left',fontsize=12)
left.set_xlim(-2.9,2.9);left.set_ylim(-1.65,1.65);left.set_aspect('equal');left.axis('off')
right.add_patch(Rectangle((-2.9,0),5.8,1.65,facecolor='#e8eff8',edgecolor='none'))
right.add_patch(Rectangle((-2.9,-1.65),5.8,1.65,facecolor='#fff3d1',edgecolor='none'))
right.axhline(0,color='#8b7742',lw=1.5)
right.plot([0,0],[-1.4,1.4],color='#365983',ls='--',lw=1.4)
right.plot([-2.7,0],[-2.7*np.tan(phi_max),0],color='#cf681c',lw=2.5)
right.annotate('',(2.7,0),(0,0),arrowprops={'arrowstyle':'->','color':'#cf681c','lw':2.0})
right.add_patch(Arc((0,0),1.7,1.7,theta1=180+np.rad2deg(phi_max),theta2=270,color='#365983',lw=1.7))
right.text(-1.65,-1.12,r'$i_c=80.63^\circ$',color='#365983')
right.text(0.16,1.1,'interface normal',color='#365983',fontsize=10)
right.text(-2.65,0.8,'Cladding');right.text(1.25,-1.25,'Core')
right.text(1.05,0.15,'tangent limit',color='#9a4c10',fontsize=10)
right.set_title('Side wall: incidence to the normal',loc='left',fontsize=12)
right.set_xlim(-2.9,2.9);right.set_ylim(-1.65,1.65);right.set_aspect('equal');right.axis('off')
fig.suptitle('Optical fibre: launch and interface angles',fontsize=18,y=0.97)
fig.text(0.5,0.14,r'$i_c+\phi_{\max}=90^\circ$     •     $\mathrm{NA}=\sqrt{n_1^2-n_2^2}=0.244131$',ha='center',fontsize=14)
fig.text(0.5,0.065,'Ideal straight step-index guide • Meridional ray model • Limiting ray is a boundary, not a wave-mode solution',ha='center',fontsize=10)
fig.subplots_adjust(left=0.06,right=0.97,top=0.86,bottom=0.21)
fig.savefig(Path.cwd()/f'{Path(__file__).stem}.png',facecolor='white',transparent=False)
plt.close(fig)
