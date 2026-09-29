"""Original adaptive Euler-Heun computation and local/global error comparison.

Emits its basename PNG in CWD. Tested with Python 3.14, matplotlib 3.10.7,
numpy 2.3.5. No external solver or data; all defects use the exact exponential.
"""
from pathlib import Path
import math
import matplotlib.pyplot as plt
import numpy as np


def integrate(atol=1e-3, end=4.0):
    """Return all trial records; rejected trials never alter the accepted state."""
    t, y, h = 0.0, 1.0, 0.2
    trials = []
    while t < end:
        h = min(h, end - t)
        if t + h == t:
            raise ArithmeticError('Step no longer advances time')
        k1 = y
        k2 = y + h * k1
        output = y + h * (k1 + k2) / 2
        difference = h * (k2 - k1) / 2
        scaled = abs(difference) / atol
        accepted = scaled <= 1
        # expm1 reduces cancellation in the known local defect.
        local = abs(y * (math.expm1(h) - h - h*h/2))
        global_error = abs(math.exp(t + h) - output)
        trials.append({'t': t, 'h': h, 'start': y, 'output': output,
                       'estimate': scaled, 'local': local / atol,
                       'global': global_error / atol, 'accepted': accepted})
        if accepted:
            t, y = t + h, output
        factor = 2.0 if scaled == 0 else min(2.0, max(0.2, 0.9 / math.sqrt(scaled)))
        h *= factor
    return trials


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white'})
    trials = integrate()
    accepted = [r for r in trials if r['accepted']]
    rejected = [r for r in trials if not r['accepted']]
    fig, (steps, errors) = plt.subplots(1, 2, figsize=(11, 4.8), layout='constrained')
    steps.semilogy([r['t'] for r in accepted], [r['h'] for r in accepted],
                   '.-', ms=3, lw=1, color='#2675ad', label='Accepted steps')
    steps.scatter([r['t'] for r in rejected], [r['h'] for r in rejected],
                  marker='x', s=65, color='#b35412', label='Rejected trial', zorder=5)
    steps.annotate('Retry at the same time\n$h=0.0402492$, $E=0.81$',
                   xy=(0, accepted[0]['h']), xytext=(.35, .095),
                   arrowprops={'arrowstyle': '->'}, fontsize=10)
    steps.annotate('Final step capped\nat $t=4$', xy=(accepted[-1]['t'], accepted[-1]['h']),
                   xytext=(2.65, .012), arrowprops={'arrowstyle': '->'}, fontsize=10)
    steps.set(xlabel='Accepted starting time $t_n$', ylabel='Trial step size $h_n$',
              title=f"{len(accepted)} accepted steps; {len(rejected)} rejection")
    steps.legend(loc='upper right', fontsize=10)
    index = np.arange(1, len(accepted) + 1)
    for key, label, color in [('estimate', 'Accepted pair estimate $|d|/s$', '#2675ad'),
                              ('local', 'Actual Heun local defect / $s$', '#268544'),
                              ('global', 'Actual accumulated global error / $s$', '#a03977')]:
        errors.semilogy(index, [r[key] for r in accepted], color=color, lw=1.8, label=label)
    errors.axhline(1, color='black', ls='--', lw=1, label='Local acceptance level')
    errors.annotate(f"Endpoint: {accepted[-1]['global']:.4f}$s$",
                    xy=(len(accepted), accepted[-1]['global']), xytext=(160, 28),
                    arrowprops={'arrowstyle': '->'}, color='#a03977', fontsize=10)
    errors.set(xlabel='Accepted-step number', ylabel='Error / absolute tolerance $s$',
               title='Passing local tests gives no global guarantee', ylim=(5e-5, 100))
    errors.legend(loc='lower left', fontsize=9)
    for ax in (steps, errors):
        ax.grid(alpha=.2, which='both')
    fig.suptitle(r"Euler-Heun on $y'=y$, $0\leq t\leq4$: $s=10^{-3}$, accept Heun", fontsize=14)
    fig.savefig(Path(__file__).stem + '.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
