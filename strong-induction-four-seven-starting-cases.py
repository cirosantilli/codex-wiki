"""Original batch-size example: four base totals and the step adding four. Output to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def representations(n):
    return [(a, b) for b in range(n // 7 + 1) for a in range(n // 4 + 1) if 4*a+7*b == n]


def main():
    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(12, 6.7), layout='constrained', facecolor='white')
    gs = fig.add_gridspec(2, 1, height_ratios=[3.8, 1.8])
    ax = fig.add_subplot(gs[0]); bottom = fig.add_subplot(gs[1])
    colors = ['#2465aa', '#9b4b86', '#287e59', '#bc6827']
    bases = [18, 19, 20, 21]
    labels = [r'$18=4+7+7$', r'$19=4+4+4+7$', r'$20=5\cdot4$', r'$21=3\cdot7$']
    for row, (base, color, label) in enumerate(zip(bases, colors, labels)):
        y = 3-row
        ax.text(-.95, y, label, ha='right', va='center', fontsize=13, color=color)
        for j in range(4):
            x = j*1.8
            ax.add_patch(FancyBboxPatch((x-.44, y-.24), .88, .48, boxstyle='round,pad=0.035', fc=color if j==0 else '#ffffff', ec=color, lw=2))
            ax.text(x, y, str(base+4*j), color='white' if j==0 else color, ha='center', va='center', fontsize=15)
            if j<3:
                ax.annotate('', (x+1.32,y), (x+.48,y), arrowprops={'arrowstyle':'->','color':color,'lw':1.5})
                ax.text(x+.9,y+.13,'+4',ha='center',va='bottom',fontsize=10,color=color)
        ax.text(6.2, y, r'$\cdots$', ha='left', va='center', fontsize=20, color=color)
    ax.set(xlim=(-3.35, 6.8), ylim=(-.5,3.6), title='One starting total for each remainder modulo four')
    ax.axis('off')
    for n in range(30):
        ok=bool(representations(n))
        if ok:bottom.scatter(n,0,c='#287e59',s=60,marker='o')
        else:bottom.scatter(n,0,c='#ad4141',s=55,marker='x',linewidths=1.7)
        bottom.text(n,-.29,str(n),ha='center',va='top',fontsize=9)
    bottom.axvspan(17.5,29.6,fc='#e6f2e9',zorder=-1)
    bottom.text(23.5,.4,'Every shown total from 18 is attainable',ha='center',fontsize=11)
    bottom.text(7.8,.4,'Circles: attainable; crosses: impossible',ha='center',fontsize=10)
    bottom.set(xlim=(-.6,29.6),ylim=(-.65,.7),title='Independent finite check for batches of four and seven')
    bottom.axis('off')
    fig.suptitle('Strong induction: four starts support a step that adds four', fontsize=17)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
