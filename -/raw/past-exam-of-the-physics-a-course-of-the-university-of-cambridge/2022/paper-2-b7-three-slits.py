"""Original calculated three-slit solution figure; Python 3.14, root dependencies.
Write opaque PNG basename in cwd. Narrow-slit and finite-width peaks normalized alike.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-32, 32, 7000)  # mm
beta = np.pi*X/10
array = (1+2*np.cos(2*beta))**2/9
envelope = np.sinc(X/20)**2
fig, axes = plt.subplots(2,1,figsize=(8.4,5.8), dpi=130, sharex=True, facecolor='white')
axes[0].plot(X,array,color='#31688e')
axes[1].plot(X,array*envelope,color='#31688e', label='Three-slit intensity')
axes[1].plot(X,envelope,'--',color='#d55e00',label='Single-slit envelope')
axes[0].set_title('Ideal narrow slits: principal maxima every 10 mm', fontsize=11)
axes[1].set_title('Width 25 micrometres: envelope zeros at ±20 mm, ±40 mm, ...', fontsize=11)
for ax in axes:
    ax.set(ylim=(-.03,1.15),xlim=(-32,32),ylabel=r'$I(X)/I(0)$')
    ax.spines[['top','right']].set_visible(False)
    ax.set_xticks(np.arange(-30,31,10))
    ax.grid(alpha=.2)
axes[0].annotate('Small maximum = 1/9', (5,1/9), (7,.48), fontsize=9,
                 arrowprops=dict(arrowstyle='->',color='0.4'))
axes[1].legend(fontsize=9,loc='upper right')
axes[1].set_xlabel('Screen displacement X / mm')
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
