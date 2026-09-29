"""Original digit/carry illustration; Python 3.14.4 / Matplotlib 3.10.7.

Run from _media; writes the matching basename.png to the working directory.
"""
from math import comb, factorial
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def digits(n, base):
    result = []
    while n:
        n, digit = divmod(n, base)
        result.append(digit)
    return result or [0]


def valuation(n, p):
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def carry_count(a, b, p):
    carry = total = 0
    while a or b or carry:
        a, da = divmod(a, p)
        b, db = divmod(b, p)
        carry = (da + db + carry) // p
        total += carry
    return total


def check():
    assert digits(50, 3) == [2, 1, 2, 1]
    assert sum(digits(50, 3)) == 6
    assert digits(17, 3) == [2, 2, 1]
    assert digits(33, 3) == [0, 2, 0, 1]
    assert carry_count(17, 33, 3) == 1
    number = comb(50, 17)
    assert number % 3 == 0 and number % 9 != 0
    assert [valuation(factorial(n), 3) for n in (50, 17, 33)] == [22, 6, 15]
    for p in (2, 3, 5, 7):
        for n in range(51):
            assert valuation(factorial(n), p) == (n - sum(digits(n, p))) // (p - 1)
            for k in range(n + 1):
                count = carry_count(k, n - k, p)
                deficit = sum(digits(k, p)) + sum(digits(n - k, p)) - sum(digits(n, p))
                assert deficit == (p - 1) * count
                assert valuation(comb(n, k), p) == count


def main():
    check()
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white',
                         'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.12, top=0.82, wspace=0.12)
    fig.suptitle('Base-three digits connect factorial factors and carries', fontsize=18, y=0.96)
    left, right = axes
    for ax in axes:
        ax.axis('off')
        ax.set(xlim=(-1.85, 3.7), ylim=(-1.5, 4.1))
    left.set_title(r'$50=(1212)_3$', fontsize=17, pad=13)
    left.text(-0.6, 3.6, '27', ha='center', color='#52616a')
    for x, label in zip((0.4, 1.4, 2.4), ('9', '3', '1')):
        left.text(x, 3.6, label, ha='center', color='#52616a')
    for x, d in zip((-0.6, 0.4, 1.4, 2.4), reversed(digits(50, 3))):
        left.add_patch(Rectangle((x - 0.4, 2.4), 0.8, 0.85,
                                 facecolor='#e5f0f7', edgecolor='white'))
        left.text(x, 2.82, str(d), ha='center', va='center', fontsize=24, color='#246a9c')
    left.text(0.9, 1.86, r'$d_3(50)=1+2+1+2=6$', ha='center', fontsize=15)
    left.text(0.9, 0.85, r'$v_3(50!)=\frac{50-6}{3-1}=22$', ha='center', fontsize=21)
    left.text(0.9, -0.25, 'Digit contributions to the valuation:', ha='center', fontsize=11)
    left.text(0.9, -0.85, r'$13+8+1+0=22$', ha='center', fontsize=16)

    right.set_title(r'$17+33=50$', fontsize=17, pad=13)
    xs = (-0.6, 0.4, 1.4, 2.4)
    for x, label in zip(xs, ('27', '9', '3', '1')):
        right.text(x, 3.6, label, ha='center', color='#52616a')
    for y, value, label in ((2.6, 17, '17'), (1.65, 33, '+ 33'), (0.5, 50, '= 50')):
        row = list(reversed(digits(value, 3) + [0] * (4 - len(digits(value, 3)))))
        right.text(-1.3, y, label, ha='right', va='center', fontsize=13)
        for x, d in zip(xs, row):
            right.text(x, y, str(d), ha='center', va='center', fontsize=24,
                       color='#246a9c' if value == 50 else '#26343d')
    right.plot([-0.95, 2.8], [1.05, 1.05], color='#88959e')
    right.add_patch(FancyArrowPatch((1.4, 2.98), (0.4, 2.98),
                                    connectionstyle='arc3,rad=0.5',
                                    arrowstyle='-|>', mutation_scale=15,
                                    color='#b86428', lw=2))
    right.text(0.4, 2.98, '1', ha='center', va='bottom', color='#b86428', fontsize=14)
    right.text(0.9, -0.28, 'One carry: 2 + 2 = 1 + 3', ha='center', fontsize=12, color='#9c4c18')
    right.text(0.9, -0.98, r'$v_3\binom{50}{17}=\frac{5+3-6}{2}=1$', ha='center', fontsize=19)
    fig.text(0.5, 0.045, 'Each base-three carry lowers the digit sum by 2.', ha='center', fontsize=13)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=100, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
