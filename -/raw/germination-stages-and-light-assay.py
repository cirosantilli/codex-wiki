"""Original stage and proposed assay diagram; Python 3.14, matplotlib 3.10.7.
Run from _media; writes germination-stages-and-light-assay.png to CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(11.2, 8), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 11.2), ylim=(0, 8))
ax.axis('off')
ax.text(5.6, 7.72, 'Water uptake, emergence and later growth are different endpoints', ha='center', fontsize=16, weight='bold')
xs = [1.5, 4.2, 6.9, 9.6]
labels = ['Imbibition', 'Activation / expansion', 'Radicle emerges', 'Seedling growth']
for i, x in enumerate(xs):
    ax.add_patch(FancyBboxPatch((x-1.15, 5.15), 2.3, 2.1, boxstyle='round,pad=0.06', facecolor='#fafafa', edgecolor='#ccc'))
    ax.text(x, 6.96, labels[i], ha='center', fontsize=11, weight='bold')
    ax.add_patch(Ellipse((x, 6.08), .82, .57, facecolor='#ebd59b', edgecolor='#78502d', linewidth=2))
    if i == 0:
        ax.annotate('water', (x-.3, 6.1), xytext=(x-.77, 6.6), fontsize=10, color='#247aaa', arrowprops={'arrowstyle':'->','color':'#247aaa'})
    if i == 1:
        ax.plot([x-.12,x+.12], [6.17,5.97], color='#267348', lw=5)
    if i >= 2:
        ax.plot([x+.25,x+.42,x+.4], [5.94,5.84,5.72], color='#267348', lw=4)
    if i == 3:
        ax.plot([x,x,x+.13], [6.2,6.54,6.68], color='#267348', lw=4)
        for dx, angle in [(-.2, -25),(.2,25)]:
            ax.add_patch(Ellipse((x+dx,6.6),.46,.17,angle=angle,facecolor='#267348'))
    ax.text(x, 5.3, ['Swelling alone\nis insufficient', 'Internal activity\nbefore protrusion', 'Common assay\ncompletion criterion', 'Establishment /\nsurvival measured later'][i], ha='center', fontsize=10)
for a,b in zip(xs[:-1],xs[1:]):
    ax.annotate('', (b-1.23,6.05), xytext=(a+1.23,6.05), arrowprops={'arrowstyle':'->','lw':1.6})
ax.plot([8.25,8.25],[5,7.25], color='#267348', linestyle='--', lw=1.5)
ax.text(5.6,4.65,'Proposed matched-condition light assay • no outcome data shown',ha='center',fontsize=15,weight='bold')
ax.text(.45,4.17,'One seed lot → random allocation to replicated dishes',fontsize=12)
ax.text(.45,3.83,'Match water, temperature, handling and total elapsed time',fontsize=12,color='#444')
row_y = [3.21,2.65,2.09,1.53]
for label,y,pulses in zip(['Dark control','Red','Red → far-red','Red → far-red → red'],row_y,[[],['R'],['R','FR'],['R','FR','R']]):
    ax.text(.45,y,label,va='center',fontsize=12)
    for j in range(3):
        x=4.1+j*.86
        pulse = pulses[j] if j<len(pulses) else 'wait'
        color = '#c65343' if pulse=='R' else '#834b6b' if pulse=='FR' else '#eeeeee'
        ax.add_patch(FancyBboxPatch((x-.32,y-.19),.64,.38,boxstyle='round,pad=.025',facecolor=color,edgecolor='none'))
        ax.text(x,y,pulse,ha='center',va='center',fontsize=10,color='white' if pulse!='wait' else '#555')
    ax.annotate('', (7.3,y), xytext=(6.34,y),arrowprops={'arrowstyle':'->','color':'#555'})
ax.add_patch(FancyBboxPatch((7.5,1.28),3.15,2.19,boxstyle='round,pad=.04',facecolor='#e9f2ec',edgecolor='#267348'))
ax.text(9.08,2.4,'Hold under matched\nconditions in darkness\n\nCount first radicle emergence\nat a specified deadline',ha='center',va='center',fontsize=11)
ax.text(5.6,.88,'R = red light   FR = far-red light   wait = sham interval',ha='center',fontsize=11)
ax.text(5.6,.42,'Keep observation light controlled; replicate dishes, not just seeds within one dish.',ha='center',fontsize=11,color='#555')
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),facecolor='white',transparent=False)
plt.close(fig)
