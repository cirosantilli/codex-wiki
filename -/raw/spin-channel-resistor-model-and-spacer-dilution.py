"""Original stipulated CPP resistor model, not a fit to the CIP experiments."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig = plt.figure(figsize=(12, 5.2), dpi=140, facecolor='white')
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1], wspace=.28)
ax=fig.add_subplot(gs[0]);ax.set(xlim=(-.5,9),ylim=(-.65,6));ax.axis('off')
for y, parallel in [(4.3,True),(1.6,False)]:
    ax.text(4.3,y+.85,'Parallel' if parallel else 'Antiparallel',ha='center',fontsize=13,weight='bold')
    for dy, vals in [(.35,[1,1,1] if parallel else [1,1,4]),(-.35,[4,1,4] if parallel else [4,1,1])]:
        yy=y+dy;ax.plot([.6,7.8],[yy,yy],color='#555',zorder=0)
        for x,v,label in zip([2,4.2,6.4],vals,['Layer 1','Spacer','Layer 2']):
            ax.add_patch(Rectangle((x-.6,yy-.22),1.2,.44,facecolor='#e6edf2' if label!='Spacer' else '#eee',edgecolor='#555'))
            ax.text(x,yy,f'{v} Ω',ha='center',va='center',fontsize=10)
    for x in [.6,7.8]:ax.plot([x,x],[y-.35,y+.35],color='#555')
    ax.text(4.2,y-.85,r'$R_P=2.25\ \Omega$' if parallel else r'$R_{AP}=3\ \Omega$',ha='center',fontsize=13)
ax.text(4.2,5.9,'Two independent spin channels',ha='center',fontsize=12)
ax.text(4.2,-.5,r'Each row: series resistors; rows: parallel at the terminals',ha='center',fontsize=10)
ax2=fig.add_subplot(gs[1]);p=np.linspace(0,.85,401)
for s,c in [(0,'#3569a2'),(.2,'#d17a29'),(.8,'#3b8e64')]:
    m=p*p/((1+s)**2-p*p);ax2.plot(p,m,label=f's = {s:g}',color=c,lw=2.2)
ax2.scatter([.6],[1/3],color='#222',zorder=5)
ax2.annotate('Chosen network\np = 0.6, s = 0.2\nm = 1/3',(.6,1/3),(.12,1.6),arrowprops=dict(arrowstyle='->',color='#444'),fontsize=11)
ax2.set(xlabel=r'Spin-channel contrast $p=(b-a)/(a+b)$',ylabel=r'$m=(R_{AP}-R_P)/R_P$',xlim=(0,.85),ylim=(0,2.8),title='A common spacer dilutes the ratio')
ax2.legend(title=r'$s=r/(a+b)$',loc='upper left',frameon=False);ax2.grid(alpha=.18)
fig.suptitle('A current-perpendicular-to-plane (CPP) resistor toy model',fontsize=16,y=.98)
fig.text(.5,.025,'a = 1 Ω, b = 4 Ω, r = 1 Ω per channel. No spin flips; equal terminal voltage. Not measured CIP data.',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.97,top=.84,bottom=.17)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
