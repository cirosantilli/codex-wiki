"""Compare original nested-measurement predictions; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(9, 5.8), dpi=110, facecolor='white')
    fig.subplots_adjust(left=.12, right=.96, bottom=.27, top=.78)
    leaves = np.arange(3, 13)
    pots = np.arange(4, 17)
    total = np.linspace(12, 48, 200)
    ax.plot(4*leaves, 1+1/(4*leaves), 'o-', color='#17628c', lw=2.5,
            markersize=5, label='More leaves: four pots fixed')
    ax.plot(3*pots, 4/pots+1/(3*pots), 's-', color='#a3421d', lw=2.5,
            markersize=4, label='More pots: three leaves per pot')
    ax.plot(total, 5/total, '--', color='#646464', lw=2,
            label='False independence: 5 / measurement count')
    ax.axhline(1, color='#17628c', linestyle=':', lw=1.4)
    ax.text(33, .965, 'Four-pot limit = 1', color='#17628c', fontsize=10, va='top')
    ax.annotate('13/12: four pots, three leaves each', xy=(12,13/12),
                xytext=(17,1.19), fontsize=10, color='#233341',
                arrowprops={'arrowstyle':'->','color':'#233341'})
    ax.annotate('49/48', xy=(48,49/48), xytext=(43.5,1.09),
                fontsize=10, color='#17628c')
    ax.annotate('13/48', xy=(48,13/48), xytext=(43.5,.34),
                fontsize=10, color='#a3421d')
    ax.set(xlim=(11,49), ylim=(0,1.29), xticks=[12,24,36,48],
           xlabel='Measurements per treatment group',
           ylabel='Variance of the group mean (squared length units)')
    ax.grid(alpha=.18)
    ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='upper center', bbox_to_anchor=(.5,-.23), frameon=False, fontsize=9.5)
    fig.text(.5,.94,'Spend measurements on new pots or on more leaves?',
             ha='center',fontsize=17,weight='bold',color='#233341')
    fig.text(.5,.87,r'Constructed model: $\tau^2=4$, $\sigma^2=1$; '
             r'$\mathrm{Var}(\overline{Y})=4/n+1/(nm)$',
             ha='center',fontsize=12,color='#465461')
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
