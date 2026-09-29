"""Show the first sieve pass responsible for each composite through 100."""

from math import isqrt
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


def sieve(limit):
    smallest = [0]*(limit+1)
    for p in range(2, isqrt(limit)+1):
        if smallest[p]:
            continue
        for n in range(p*p, limit+1, p):
            if not smallest[n]:
                smallest[n] = p
    return smallest


def trial_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n)+1))


def main():
    smallest = sieve(100)
    primes = [n for n in range(2, 101) if not smallest[n]]
    assert len(primes) == 25 and primes[-1] == 97
    for n in range(2, 101):
        assert (smallest[n] == 0) == trial_prime(n)
        if smallest[n]:
            p = smallest[n]
            assert n % p == 0 and p <= isqrt(n)
            assert p == next(d for d in range(2, n) if n % d == 0)
    assert smallest[49] == 7 and smallest[91] == 7
    assert 2*3*5*7*11*13+1 == 30031 == 59*509
    assert trial_prime(59) and trial_prime(509)
    colors = {0:'#d6ecd7', 2:'#d6e6f3', 3:'#f3dfc3', 5:'#e5daf0', 7:'#f0d6d6'}
    fig, ax = plt.subplots(figsize=(9.2, 8), dpi=120, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 10), aspect='equal')
    ax.axis('off')
    for n in range(1, 101):
        col = (n-1) % 10
        row = 9-(n-1)//10
        face = '#eeeeee' if n == 1 else colors[smallest[n]]
        ax.add_patch(Rectangle((col+.04,row+.04),.92,.92,
                              facecolor=face, edgecolor='white', lw=1.5))
        ax.text(col+.5,row+.51,str(n),ha='center',va='center',fontsize=13,
                fontweight='bold' if n in primes else 'normal',
                color='#235e32' if n in primes else '#303840')
        if n == 1:
            ax.plot([col+.2,col+.8],[row+.2,row+.8],color='#8b8b8b',lw=1)
    fig.suptitle('Sieve through 100: remove multiples, retain primes',fontsize=17,y=.975)
    handles = [Patch(facecolor=colors[0],label='Prime (25 survivors)'),
               Patch(facecolor='#eeeeee',label='1: excluded')]
    handles += [Patch(facecolor=colors[p],label=f'First removed by {p}') for p in [2,3,5,7]]
    fig.legend(handles=handles,loc='lower center',ncol=3,frameon=False,
               bbox_to_anchor=(.5,.015),fontsize=11)
    fig.subplots_adjust(top=.9,bottom=.135,left=.08,right=.92)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
