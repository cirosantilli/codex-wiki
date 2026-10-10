"""Original ideal event readout for a stipulated recovery rule; no voltage trace.

Tested: Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Output matching basename.png in cwd. Each row is an independently reset trial.
Conditioning success at time zero is assumed; successful tests emit at onset.
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HOLD_MS = 2.0
TAU_MS = 3.0
BASE_NA = 0.2
EXCESS = 2.0
TEST_NA = 0.35
WIDTH_MS = 0.2


def required_current(delay_ms):
    if delay_ms < HOLD_MS:
        return np.inf
    return BASE_NA * (1 + EXCESS*np.exp(-(delay_ms-HOLD_MS)/TAU_MS))


def test_passes(delay_ms, current_na=TEST_NA):
    if delay_ms < HOLD_MS:
        return False
    required = required_current(delay_ms)
    # Include mathematical equality despite a few ULPs of floating-point error.
    return current_na >= required or math.isclose(
        current_na, required, rel_tol=4*np.finfo(float).eps, abs_tol=0.0)


def pulse(ax, start, height, color):
    ax.plot([start, start, start+WIDTH_MS, start+WIDTH_MS],
            [0, height, height, 0], color=color, lw=2.3)


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig, axes = plt.subplots(3, 2, figsize=(10.0, 6.1), sharex=True,
                             gridspec_kw={'width_ratios': [1.05, 1]}, layout='constrained')
    fig.set_facecolor('white')
    blue, orange = '#225f91', '#a74321'
    for row, delta in enumerate([1.0, 4.0, 6.0]):
        inp, out = axes[row]
        for ax in [inp, out]:
            ax.set_facecolor('white')
            ax.axvspan(0, HOLD_MS, color='#eeeeee', zorder=0)
            ax.spines[['top', 'right']].set_visible(False)
            ax.set_xlim(-0.5, 8)
            ax.set_xticks([0, 2, 4, 6, 8])
        inp.plot([-0.5, 8], [0, 0], color='#444444', lw=1)
        pulse(inp, 0, 0.65, blue)
        pulse(inp, delta, TEST_NA, orange)
        inp.set_ylim(-0.04, 0.88)
        inp.set_yticks([0, 0.35, 0.65])
        inp.set_ylabel('Current (nA)')
        inp.set_title(f'Delay Δ = {delta:g} ms', loc='left', fontsize=12)
        if row == 0:
            inp.text(0.3, 0.73, 'Conditioning', color=blue, fontsize=10)
            inp.text(1.4, 0.38, 'Test: 0.35 nA', color=orange, fontsize=10)
        out.set_ylim(0, 1.55)
        out.set_yticks([])
        out.spines['left'].set_visible(False)
        out.hlines(0.55, -0.5, 8, color='#aaaaaa', lw=1)
        out.vlines(0, 0.35, 1.0, color=blue, lw=3)
        out.text(0.2, 1.05, 'Conditioning event', color=blue, fontsize=10)
        if test_passes(delta):
            out.vlines(delta, 0.35, 1.0, color=orange, lw=3)
            out.text(delta, 1.05, 'Test event', color=orange, ha='center', fontsize=10)
            reason = f'Pass: 0.35 ≥ {required_current(delta):.3f} nA'
        else:
            out.plot(delta, 0.55, marker='x', color=orange, ms=9, mew=2)
            reason = ('Fails during absolute hold' if delta < HOLD_MS else
                      f'Fails: 0.35 < {required_current(delta):.3f} nA')
        out.text(7.9, 0.12, reason, ha='right', color=orange, fontsize=11)
    axes[-1, 0].set_xlabel('Pulse onset time (ms)')
    axes[-1, 1].set_xlabel('Ideal event time (ms)')
    fig.suptitle('Paired-pulse readout: equal tests, different outcomes', fontsize=16)
    fig.supxlabel('Rectangles: imposed pulses. Ticks: events. Crosses: failed tests. Grey: chosen 2 ms hold.', fontsize=10)
    axes[0, 1].set_title('Abstract event readout; not membrane voltage', loc='left', fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120,
                facecolor='white', bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
