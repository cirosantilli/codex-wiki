"""Qualitative protease-protection controls, not measured or simulated gel lanes.

Tested with Python 3.14, matplotlib 3.10.7. Emit basename PNG in CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Polygon

INK='#18354b'; BLUE='#216b9a'; RED='#b84739'; GREEN='#157451'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11, 'text.color':INK})
fig=plt.figure(figsize=(11.5,8),dpi=110,facecolor='white')
fig.text(.04,.95,'Does a membrane barrier explain protection?',fontsize=19,weight='bold')
fig.text(.04,.91,'Qualitative control logic for completed soluble cargo • no gel lanes or measured amounts',fontsize=10.5)
a=fig.add_axes([.04,.57,.92,.29]); a.set(xlim=(0,12),ylim=(0,3)); a.axis('off')
for i,title in enumerate(['Cargo outside', 'Cargo enclosed', 'Barrier disrupted']):
    cx=2+4*i
    a.text(cx,2.8,title,ha='center',weight='bold',fontsize=12)
    if i<2:
        a.add_patch(Circle((cx,1.45),.74,facecolor='#eef6fa',edgecolor=BLUE,lw=2.8))
    else:
        for ang in (15,140,265):
            a.add_patch(Arc((cx,1.45),1.48,1.48,theta1=ang,theta2=ang+70,color=BLUE,lw=2.8))
    for dx,dy in [(-1.06,.32),(.98,.4)]:
        a.add_patch(Polygon([(cx+dx,1.45+dy),(cx+dx+.14,1.65+dy),(cx+dx+.28,1.45+dy)],color=RED))
    if i==0:
        a.plot([cx-.8,cx-.58,cx-.34],[.41,.55,.39],color=GREEN,lw=3)
        a.annotate('',(cx-.57,.58),(cx-.97,1.62),arrowprops={'arrowstyle':'->','color':RED,'lw':1.5})
        note='External protease can reach cargo'
    elif i==1:
        a.plot([cx-.36,cx-.12,cx+.12,cx+.36],[1.4,1.58,1.35,1.55],color=GREEN,lw=3)
        note='Intact barrier excludes protease'
    else:
        a.plot([cx-.35,cx-.15],[1.3,1.4],color=GREEN,lw=3)
        a.plot([cx+.1,cx+.3],[1.65,1.55],color=GREEN,lw=3)
        a.annotate('',(cx+.25,1.48),(cx+.98,1.86),arrowprops={'arrowstyle':'->','color':RED,'lw':1.5})
        note='Protease now reaches cargo'
    a.text(cx,.02,note,ha='center',fontsize=10)

rows=[
['No membranes; + protease','Cargo digested','Exposed-cargo / protease activity control'],
['Membranes; no additions','Cargo detectable','Starting product and recovery control'],
['Membranes; + protease','Cargo protected','Compatible with enclosure'],
['Membranes; + detergent only','Cargo detectable','Disruption must preserve detection'],
['Membranes; + detergent + protease','Cargo digested','Protection depends on intact barrier'],
]
tax=fig.add_axes([.04,.19,.92,.35]); tax.axis('off')
table=tax.table(cellText=rows,colLabels=['Treatment after import','Expected result*','What the comparison tests'],colWidths=[.32,.21,.47],cellLoc='left',colLoc='left',bbox=[0,0,1,1])
table.auto_set_font_size(False);table.set_fontsize(10)
for (r,c),cell in table.get_celld().items():
    cell.set_edgecolor('#d0dce4');cell.PAD=.08
    cell.set_facecolor('#e8f0f5' if r==0 else ('#f5f8fa' if r%2 else 'white'))
    cell.get_text().set_color(INK)
    if r==0:cell.get_text().set_weight('bold')
fig.text(.04,.14,'*Conditional expectations: intact vesicles, digestible cargo, active protease with and without detergent.',fontsize=10)
fig.text(.04,.103,'Use exposed-cargo controls in both chemical conditions. Detergent is added after import, not during synthesis.',fontsize=10)
fig.text(.04,.055,'A nascent chain can retain ribosome-shielded fragments. A transmembrane chain can protect only its luminal part.',fontsize=10)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',dpi=110)
plt.close(fig)
