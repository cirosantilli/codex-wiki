"""Draw the comparator chart and next-state maps; writes PNG in cwd.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(9, 7), facecolor='white')
gs = fig.add_gridspec(2, 2, height_ratios=[1.45, 1], hspace=.35, wspace=.3)
ax = fig.add_subplot(gs[0, :]); ax.set(xlim=(-3,3), ylim=(-.8,2.7)); ax.set_aspect('equal'); ax.axis('off')
pos = {'Lt':(-1.8,0), 'Eq':(0,1.55), 'Gt':(1.8,0)}
for s,p in pos.items():
    ax.add_patch(Circle(p,.36,facecolor='#e6f1fa',edgecolor='#264f70',lw=1.6))
    ax.text(*p,s+'\n'+{'Lt':'10','Eq':'00','Gt':'01'}[s],ha='center',va='center')
for s,t,lab,rad,loc in [
    ('Eq','Lt','01',.12,(-1.1,1.05)),
    ('Eq','Gt','10',-.12,(1.1,1.05)),
    ('Lt','Gt','10',.18,(0,-.53)),('Gt','Lt','01',.18,(0,.38))]:
    ax.add_patch(FancyArrowPatch(pos[s],pos[t],shrinkA=28,shrinkB=28,arrowstyle='-|>',mutation_scale=14,connectionstyle=f'arc3,rad={rad}',color='#264f70',lw=1.3))
    ax.text(*loc,lab,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
for s,(x,y) in pos.items():
    side=-1 if s=='Lt' else 1
    if s=='Eq':
        p1=(x-.2,y+.28); p2=(x+.2,y+.28); label=(x,y+.8)
    else:
        p1=(x+side*.24,y+.24); p2=(x+side*.24,y-.24);label=(x+side*.78,y-.48)
    ax.add_patch(FancyArrowPatch(p1,p2,connectionstyle='arc3,rad=-2.1' if s=='Eq' else f'arc3,rad={-2.1*side}',arrowstyle='-|>',mutation_scale=12,color='#264f70'))
    ax.text(*label,{'Lt':'00,01,11','Eq':'00,11','Gt':'00,10,11'}[s],ha='center',va='center')
ax.annotate('start',xy=(-.33,1.55),xytext=(-1,2.15),arrowprops={'arrowstyle':'->'},ha='center')
ax.set_title('LSB-first comparator: input labels are ab',pad=12,weight='bold')
for i,(name,rows) in enumerate([('L⁺',['0100','0100','----','1110']),('G⁺',['0001','1011','----','0001'])]):
    a=fig.add_subplot(gs[1,i]);a.axis('off')
    tab=a.table(cellText=[list(r.replace('-','–')) for r in rows],rowLabels=['00','01','11','10'],colLabels=['00','01','11','10'],cellLoc='center',loc='center',bbox=[.15,.05,.8,.82])
    tab.auto_set_font_size(False);tab.set_fontsize(12)
    for (r,c),cell in tab.get_celld().items():
        if r==0 or c==-1:cell.set_facecolor('#edf0f4')
        elif rows[r-1][c]=='1':cell.set_facecolor('#cce9df')
        elif rows[r-1][c]=='-':cell.set_facecolor('#eeeeee')
    a.set_title(f'{name} Karnaugh map',weight='bold');a.text(.55,.93,'ab →',transform=a.transAxes,ha='center');a.text(-.10,.48,'LG ↓',transform=a.transAxes,va='center',ha='center',rotation=90)
fig.text(.5,.015,'Gray order on both axes; “–” is an unused-state don’t-care.',ha='center',fontsize=10)
fig.savefig(Path.cwd()/'computing-prelims-2003-comparator.png',dpi=120,facecolor='white',metadata={'Software':'computing-prelims-2003-comparator.py'})
plt.close(fig)
