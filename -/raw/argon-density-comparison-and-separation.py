"""Draw a functional gas-comparison/separation diagram; emit PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(13, 6.4), dpi=120, facecolor='white')
    ax.set(xlim=(0, 14), ylim=(0, 7.5))
    ax.axis('off')
    fig.subplots_adjust(left=.015, right=.985, bottom=.09, top=.90)
    fig.suptitle('Gas preparation, controlled weighing, and separation', fontsize=18, y=.97)

    def box(x, y, width, height, text, color='#edf4fa'):
        ax.add_patch(FancyBboxPatch((x,y), width,height, boxstyle='round,pad=0.10',
                                   facecolor=color, edgecolor='#34495e', linewidth=1.6))
        ax.text(x+width/2,y+height/2,text,ha='center',va='center',linespacing=1.5)

    def arrow(start,end, color='#34495e'):
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,
                                    color=color,linewidth=1.7))

    box(.4,5.8,3.1,1.15,'Air after removal\nof oxygen')
    box(.4,3.65,3.1,1.15,'Nitrogen prepared\nfrom chemical sources')
    box(5.05,4.45,3.7,2.45,'Same globe volume\nSame pressure\nSame temperature\nCompare gas masses', '#e8f4ed')
    arrow((3.65,6.35),(4.91,6.15))
    arrow((3.65,4.22),(4.91,4.95))
    box(10.15,4.75,3.3,1.85,'Repeatable difference:\nwhat differs between\nthe samples?', '#fff0dc')
    arrow((8.90,5.65),(10.01,5.65))
    box(5.05,.65,3.7,1.85,'Circulation over\nheated magnesium\nremoves nitrogen', '#f5ecdf')
    arrow((6.90,4.30),(6.90,2.64))
    ax.text(7.20,3.45,'Separate a\nremaining component',va='center',fontsize=11)
    box(10.15,.65,3.3,1.85,'Concentrated residue\nCheck its spectrum\nand remaining nitrogen', '#e8f4ed')
    arrow((8.90,1.58),(10.01,1.58))
    ax.text(1.95,1.8,'Weighing suggests\na composition question.\nSeparation supplies\na different test.',ha='center',va='center',fontsize=12)
    fig.text(.5,.025,'Functional summary, not a scale reconstruction. No measured masses or spectra are plotted.',
             ha='center',fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'),facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
