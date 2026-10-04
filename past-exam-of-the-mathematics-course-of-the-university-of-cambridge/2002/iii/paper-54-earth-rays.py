"""Original spherical elastic-ray sketches; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-54-earth-rays.png in the caller's working directory.
"""
import os
from pathlib import Path
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'paper-54-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

R, a, cm, cc = 1., .55, 1., .65
limit = 2*np.arccos(a/R)
delta = np.linspace(0, limit, 500)
fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 4.7), layout='constrained', facecolor='white')
left.plot(np.degrees(delta), 2*R/cm*np.sin(delta/2), label='Direct: mantle-only chord', color='#2266aa')
left.plot(np.degrees(delta), 2/cm*np.sqrt(R*R+a*a-2*R*a*np.cos(delta/2)), label='Core-boundary reflection', color='#cc6600')
continuation = np.linspace(limit, np.pi, 200)
left.plot(np.degrees(continuation), 2*R/cm*np.sin(continuation/2), '--', color='.6', label='Homogeneous-sphere continuation')
left.axvline(np.degrees(limit), color='.6', lw=.8)
left.annotate('Grazing join', (np.degrees(limit), 2*np.sqrt(R*R-a*a)), xytext=(45, 1.9), arrowprops={'arrowstyle':'->'})
left.set(xlabel=r'Epicentral angle $\Delta$ (degrees)', ylabel=r'Travel time $Tc_m/R$', title='Direct and reflected arrivals', xlim=(0, 180), ylim=(0, 2.15))
left.legend(fontsize=8, loc='lower right')
left.grid(alpha=.2)
theta = np.linspace(0, 2*np.pi, 600)
right.fill(a*np.cos(theta), a*np.sin(theta), color='#eee5d6')
right.plot(R*np.cos(theta), R*np.sin(theta), color='.25')
right.plot(a*np.cos(theta), a*np.sin(theta), color='.4')
p=.25
im, ic, ir = np.arcsin(p*cm/a), np.arcsin(p*cc/a), np.arcsin(p*cm/R)
dm, dc = im-ir, np.pi-2*ic
angles = np.array([0, dm, dm+dc, 2*dm+dc])
radii = np.array([R, a, a, R])
points=np.column_stack((radii*np.cos(angles), radii*np.sin(angles)))
right.plot(*points.T, '-o', color='#2266aa', markersize=4, label='Core-transmitted P ray')
for k in [1, 2]:
 unit=points[k]/a
 right.plot([points[k,0]-.19*unit[0],points[k,0]+.19*unit[0]], [points[k,1]-.19*unit[1],points[k,1]+.19*unit[1]], '--', color='.5', lw=.8)
for text, point in zip(['Source', 'Entry', 'Exit', 'Receiver'], points):
 right.annotate(text, point, xytext=(4, 6), textcoords='offset points', fontsize=8)
right.text(.05, -.12, r'Core: $c_c=0.65c_m$', ha='center', fontsize=9)
right.text(-.15, -.84, 'Mantle', fontsize=9)
right.text(-1.04, 1.05, r'$a/R=0.55$; bends toward normal at entry', fontsize=9)
right.set(aspect='equal', title='Refraction through the slower core', xlim=(-1.15,1.15), ylim=(-1.15,1.15))
right.axis('off')
fig.savefig(Path.cwd()/'paper-54-earth-rays.png', dpi=135, facecolor='white', transparent=False)
plt.close(fig)
