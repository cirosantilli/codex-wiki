"""Plot binary-channel information and joint probabilities; save to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def binary_entropy(q):
    q = np.asarray(q, dtype=float)
    out = np.zeros_like(q)
    interior = (q > 0) & (q < 1)
    p = q[interior]
    out[interior] = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    return out


def main():
    q = np.linspace(0, 1, 801)
    h = binary_entropy(q)
    assert np.allclose(binary_entropy([0, .5, 1]), [0, 1, 0])
    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(11, 7.2), layout='constrained', facecolor='white')
    grid = fig.add_gridspec(2, 3, height_ratios=[1.7, 1])
    ax = fig.add_subplot(grid[0, :])
    ax.plot(q, h, color='#d87921', linewidth=2.5, label='Error uncertainty: H(Y|X) = h2(q)')
    ax.plot(q, 1-h, color='#2563a6', linewidth=2.5, label='Retained information: I(X;Y) = 1 - h2(q)')
    chosen_q = .1
    chosen_i = float(1 - binary_entropy([chosen_q])[0])
    ax.scatter([chosen_q], [chosen_i], color='#2563a6', zorder=3)
    ax.annotate('q = 0.1: %.3f bits retained' % chosen_i, (chosen_q, chosen_i),
                xytext=(.18, .68), arrowprops={'arrowstyle': '->'}, fontsize=10)
    ax.set(xlabel='Bit-flip probability q', ylabel='Bits per channel use',
           xlim=(0, 1), ylim=(-.03, 1.16), title='A fair input bit: random errors lose information, certain flips do not')
    ax.grid(alpha=.2)
    ax.legend(loc='upper center', fontsize=10)
    for i, noise in enumerate([0, .5, 1]):
        a = fig.add_subplot(grid[1, i])
        joint = .5 * np.array([[1-noise, noise], [noise, 1-noise]])
        a.imshow(joint, vmin=0, vmax=.5, cmap='Blues')
        for x in range(2):
            for y in range(2):
                a.text(y, x, '%.2f' % joint[x, y], ha='center', va='center',
                       color='white' if joint[x, y] > .3 else '#142738', fontsize=15)
        a.set(xticks=[0, 1], yticks=[0, 1], xlabel='Output Y', ylabel='Input X',
              title=['q = 0: unchanged', 'q = 0.5: independent', 'q = 1: inverted'][i])
    fig.suptitle('Joint probabilities P(X,Y) below; both marginals remain fair', fontsize=14)
    fig.savefig(Path.cwd() / 'binary-channel-information.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
