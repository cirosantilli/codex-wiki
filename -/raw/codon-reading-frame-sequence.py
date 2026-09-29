"""Draw an original codon example. Tested with Python 3.14 and matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SEQUENCE = 'AUGGCUUUCUGA'

def draw():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=110, facecolor='white')
    ax.set(xlim=(0, 14.8), ylim=(0, 9.1))
    ax.axis('off')
    ink = '#243349'
    colors = ['#dcedfa', '#dff2e8', '#fff0cb', '#f8dce0']
    ax.text(.3, 8.6, 'One RNA sequence, three possible forward reading frames', fontsize=17, color=ink, weight='bold')
    ax.text(.3, 8.0, 'Constructed example • standard genetic code • read 5′ → 3′', fontsize=12, color=ink)
    left, step = 3.25, .68
    def row(sequence, offset, y, label, insertion=False):
        ax.text(.3, y+.02, label, fontsize=12, color=ink, va='center')
        for start in range(offset, len(sequence)-2, 3):
            x = left + start*step
            ci = ((start-offset)//3)%4
            ax.add_patch(FancyBboxPatch((x-.26,y-.3), 2*step+.53,.6, boxstyle='round,pad=0.05', facecolor=colors[ci], edgecolor='#607086', linewidth=1))
        for i, letter in enumerate(sequence):
            complete = offset <= i < offset+3*((len(sequence)-offset)//3)
            ax.text(left+i*step,y,letter,ha='center',va='center',fontsize=16, family='monospace',color=('#9b1c34' if insertion and i==3 else ink if complete else '#85909b'),weight='bold' if insertion and i==3 else 'normal')
        ax.text(left-.65,y,'5′',ha='center',va='center',fontsize=12,color=ink)
        ax.text(left+len(sequence)*step+.02,y,'3′',ha='center',va='center',fontsize=12,color=ink)
    row(SEQUENCE,0,6.85,'Position 1')
    for j, aa in enumerate(['Met','Ala','Phe','STOP']):
        x=left+(1+3*j)*step
        ax.annotate('',xy=(x,5.87),xytext=(x,6.43),arrowprops={'arrowstyle':'->','color':'#607086'})
        ax.text(x,5.65,aa,ha='center',va='center',fontsize=13,color=ink,weight='bold')
    ax.text(left,5.10,'Peptide: N–Met–Ala–Phe–C',fontsize=13,color=ink)
    ax.text(left+6.9,5.10,'Stop adds no residue',fontsize=11,color='#9b1c34',ha='center')
    row(SEQUENCE,1,4.0,'Position 2')
    row(SEQUENCE,2,2.95,'Position 3')
    ax.text(left,2.32,'Regroupings only; neither row assumes cellular initiation.',fontsize=11,color=ink)
    row(SEQUENCE[:3]+'C'+SEQUENCE[3:],0,1.48,'+ C after AUG',insertion=True)
    ax.text(.3,.66,'Same start retained: AUG stays intact; downstream triplets change.',fontsize=12,color=ink)
    ax.text(.3,.18,'Grey letters are incomplete groups at the displayed end.',fontsize=11,color='#596573')
    fig.subplots_adjust(left=.015,right=.99,top=.99,bottom=.02)
    fig.savefig(Path(__file__).stem+'.png',facecolor='white',transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    draw()
