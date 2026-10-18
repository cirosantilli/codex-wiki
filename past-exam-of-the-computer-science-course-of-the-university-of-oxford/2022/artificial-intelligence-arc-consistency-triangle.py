"""Local supports versus global incompatibility; no source figure is reproduced."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.7, 3.1), dpi=100,
                           gridspec_kw={'width_ratios': [1.15, 1]})
fig.patch.set_facecolor('white')
pos = {'X': (0, 1), 'Y': (-.85, -.55), 'Z': (.85, -.55)}
for a,b in [('X','Y'),('Y','Z'),('Z','X')]:
    x,y = pos[a],pos[b]
    ax.plot([x[0],y[0]],[x[1],y[1]], color='#778792', lw=2, zorder=0)
    mx,my=(x[0]+y[0])/2,(x[1]+y[1])/2
    ax.text(mx,my,'≠',ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':2})
for name,(x,y) in pos.items():
    ax.add_patch(Circle((x,y),.37,facecolor='#e6f1f5',edgecolor='#177ca4',lw=1.8))
    ax.text(x,y+.09,name,ha='center',va='center',weight='bold')
    ax.text(x,y-.13,'{0, 1}',ha='center',va='center',fontsize=10)
ax.set(xlim=(-1.38,1.38),ylim=(-1.05,1.65),aspect='equal')
ax.axis('off')
ax.set_title('Every arc has support', fontsize=11)
bx.axis('off')
bx.set_title('Neither initial choice extends', fontsize=11)
for y,start in [(.75,0),(.44,1)]:
    seq=[start,1-start,start]
    bx.text(.04,y,f'X = {seq[0]}  →  Y = {seq[1]}  →  Z = {seq[2]}',fontsize=11,
            transform=bx.transAxes, color='#283b46')
    bx.text(.04,y-.13,'but X = Z violates the last edge',fontsize=9.5,
            transform=bx.transAxes, color='#a13e28')
bx.text(.04,.08,'AC-3 keeps all six values.\nNo complete solution exists.',
        transform=bx.transAxes,fontsize=10.5,linespacing=1.7,
        bbox={'facecolor':'#fff3e8','edgecolor':'none','pad':8})
fig.tight_layout(pad=1.1,w_pad=1)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
