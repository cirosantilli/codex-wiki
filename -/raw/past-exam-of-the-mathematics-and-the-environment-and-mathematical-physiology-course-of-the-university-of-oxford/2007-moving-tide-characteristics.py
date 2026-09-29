"""Original scalar momentum-model characteristics; writes PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    froude, epsilon, boundary_u, tidal_speed = 0.7, 0.04, 0.65, 0.4
    age = np.linspace(0, 1, 10001)
    dt = age[1] - age[0]
    u = np.empty_like(age)
    u[0] = boundary_u
    def rhs(value):
        return (1 - value**3) / (epsilon * froude**2)
    for j in range(len(age)-1):
        k1 = rhs(u[j]); k2 = rhs(u[j]+dt*k1/2)
        k3 = rhs(u[j]+dt*k2/2); k4 = rhs(u[j]+dt*k3)
        u[j+1] = u[j] + dt*(k1+2*k2+2*k3+k4)/6
    speed = 1/(froude**2*u**2)-u
    displacement = np.r_[0, np.cumsum((speed[:-1]+speed[1:])*dt/2)]
    background = 1/froude**2-1
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.2), layout='constrained')
    for ax, v, title in zip(axes, [0, tidal_speed], ['Fixed downstream boundary', 'Advancing tidal boundary']):
        for start in np.linspace(0, 0.82, 9):
            mask = age+start <= 1
            ax.plot(v*start+displacement[mask], age[mask]+start, color='#176fa8', lw=1.5)
        for x0 in np.linspace(0.12, 0.8, 5):
            ax.plot(x0+background*age, age, color='#bbb', lw=0.8)
        ax.plot(v*age, age, color='#b23a35', lw=2.2, label=f'Boundary X = {v:g}t')
        ax.set(xlim=(-0.025, 1.4), ylim=(0, 1), xlabel='Upstream coordinate X', ylabel='Time t', title=title)
        ax.grid(alpha=.18);ax.legend(loc='lower right', fontsize=8)
    fig.suptitle('Momentum-only characteristics: rapid relaxation to the background speed')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), dpi=120, facecolor='white')
    plt.close(fig)

if __name__ == '__main__':
    main()
