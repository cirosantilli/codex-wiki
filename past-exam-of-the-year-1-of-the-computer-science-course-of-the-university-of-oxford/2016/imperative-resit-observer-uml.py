"""Service observer UML. Python 3.14; matplotlib 3.10.7; writes PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


def main():
    fig,ax=plt.subplots(figsize=(13.5,7.4),facecolor='white')
    ax.set(xlim=(0,18.3),ylim=(0,9.6))
    ax.axis('off')
    def box(x,y,w,h,title,body,tint='#f2f6fa'):
        ax.add_patch(Rectangle((x-w/2,y-h/2),w,h,facecolor=tint,
                     edgecolor='#25364a',lw=1.4,zorder=3))
        split=y+h/2-.55
        ax.plot([x-w/2,x+w/2],[split,split],color='#25364a',lw=1,zorder=4)
        ax.text(x,y+h/2-.27,title,ha='center',va='center',fontsize=11,
                weight='bold',zorder=5)
        ax.text(x-w/2+.12,split-.16,body,ha='left',va='top',fontsize=10.5,
                linespacing=1.5,zorder=5)
    def edge(start,end,dashed=False):
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=20,
                     edgecolor='#25364a',facecolor='white',linewidth=1.3,
                     linestyle='--' if dashed else '-',zorder=1))
    box(3.0,7.15,5.1,3.1,'«trait» Service',
        '- _value: Double\n- companies: List[Company]\n+ value / value_=\n+ addCompany(c), sendMessage()\n+ updateValue(newValue)')
    box(11.5,7.55,4.0,1.6,'«interface» Company','+ meth(): Unit')
    ax.annotate('',xy=(9.5,7.55),xytext=(5.55,7.55),
                arrowprops=dict(arrowstyle='->',color='#25364a',lw=1.3))
    ax.text(7.5,7.8,'companies  0..*',ha='center',fontsize=10.5)
    ax.text(7.5,7.1,'notify: meth()',ha='center',fontsize=10.5)
    box(3.0,2.65,5.1,2.0,'SomeService',
        '+ updateValue(newValue):\n  set value, then notify')
    edge((3,3.65),(3,5.60))
    for x,name,factor in [(8.0,'PrivateCompany','1.1'),
                           (12.0,'PublicCompany','0.9'),
                           (16.0,'NonProfit','1.0')]:
        box(x,2.65,3.7,2.3,name,
            '- service: SomeService\n- v: Double\n+ meth(): refresh v',
            '#fff6df' if name=='NonProfit' else '#f2f6fa')
        edge((x,3.8),(11.5,6.75),True)
        ax.text(x,1.0,'callback factor '+factor,ha='center',fontsize=10)
    ax.text(.5,9.1,'Service values: subject registers and notifies company observers',
            fontsize=14,weight='bold')
    ax.text(.5,.35,'Each concrete company retains one SomeService and registers itself with it.',
            fontsize=10.5,color='#354354')
    fig.tight_layout(pad=.6)
    fig.savefig(Path.cwd()/'imperative-resit-observer-uml.png',dpi=115,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
