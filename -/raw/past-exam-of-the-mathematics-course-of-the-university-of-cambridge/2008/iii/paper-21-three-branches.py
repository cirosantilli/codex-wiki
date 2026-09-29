"""Triple-branch comparison; tested with Python 3.14 and matplotlib 3.10.7.

Write the PNG basename to the caller's current directory; honour MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 4.4), dpi=100, facecolor='white')
spatial = fig.add_subplot(121, projection='3d')
plane = fig.add_subplot(122)
colors = ['#236aa8', '#b83c3c', '#3e8b63']
u = np.linspace(-1, 1, 101)
zero = np.zeros_like(u)
spatial.plot(u, zero, zero, lw=3, color=colors[0])
spatial.plot(zero, u, zero, lw=3, color=colors[1])
spatial.plot(zero, zero, u, lw=3, color=colors[2])
spatial.scatter([0], [0], [0], s=27, color='#222222')
spatial.text(1.12, 0, 0, '$x$', fontsize=14, color=colors[0])
spatial.text(0, 1.12, 0, '$y$', fontsize=14, color=colors[1])
spatial.text(0, 0, 1.12, '$z$', fontsize=14, color=colors[2])
spatial.set_xlim(-1.2, 1.2)
spatial.set_ylim(-1.2, 1.2)
spatial.set_zlim(-1.2, 1.2)
spatial.set_box_aspect((1, 1, 1))
spatial.view_init(elev=22, azim=-50)
spatial.set_axis_off()
spatial.set_title(r'Spatial axes: $\dim T_0X=3$', fontsize=15, pad=0)
plane.plot(u, zero, lw=3, color=colors[0])
plane.plot(zero, u, lw=3, color=colors[1])
plane.plot(u, u, lw=3, color=colors[2])
plane.scatter([0], [0], s=27, color='#222222', zorder=5)
plane.text(1.1, -.14, '$t=0$', fontsize=13, color=colors[0])
plane.text(.08, 1.07, '$s=0$', fontsize=13, color=colors[1])
plane.text(.71, .86, '$s=t$', fontsize=13, color=colors[2])
plane.set_xlim(-1.2, 1.5)
plane.set_ylim(-1.15, 1.25)
plane.set_aspect('equal')
plane.axis('off')
plane.set_title(r'Coplanar lines: $\dim T_0Y=2$', fontsize=15)
fig.suptitle('Tangent spaces at a triple intersection', fontsize=18, y=.98)
fig.text(.5, .035, 'Real sketches; the cotangent-space proof works over every algebraically closed field.',
         ha='center', fontsize=10, color='#555555')
fig.subplots_adjust(left=.025, right=.97, bottom=.10, top=.83, wspace=.10)
fig.savefig(Path.cwd() / 'paper-21-three-branches.png', dpi=100,
            facecolor='white', transparent=False)
plt.close(fig)
