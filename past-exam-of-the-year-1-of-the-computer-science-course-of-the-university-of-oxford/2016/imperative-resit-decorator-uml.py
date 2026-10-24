"""Cable-TV decorator UML. Python 3.14; matplotlib 3.10.7; writes PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


def main():
    fig, ax = plt.subplots(figsize=(12.8, 7.3), facecolor='white')
    ax.set(xlim=(0, 16), ylim=(0, 9))
    ax.axis('off')
    def box(x, y, w, h, title, body, tint='#f2f6fa'):
        ax.add_patch(Rectangle((x-w/2, y-h/2), w, h, facecolor=tint,
                               edgecolor='#25364a', linewidth=1.4, zorder=3))
        split=y+h/2-.53
        ax.plot([x-w/2,x+w/2],[split,split],color='#25364a',lw=1,zorder=4)
        ax.text(x,y+h/2-.26,title,ha='center',va='center',fontsize=11,
                fontweight='bold',zorder=5)
        ax.text(x-w/2+.13,split-.15,body,ha='left',va='top',fontsize=10.5,
                linespacing=1.45,zorder=5)
    def edge(start, end, dashed=False):
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=19,
                     edgecolor='#25364a',facecolor='white',linewidth=1.3,
                     linestyle='--' if dashed else '-',zorder=1))
    box(7.6,7.35,4.2,1.6,'«interface» CableTV','+ cost: Double\n+ packages: String')
    box(2.6,4.5,3.6,1.9,'BasicPlan','+ cost = 30\n+ packages = "Basic plan"')
    box(9.4,4.5,4.0,1.9,'«abstract» Packages','- account: CableTV\n+ cost, packages: delegate')
    edge((2.6,5.45),(6.2,6.55),True)
    edge((8.5,5.45),(8.0,6.55),True)
    # A plain navigable association denotes a reference, not exclusive ownership.
    ax.plot([11.4,13.8,13.8,9.7],[4.75,4.75,7.35,7.35],color='#25364a',lw=1.3,zorder=1)
    ax.annotate('',xy=(9.7,7.35),xytext=(10.2,7.35),
                arrowprops=dict(arrowstyle='->',color='#25364a',lw=1.3))
    ax.text(13.95,6.2,'account\n1',fontsize=10.5,va='center')
    for x,title,cost,label in [(2.8,'Movies','10','Movies'),
                                (8.0,'HDChannels','7','HD channels'),
                                (13.2,'Sports','5','Sports')]:
        box(x,1.35,4.5,1.7,title,f'+ cost = super.cost + {cost}\n+ packages: append "{label}"',
            '#fff6df' if title=='Sports' else '#f2f6fa')
        edge((x,2.2),(9.4,3.55))
    ax.text(.45,8.65,'Cable TV: one component interface, nested package wrappers',
            fontsize=14,weight='bold')
    ax.text(.45,.05,'Hollow triangle: generalization   ·   Dashed triangle: interface realization',
            fontsize=10,color='#354354')
    fig.tight_layout(pad=.6)
    fig.savefig(Path.cwd()/'imperative-resit-decorator-uml.png',dpi=115,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
