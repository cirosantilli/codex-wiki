"""Original Fermat ray sketch. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-2-light-ray.png to the current working directory.
Matplotlib configuration is controlled by the caller's MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

a, c0 = 2.0, 1.0
radius = np.hypot(a, c0)
x = np.linspace(-a, a, 501)
y = np.sqrt(radius**2-x*x)-c0
fig, ax = plt.subplots(figsize=(7, 4.2), dpi=100, facecolor='white')
ax.fill_between(x, 0, 1.65, color='#f1f7fa')
ax.axhline(0, color='#333333', lw=1)
ax.axvline(0, color='#aaaaaa', lw=.8)
ax.plot(x, y, lw=2.5, color='#1e6596')
ax.plot((-a, 0, a), (0, -c0, 0), 'o', color='#333333', ms=4)
ax.plot((-a, 0, a), (0, -c0, 0), '--', color='#999999', lw=1)
ax.annotate('', xy=(.3, np.sqrt(radius**2-.3**2)-c0), xytext=(-.3, np.sqrt(radius**2-.3**2)-c0), arrowprops={'arrowstyle':'->', 'color':'#1e6596','lw':2})
ax.text(-a, -.22, '$(-a,0)$', ha='center')
ax.text(a, -.22, '$(a,0)$', ha='center')
ax.text(.1, -c0-.1, 'centre $(0,-c_0)$', ha='left')
ax.text(.5, -.65, r'$R=\sqrt{a^2+c_0^2}$', fontsize=11)
ax.text(-2.2, 1.47, 'speed increases upwards: $c(y)=y+c_0$', fontsize=10)
ax.set_title('Light ray in a linear speed profile', fontsize=12)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-1.45, 1.75)
ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
fig.tight_layout()
fig.savefig('paper-2-light-ray.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
