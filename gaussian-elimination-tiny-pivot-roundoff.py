"""Three-significant-decimal-digit model, evaluated with exact fractions.

Python 3.14, matplotlib 3.10.7. Run from _media; the PNG uses this basename.
Only presentation converts exact model values to Python floats.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def fl3(value):
    """Nearest three-significant-digit decimal float, ties to even.

    Exponents are unbounded. Fractions encode the toy floats exactly;
    this avoids an additional binary rounding operation in the model.
    """
    value = Fraction(value)
    if not value:
        return Fraction(0)
    magnitude = abs(value)
    scale = Fraction(1)
    while magnitude < scale:
        scale /= 10
    while magnitude >= 10 * scale:
        scale *= 10
    spacing = scale / 100
    scaled = magnitude / spacing
    integer, remainder = divmod(scaled.numerator, scaled.denominator)
    twice = 2 * remainder
    if twice > scaled.denominator or (twice == scaled.denominator and integer % 2):
        integer += 1
    return (1 if value > 0 else -1) * integer * spacing


def solve(pivot):
    """Round inputs, each primitive operation, and each stored result."""
    eps = Fraction(1, 10**6)
    rows = [[fl3(v) for v in row] for row in [[eps, 1, 1], [1, 1, 2]]]
    if pivot:
        rows[0], rows[1] = rows[1], rows[0]
    original = [row[:] for row in rows]
    multiplier = fl3(rows[1][0] / rows[0][0])
    exact_updates = [rows[1][j] - fl3(multiplier * rows[0][j]) for j in (1, 2)]
    for j in range(3):
        rows[1][j] = fl3(rows[1][j] - fl3(multiplier * rows[0][j]))
    x2 = fl3(rows[1][2] / rows[1][1])
    x1 = fl3(fl3(rows[0][2] - fl3(rows[0][1] * x2)) / rows[0][0])
    residual = [1 - (eps*x1 + x2), 2 - (x1 + x2)]
    true = [1 / (1-eps), (1-2*eps) / (1-eps)]
    relative_error = max(abs(a-b) for a, b in zip([x1, x2], true)) / max(map(abs, true))
    relative_residual = max(map(abs, residual)) / 2
    return dict(multiplier=multiplier, initial=original, rows=rows,
                exact_updates=exact_updates, solution=[x1, x2], residual=residual,
                relative_error=relative_error, relative_residual=relative_residual)


def main():
    results = [solve(False), solve(True)]
    plt.rcParams.update({'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(11, 7.1), facecolor='white')
    fig.suptitle('A tiny pivot can destroy a well-conditioned solve',
                 fontsize=19, y=.97, color='#20364a')
    fig.text(.5, .91, 'A = [[10⁻⁶, 1], [1, 1]]     b = [1, 2]'
             '     |     Three decimal significant digits after every operation',
             ha='center', fontsize=12, color='#526475')
    headings = ['Keep the tiny first pivot', 'Swap rows: partial pivoting']
    colors = ['#bc573f', '#247d66']
    details = [
        [r'Pivot $10^{-6}$; multiplier $10^6$',
         'Exact updated row: [0, −999999 | −999998]',
         'Rounded row: [0, −1000000 | −1000000]',
         'The coefficient and RHS become indistinguishable.',
         r'$\widehat{x}_2=1,\quad\widehat{x}_1=(1-1)/10^{-6}=0$',
         r'$\widehat{x}=(0,1)^T,\quad r=(0,1)^T$'],
        [r'Pivot $1$; multiplier $10^{-6}$',
         'Exact updated row: [0, 0.999999 | 0.999998]',
         'Rounded row: [0, 1.00 | 1.00]',
         'No million-sized intermediate entries.',
         r'$\widehat{x}_2=1,\quad\widehat{x}_1=(2-1)/1=1$',
         r'$\widehat{x}=(1,1)^T,\quad r=(-10^{-6},0)^T$']]
    for k in range(2):
        ax = fig.add_axes([.055+.475*k, .46, .435, .40])
        ax.axis('off')
        ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle='round,pad=.015',
                                   facecolor='#f5f7f9', edgecolor=colors[k],
                                   linewidth=1.3, transform=ax.transAxes, clip_on=False))
        ax.text(.5, .91, headings[k], ha='center', fontsize=15, color=colors[k])
        for j, line in enumerate(details[k]):
            ax.text(.5, .76-.13*j, line, ha='center', fontsize=12 if j != 3 else 10,
                    color='#20364a')
    ax = fig.add_axes([.15, .15, .76, .23])
    y = [1, 0]
    for k, result in enumerate(results):
        values = [float(result['relative_error']), float(result['relative_residual'])]
        ax.barh([v+.14 if k == 0 else v-.14 for v in y], values,
                height=.24, color=colors[k], label=['No row swap', 'Partial pivoting'][k])
        for j, value in enumerate(values):
            text = [['1', '1/2'], ['10⁻⁶', '5 × 10⁻⁷']][k][j]
            ax.text(value*1.18, y[j]+(.14 if k == 0 else -.14), text,
                    va='center', fontsize=11, color=colors[k])
    ax.set_xscale('log')
    ax.set_xlim(1e-8, 5)
    ax.set_yticks(y, ['Relative solution error', 'Relative residual'])
    ax.set_xlabel('Maximum-norm diagnostics, evaluated in exact arithmetic', fontsize=11)
    ax.grid(axis='x', alpha=.18)
    ax.set_axisbelow(True)
    ax.spines[['right', 'top', 'left']].set_visible(False)
    ax.legend(loc='upper left', bbox_to_anchor=(.28, 1.28), ncols=2, frameon=False, fontsize=10)
    fig.text(.5, .025, 'Toy arithmetic model, not hardware measurements. '
             'True solution ≈ (1.000001000001, 0.999998999999).',
             ha='center', fontsize=11, color='#526475')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
