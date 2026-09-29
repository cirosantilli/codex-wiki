"""Original passive compartment and conductance comparisons.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
Exact constant-coefficient solutions, pF / nS = ms, nS * mV = pA.
No active channels, firing/reset, fitted physiology, or cable approximation.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def compartment_voltage(t, currents):
    # Deviations from -65 mV; soma and dendrite each C=100 pF, leak=5 nS.
    # Axial coupling 10 nS. Eigenvalues of K/C set both decay rates.
    k = np.array([[15., -10.], [-10., 15.]])
    rates, vectors = np.linalg.eigh(k / 100.)
    steady = np.linalg.solve(k, np.asarray(currents, dtype=float))
    on = np.maximum(t - 10., 0.)
    duration = np.minimum(on, 50.)
    after = np.maximum(on - 50., 0.)
    modal = vectors.T @ steady
    response = vectors @ (modal[:, None] * (-np.expm1(-rates[:, None] * duration)) * np.exp(-rates[:, None] * after))
    return response


def conductance_voltage(t, ge, gi=0.):
    # Excitatory reversal 0 mV; shunt reversal and leak reversal -65 mV.
    total = 10. + ge + gi
    steady_rise = 65. * ge / total
    on = np.maximum(t - 10., 0.)
    duration = np.minimum(on, 50.)
    after = np.maximum(on - 50., 0.)
    return steady_rise * (-np.expm1(-duration * total / 200.)) * np.exp(-after * 10. / 200.)


def main():
    t = np.linspace(0, 100, 10001)
    pulse = ((t >= 10.) & (t < 60.)).astype(float)
    fig, axes = plt.subplots(2, 3, figsize=(12, 6.4), layout='constrained')
    schematic = axes[0, 0]
    schematic.set_axis_off()
    schematic.set_xlim(0, 1)
    schematic.set_ylim(0, 1)
    for x, label in [(0.24, 'Soma'), (0.76, 'Dendrite')]:
        schematic.text(x, 0.62, label, ha='center', bbox={'boxstyle': 'round,pad=0.5', 'fc': 'white', 'ec': '#1565c0'})
        schematic.annotate('100 pA', (x, 0.7), (x, 0.92), ha='center', arrowprops={'arrowstyle': '->'})
        schematic.text(x, 0.37, 'C = 100 pF\nleak = 5 nS', ha='center', fontsize=9)
    schematic.plot([0.37, 0.63], [0.62, 0.62], color='0.3', lw=2)
    schematic.text(0.5, 0.5, '10 nS', ha='center')
    schematic.text(0.5, 0.13, 'Steps: 10–60 ms; rest −65 mV\nSoma alone, dendrite alone, or both', ha='center', fontsize=9)
    schematic.set_title('A. Locations with fixed current inputs')
    for currents, label, color in [([100, 0], 'Soma input', '#1565c0'), ([0, 100], 'Dendrite input', '#c45c10'), ([100, 100], 'Both: exact sum', '#178346')]:
        axes[1, 0].plot(t, -65 + compartment_voltage(t, currents)[0], label=label, color=color, lw=2)
    axes[1, 0].set_ylabel('Passive somatic voltage (mV)')
    axes[0, 1].step(t, 2 * pulse, where='post', color='#1565c0', lw=2, label='Each input: 2 nS')
    axes[0, 1].step(t, 4 * pulse, where='post', color='#c45c10', lw=2, label='Joint excitation: 4 nS')
    axes[0, 1].set_title('B. One compartment, two conductances')
    axes[1, 1].plot(t, -65 + 2 * conductance_voltage(t, 2), ls='--', color='0.4', lw=2, label='Sum of separate voltage changes')
    axes[1, 1].plot(t, -65 + conductance_voltage(t, 4), color='#c45c10', lw=2, label='Joint conductance response')
    axes[0, 2].step(t, 4 * pulse, where='post', color='#c45c10', lw=2, label='Excitation: 4 nS')
    axes[0, 2].step(t, 20 * pulse, where='post', color='#7b3294', lw=2, label='Shunt: 20 nS, reversal −65 mV')
    axes[0, 2].set_title('C. Same excitation, added shunt')
    axes[1, 2].plot(t, -65 + conductance_voltage(t, 4), color='#c45c10', lw=2, label='Excitation alone')
    axes[1, 2].plot(t, -65 + conductance_voltage(t, 4, 20), color='#7b3294', lw=2, label='Excitation + shunt')
    for col in range(3):
        axes[1, col].set_ylim(-66, -42)
        axes[1, col].set_xlabel('Time (ms)')
        for row in range(2):
            if col == 0 and row == 0:
                continue
            axes[row, col].set_xlim(0, 100)
            axes[row, col].grid(alpha=0.18)
            axes[row, col].legend(fontsize=7.6, loc='upper right')
    for ax in axes[0, 1:]:
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Activated conductance (nS)')
    axes[1, 1].legend(fontsize=7.6, loc='lower left')
    axes[0, 1].set_ylim(-0.3, 5.5)
    axes[0, 2].set_ylim(-1, 25)
    fig.suptitle('Passive integration: location, driving force and shunting\nB–C: C = 200 pF, leak = 10 nS, rest = −65 mV, excitatory reversal = 0 mV; no spikes', fontsize=13)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
