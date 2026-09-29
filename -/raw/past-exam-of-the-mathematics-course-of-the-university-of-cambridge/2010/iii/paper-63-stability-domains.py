"""Plot three exact ODE absolute-stability domains. Python 3.14, root deps.

Writes paper-63-stability-domains.png only to caller CWD.
The caller's MPLCONFIGDIR is preserved.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 2.25, 626)
y = np.linspace(-3, 3, 601)
X, Y = np.meshgrid(x, y)
stable = [((1+X)**2+Y**2 <= 1), ((1-X)**2+Y**2 >= 1), X <= 0]
titles = ['Explicit Euler', 'Backward Euler', 'Trapezoidal rule']
functions = [r'$R(z)=1+z$', r'$R(z)=1/(1-z)$', r'$R(z)=(1+z/2)/(1-z/2)$']
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.9), dpi=135, facecolor='white')
angle = np.linspace(0, 2*np.pi, 500)
for i, ax in enumerate(axs):
    ax.set_facecolor('white')
    ax.contourf(X, Y, stable[i].astype(int), levels=[-.5, .5, 1.5], colors=['white', '#c5e3f2'])
    ax.axhline(0, color='#606a70', lw=.7)
    ax.axvline(0, color='#606a70', lw=.7)
    if i == 0:
        ax.plot(-1+np.cos(angle), np.sin(angle), color='#24566f', lw=1.4)
    elif i == 1:
        ax.plot(1+np.cos(angle), np.sin(angle), color='#24566f', lw=1.4)
    else:
        ax.axvline(0, color='#24566f', lw=1.4)
    ax.set_title(titles[i]+'\n'+functions[i], fontsize=10, pad=10)
    ax.set_xlim(-4, 2.25)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$\mathrm{Re}\,z$')
    ax.set_xticks([-4, -2, 0, 2])
    ax.set_yticks([-2, 0, 2])
    if i == 0:
        ax.set_ylabel(r'$\mathrm{Im}\,z$')
fig.suptitle('Blue regions: amplification modulus at most one', fontsize=13, y=.97)
fig.subplots_adjust(left=.055, right=.98, bottom=.17, top=.76, wspace=.27)
fig.savefig('paper-63-stability-domains.png', facecolor='white', transparent=False)
plt.close(fig)
