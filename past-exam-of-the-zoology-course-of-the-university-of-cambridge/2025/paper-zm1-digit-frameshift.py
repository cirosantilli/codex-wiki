"""Original diagram of the classical identity-shift model.
Python 3.14, matplotlib 3.10. Output is a basename in the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROMAN = ('I', 'II', 'III', 'IV', 'V')
MAPPING = {2: 1, 3: 2, 4: 3}


def main():
    fig, ax = plt.subplots(figsize=(10.7, 5.3), layout='constrained')
    blue, green, gray = '#245b94', '#167248', '#aab5bf'
    for i, r in enumerate(ROMAN, 1):
        ax.text(i, 3.55, r, ha='center', va='center', fontsize=13, color='#48515a')
        ax.text(i, 2.9, 'C'+r, ha='center', va='center', fontsize=13,
                color=blue if i in MAPPING else gray,
                bbox={'boxstyle': 'round,pad=.45', 'fc': '#eaf2fa' if i in MAPPING else 'white',
                      'ec': blue if i in MAPPING else gray,
                      'ls': '-' if i in MAPPING else ':'})
        if i in MAPPING:
            identity = 'D'+ROMAN[MAPPING[i]-1]
            ax.annotate('', xy=(i, 1.65), xytext=(i, 2.5),
                        arrowprops={'arrowstyle': '-|>', 'color': green, 'lw': 2})
            ax.text(i, 1.25, identity, ha='center', va='center', fontsize=15, weight='bold',
                    color=green, bbox={'boxstyle': 'round,pad=.5', 'fc': '#edf7f0', 'ec': green})
    ax.text(-.3, 3.55, 'Five-position\nreference', va='center', fontsize=11)
    ax.text(-.3, 2.9, 'Condensation\nposition', va='center', fontsize=11, color=blue)
    ax.text(-.3, 1.25, 'Proposed\ndigit identity', va='center', fontsize=11, color=green)
    ax.annotate('Anterior', xy=(.8, 4.03), xytext=(1.9, 4.03), ha='center', va='center',
                fontsize=10, arrowprops={'arrowstyle': '->', 'color': gray})
    ax.annotate('Posterior', xy=(5.2, 4.03), xytext=(4.1, 4.03), ha='center', va='center',
                fontsize=10, arrowprops={'arrowstyle': '->', 'color': gray})
    ax.text(2.8, .25, 'Classical model: identities I–II–III at positions II–III–IV',
            ha='center', fontsize=12, weight='bold')
    ax.text(2.8, -.17, 'Regulatory identity changes; formed digits do not physically slide sideways.',
            ha='center', fontsize=10, color='#48515a')
    ax.set(xlim=(-.6, 5.7), ylim=(-.6, 4.5))
    ax.axis('off')
    ax.set_title('Position and identity are distinct claims', fontsize=17, weight='bold', pad=15)
    fig.savefig('paper-zm1-digit-frameshift.png', dpi=150, facecolor='white')
    plt.close(fig)

if __name__ == '__main__':
    main()
