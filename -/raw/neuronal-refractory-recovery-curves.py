"""Original stipulated paired-pulse recovery; never experimental data.

Tested: Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Output matching basename.png in the current working directory.
Units: ms and nA. The absolute hold and scalar recovery are imposed rules,
not sodium/potassium channel dynamics or a Hodgkin-Huxley simulation.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HOLD_MS = 2.0
TAU_MS = 3.0
BASE_NA = 0.2
EXCESS = 2.0


def required_current(delay_ms):
    delay_ms = np.asarray(delay_ms, dtype=float)
    return np.where(delay_ms < HOLD_MS, np.inf,
                    BASE_NA * (1 + EXCESS * np.exp(-(delay_ms-HOLD_MS)/TAU_MS)))


def earliest_delay(current_na):
    if current_na <= BASE_NA:
        return np.inf
    return HOLD_MS + max(0.0, TAU_MS*np.log(EXCESS/(current_na/BASE_NA-1)))


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(9.2, 5.5), layout='constrained')
    fig.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axvspan(0, HOLD_MS, color='#e6e6e6')
    delay = np.linspace(HOLD_MS, 16, 700)
    ax.plot(delay, required_current(delay), color='#225f91', lw=2.8,
            label='Required amplitude after the hold')
    ax.scatter([HOLD_MS], [0.6], color='#225f91', s=35, zorder=5)
    ax.axhline(BASE_NA, color='#666666', ls='--', lw=1.5)
    ax.text(15.7, 0.182, 'Asymptotic baseline: 0.2 nA', ha='right', va='top', fontsize=11)
    for amplitude, color, label_y in [(0.35, '#a74321', 0.27), (0.5, '#267550', 0.55)]:
        first = earliest_delay(amplitude)
        ax.axhline(amplitude, color=color, lw=1.5, ls=':')
        ax.scatter([first], [amplitude], color=color, s=55, zorder=6)
        ax.plot([first, first], [0.13, amplitude], color=color, lw=1, ls='--')
        ax.annotate(f'{amplitude:g} nA test\nFirst passes at {first:.3f} ms',
                    xy=(first, amplitude), xytext=(8.8, label_y),
                    arrowprops={'arrowstyle': '->', 'color': color}, color=color,
                    bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 3})
    ax.text(1.0, 0.54, 'Absolute\nhold\n\nNo second\nevent', ha='center', va='center', fontsize=11,
            bbox={'facecolor': '#e6e6e6', 'edgecolor': 'none', 'pad': 3})
    ax.text(9.5, 0.63, r'$I_{\rm req}=0.2[1+2e^{-(\Delta-2)/3}]$ nA', ha='center', fontsize=13)
    ax.set(xlim=(0, 16), ylim=(0.13, 0.69),
           xlabel='Delay from conditioning event, Δ (ms)',
           ylabel='Test-pulse amplitude (nA)')
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', color='#eeeeee')
    ax.set_axisbelow(True)
    fig.suptitle('Paired-pulse recovery: an imposed example', fontsize=17)
    ax.set_title('Chosen 2 ms hold; 3 ms recovery constant; fixed 0.2 ms pulse width', fontsize=11, pad=13)
    fig.text(0.99, -0.025, 'Original phenomenological rule — not recordings or a channel simulation',
             ha='right', fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120,
                facecolor='white', bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
