"""Original one-step replication diagram; tested with Python 3.14.4.

Uses matplotlib 3.10.7. Run from _media to save the PNG in that directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    stock = Fraction(100)
    up, down = Fraction(120), Fraction(80)
    gross = Fraction(21, 20)
    payoff_up, payoff_down = Fraction(20), Fraction(0)
    delta = (payoff_up - payoff_down) / (up - down)
    cash = (payoff_down - delta * down) / gross
    price = delta * stock + cash
    q = (gross * stock - down) / (up - down)
    assert delta == Fraction(1, 2) and cash == Fraction(-800, 21)
    assert price == Fraction(250, 21) and q == Fraction(5, 8)
    assert delta * up + gross * cash == payoff_up
    assert delta * down + gross * cash == payoff_down
    plt.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots(figsize=(10, 5.8), facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis('off')
    fig.suptitle('One call = half a share + a bank-account debt', fontsize=17, y=.97)
    ax.text(5, 5.9, 'One period · no dividends · strike K = 100 · bank growth R = 1.05',
            ha='center', va='top', fontsize=12, color='#444444')
    box = {'boxstyle': 'round,pad=.7', 'facecolor': '#f4f7fa',
           'edgecolor': '#2563a6', 'linewidth': 1.5}
    ax.text(1.9, 3.05,
            'TODAY\n\nStock: 100\nHalf a share costs: 50\nInitial cash: −800/21\n(borrow ≈ 38.09524)\n\nNet cost: 250/21\n≈ 11.90476',
            ha='center', va='center', linespacing=1.4, bbox=box)
    for y, label, terminal, share_value, payoff in [
        (4.5, 'UP STATE', 120, 60, 20),
        (1.45, 'DOWN STATE', 80, 40, 0),
    ]:
        ax.annotate('', xy=(6.35, y), xytext=(3.55, 3.05),
                    arrowprops={'arrowstyle': '->', 'color': '#687b8b', 'lw': 2})
        ax.text(7.8, y,
                f'{label}\nStock: {terminal}\nHalf a share: {share_value}\nBank debt: −40\nPortfolio: {share_value} − 40 = {payoff}\nCall: max({terminal} − 100, 0) = {payoff}',
                ha='center', va='center', linespacing=1.4,
                bbox={**box, 'facecolor': '#f4f9f4', 'edgecolor': '#327b50'})
    ax.text(4.9, 4.5, 'Pricing weight\nq = 5/8', ha='center', fontsize=11)
    ax.text(4.9, 1.5, 'Pricing weight\n1 − q = 3/8', ha='center', fontsize=11)
    ax.text(5, -.03, 'The debt grows to 40 in either state; replication matches each payoff exactly.',
            ha='center', va='bottom', fontsize=12)
    fig.subplots_adjust(left=.015, right=.985, bottom=.08, top=.87)
    fig.savefig(Path.cwd() / 'binomial-option-replication.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
