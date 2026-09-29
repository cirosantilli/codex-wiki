"""Original discrepancy plot. Python 3.14, numpy, matplotlib; PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

n = np.array([30, 100, 300, 1000, 3000, 10000])
f = np.array([0.000, 0.080, 0.087, 0.093, 0.094, 0.097])
discrepancy = (f - 0.1) ** 2
x = np.geomspace(25, 13000, 300)
fig, ax = plt.subplots(figsize=(6.2, 3.9), layout='constrained')
ax.loglog(n, discrepancy, 'o', color='#245c94', label='Squared discrepancies from rounded fractions')
ax.loglog(x, 0.09 / x, '--', color='#a23d25', label=r'Independent-digit expectation: $0.09/N$')
ax.set(xlabel='Number of digits, N', ylabel=r'$(f_0-0.1)^2$', xlim=(25, 13000), ylim=(4e-6, 2e-2), title='Digit-frequency discrepancies')
ax.text(0.04, 0.07, 'Nested prefixes are correlated; the line is an expectation.', transform=ax.transAxes, fontsize=8)
ax.grid(which='both', alpha=0.2)
ax.legend(fontsize=8, loc='upper right')
fig.savefig('paper-1-digit-deviations.png', dpi=150, facecolor='white')
plt.close(fig)
