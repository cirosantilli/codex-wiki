import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

beta = 2.0
d = np.linspace(0, 3, 601)
t = beta / (1 + beta)
population = np.where(d <= t, 1-d, np.where(d <= beta, d/beta, 1.0))
fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=100, layout='constrained')
ax.plot(d, population, color='#1765a4', linewidth=2.5)
ax.axvline(t, color='#777777', linestyle=':', linewidth=1)
ax.axvline(beta, color='#777777', linestyle=':', linewidth=1)
ax.scatter([t], [1/(1+beta)], color='#b33a32', zorder=3)
ax.text(0.18, 1.03, 'all infected', fontsize=10)
ax.text(1.1, 0.48, 'coexistence', fontsize=10)
ax.text(2.18, 1.03, 'disease-free', fontsize=10)
ax.set(xlim=(0, 3), ylim=(0, 1.16), xlabel='Disease mortality d', ylabel='Steady total population', title='Disease mortality can be most harmful at an intermediate rate')
ax.set_xticks([0, t, beta, 3], ['0', r'$\beta/(1+\beta)$', r'$\beta$', '3'])
ax.spines[['top', 'right']].set_visible(False)
fig.savefig('paper-3-frog-population.png', facecolor='white', transparent=False)
plt.close(fig)
