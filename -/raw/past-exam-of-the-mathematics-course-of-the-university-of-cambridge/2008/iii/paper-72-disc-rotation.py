"""Specified Milky-Way-like asymmetric-drift toy model, not a data fit.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output basename to caller CWD.
Uses caller MPLCONFIGDIR unchanged; opaque white PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def circular_speed(r):
    return 220*np.tanh(r/1.5)

def stellar_speed(r):
    sigma = 30*np.exp(-(r-8)/14)
    speed_squared = circular_speed(r)**2-sigma**2*r*(1/2.6+1/7)
    if np.any(speed_squared < 0):
        raise ValueError('Tracer prescription has no real streaming speed here')
    return np.sqrt(speed_squared)

def main():
    r = np.linspace(0, 18, 700)
    rs = np.linspace(1, 18, 650)
    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=150, facecolor='white')
    ax.axvspan(0, 1, color='#dedede', alpha=0.65)
    ax.plot(r, circular_speed(r), color='#166996', lw=2.6, label='Cold gas: circular speed')
    ax.plot(rs, stellar_speed(rs), color='#b14e1b', lw=2.4, label='Stars: specified isotropic tracer')
    ax.axvline(8, color='#6b6b6b', lw=1, ls=':')
    ax.scatter([8, 8], [circular_speed(8), stellar_speed(np.array([8]))[0]], c=['#166996', '#b14e1b'], zorder=5)
    ax.annotate('At 8 kpc: 220 vs 211 km/s', xy=(8, stellar_speed(np.array([8]))[0]),
                xytext=(9.5, 158), fontsize=10, arrowprops={'arrowstyle':'->', 'color':'#777777'})
    ax.text(1.5, 53, r'$R_d=2.6$ kpc, $R_\sigma=7$ kpc'+'\n'+r'$\sigma(8\ {\rm kpc})=30$ km/s', fontsize=10)
    ax.set(xlim=(0, 18), ylim=(0, 255), xlabel='Galactocentric radius (kpc)',
           ylabel='Mean rotation speed (km/s)', title='Gas rotation and stellar asymmetric drift')
    ax.grid(alpha=0.2)
    ax.legend(loc='lower right', fontsize=9.5)
    fig.tight_layout()
    fig.savefig('paper-72-disc-rotation.png', facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
