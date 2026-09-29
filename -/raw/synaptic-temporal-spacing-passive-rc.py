"""Original passive RC pulse comparison; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media. Chosen inputs, no active channels, spike generation, or reset.
Units: pF*mV/ms = pA; nS*mV = pA; pF/nS = ms.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CAPACITANCE = 200.0  # pF
LEAK = 10.0  # nS
REST = -65.0  # mV
AMPLITUDE = 300.0  # pA
DURATION = 5.0  # ms
TAU = CAPACITANCE / LEAK


def pulse_voltage(t, starts):
    """Exact convolution with rectangular currents, measured relative to rest."""
    voltage = np.zeros_like(t, dtype=float)
    for start in starts:
        elapsed = np.maximum(t - start, 0.0)
        voltage += AMPLITUDE / LEAK * (-np.expm1(-np.minimum(elapsed, DURATION) / TAU)) * np.exp(-np.maximum(elapsed - DURATION, 0.0) / TAU)
    return voltage


def main():
    t = np.linspace(0, 110, 11001)
    fig, axes = plt.subplots(2, 2, figsize=(10, 6), sharex=True, sharey='row', layout='constrained')
    for column, (starts, label, color) in enumerate([([10, 15, 20], '5 ms onset spacing', '#1565c0'), ([10, 40, 70], '30 ms onset spacing', '#c45c10')]):
        current = sum(AMPLITUDE * ((t >= start) & (t < start + DURATION)) for start in starts)
        axes[0, column].step(t, current, where='post', color=color, lw=2)
        axes[0, column].set_title(label)
        voltage = REST + pulse_voltage(t, starts)
        axes[1, column].plot(t, voltage, color=color, lw=2.2)
        axes[1, column].axhline(-50, color='0.35', ls='--', lw=1.2, label='Illustrative threshold; no firing rule')
        peak = voltage.max()
        axes[1, column].text(0.97, 0.45, f'Peak {peak:.2f} mV', transform=axes[1, column].transAxes, ha='right', va='bottom')
        axes[1, column].set_xlabel('Time (ms)')
        axes[1, column].set_ylim(-66, -46)
        axes[0, column].set_ylim(-20, 340)
        for ax in axes[:, column]:
            ax.grid(alpha=0.18)
            ax.set_xlim(0, 110)
    axes[0, 0].set_ylabel('Imposed inward current (pA)')
    axes[1, 0].set_ylabel('Passive membrane voltage (mV)')
    axes[1, 0].legend(fontsize=8, loc='upper right')
    fig.suptitle('Passive temporal integration: same charge, different spacing\nC = 200 pF; leak = 10 nS; rest = −65 mV; τ = 20 ms', fontsize=13)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
