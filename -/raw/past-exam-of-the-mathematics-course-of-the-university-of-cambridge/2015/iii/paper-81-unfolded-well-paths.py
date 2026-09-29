"""Draw original interval-image paths. Write the PNG to the working directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import os
import tempfile
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'codex-wiki-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
t = np.linspace(0, 1, 1001)
q = 0.3
endpoints = [(2 + q, '#1565c0', 'Even: image endpoint 2L + q'),
             (2 - q, '#c62828', 'Odd: image endpoint 2L − q')]
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=125, facecolor='white')
for endpoint, color, label in endpoints:
    x = q + (endpoint-q)*t
    # Fold the unfolded path back into [0,L], with L=1.
    folded = 1-np.abs(np.remainder(x, 2)-1)
    axes[0].plot(t, x, color=color, lw=2.7, label=label)
    axes[1].plot(t, folded, color=color, lw=2.7)
for axis in axes:
    axis.set_xlabel('Imaginary time / total duration')
    axis.set_xlim(0, 1)
    axis.set_xticks([0, 0.5, 1])
    axis.grid(alpha=0.18)
axes[0].set_title('Unfolded free paths')
axes[0].set_ylabel('Unfolded position / L')
axes[0].set_ylim(0, 2.55)
for y in (0, 1, 2):
    axes[0].axhline(y, color='0.45', ls='--', lw=1)
axes[0].legend(loc='upper left', fontsize=10, framealpha=0.95)
axes[1].set_title('Same paths in the physical well')
axes[1].set_ylabel('Position / L')
axes[1].set_ylim(-0.08, 1.13)
for y in (0, 1):
    axes[1].axhline(y, color='0.2', lw=2)
axes[1].text(0.03, 1.055, 'Hard wall', fontsize=10)
axes[1].text(0.42, 0.08, 'Both return to q = 0.3L', fontsize=10)
fig.suptitle('Image paths: two reflections (+) or one reflection (−)', fontsize=15)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=125, facecolor='white', transparent=False)
plt.close(fig)
