"""Original resonant spin dynamics, full Hamiltonian versus rotating-wave result.

Python 3.14/numpy 2.3.5/matplotlib 3.10.7. Run from mirrored _media directory.
The unitary midpoint integrator preserves spinor norm at every step.
Units: gamma*B_z=omega=1, ratio=B_x/B_z, tau=gamma*B_z*t.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def solve(ratio, duration, steps):
    time = np.linspace(0, duration, steps+1)
    psi = np.zeros((steps+1, 2), complex)
    psi[0, 0] = 1
    dt = duration/steps
    for j in range(steps):
        drive = ratio*np.cos((j+.5)*dt)
        norm = np.hypot(1, drive)
        c = np.cos(norm*dt/2)
        s = 1j*np.sin(norm*dt/2)/norm
        a, b = psi[j]
        psi[j+1] = (c*a+s*(a+drive*b), c*b+s*(drive*a-b))
    ab = np.conj(psi[:, 0])*psi[:, 1]
    bloch = np.column_stack([2*ab.real, 2*ab.imag, abs(psi[:, 0])**2-abs(psi[:, 1])**2])
    return time, bloch


def rotating_wave(time, ratio):
    return np.column_stack([np.sin(ratio*time/2)*np.sin(time), np.sin(ratio*time/2)*np.cos(time), np.cos(ratio*time/2)])


def main():
    fig = plt.figure(figsize=(10.6, 7.6), layout='constrained')
    fig.get_layout_engine().set(hspace=0.16, h_pad=0.08)
    for col, (ratio, duration, title) in enumerate([(.15, 4*np.pi/.15, r'Weak drive: $B_x/B_z=0.15$'), (10., 2*np.pi, r'Strong drive: $B_x/B_z=10$')]):
        steps = max(12000, int(duration*max(1, ratio)*1000))
        t, full = solve(ratio, duration, steps)
        rwa = rotating_wave(t, ratio)
        ax = fig.add_subplot(2, 2, col+1, projection='3d')
        end = len(t)//2 if col == 0 else len(t)
        stride = max(1, end//2500)
        ax.plot(*full[:end:stride].T, color='#236bc0', lw=1.7, label='full Hamiltonian')
        ax.plot(*rwa[:end:stride].T, color='#c26712', lw=1.2, ls='--', label='rotating-wave')
        ax.scatter([0], [0], [1], color='black', s=18)
        ax.set(xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1), xlabel=r'$s_x$', ylabel=r'$s_y$', zlabel=r'$s_z$', title=title)
        ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.set_zticks([-1,0,1])
        ax.set_box_aspect([1,1,1])
        ax.view_init(elev=21, azim=-54)
        ax.legend(fontsize=8, loc='upper left')
        low = fig.add_subplot(2, 2, col+3)
        stride = max(1, len(t)//4000)
        low.plot(t[::stride], full[::stride,2], color='#236bc0', lw=1.7)
        low.plot(t[::stride], rwa[::stride,2], color='#c26712', ls='--', lw=1.3)
        low.set(xlim=(0,duration), ylim=(-1.08,1.08), xlabel=r'$\tau=\gamma B_zt$', ylabel=r'$s_z=2\langle S_z\rangle/\hbar$')
        low.grid(alpha=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
