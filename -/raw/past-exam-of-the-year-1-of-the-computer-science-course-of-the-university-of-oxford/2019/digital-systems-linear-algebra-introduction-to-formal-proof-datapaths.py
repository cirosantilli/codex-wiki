"""Original solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
OUT='digital-systems-linear-algebra-introduction-to-formal-proof-datapaths.png'
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
plt.rcParams.update({'font.size':9,'font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,2,figsize=(8.6,3.8),dpi=100,facecolor='white')
def box(ax,x,y,w,h,t):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.04',fc='white',ec='#2166ac',lw=1.4,zorder=3));ax.text(x,y,t,ha='center',va='center',zorder=4)
def arrow(ax,pts,label=None,off=(0,0)):
 for a,b in zip(pts[:-1],pts[1:]):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->' if b==pts[-1] else '-',mutation_scale=10,color='#444444',lw=1.2))
 if label:ax.text((pts[0][0]+pts[-1][0])/2+off[0],(pts[0][1]+pts[-1][1])/2+off[1],label,ha='center',va='center',fontsize=8)
for ax in axes:ax.set_xlim(0,10);ax.set_ylim(0,9);ax.axis('off')
a=axes[0];a.set_title('Parallel: select ALU or shift result',fontsize=10,fontweight='bold',pad=15)
box(a,1.8,5.8,2.4,1.3,'Register file');box(a,5,7,1.5,1,'ALU');box(a,5,4.6,1.5,1,'Shifter');box(a,8.4,5.8,1.3,1.4,'Result\nmux')
arrow(a,[(3,6.15),(3.7,6.15),(3.7,7),(4.2,7)],'A, B',off=(-.4,.5));arrow(a,[(3,5.45),(3.7,5.45),(3.7,4.6),(4.2,4.6)],'B',off=(-.3,-.5));arrow(a,[(5.8,7),(7.5,7),(7.5,6.15),(7.7,6.15)]);arrow(a,[(5.8,4.6),(7.5,4.6),(7.5,5.45),(7.7,5.45)]);arrow(a,[(9.1,5.8),(9.8,5.8)])
box(a,6.8,1.7,2.2,.9,'Data memory');arrow(a,[(5.8,7),(6.6,7),(6.6,2.2)]);a.plot(6.6,7,'o',color='#444444',ms=3);a.text(7.0,3.1,'address',fontsize=8)
a.text(3.0,2.9,'Controls: ALU operation,\nshift amount, result select;\ncommon write controls.',ha='center',fontsize=8.2)
a.text(5,.45,'ALU and shifter can operate in parallel.',ha='center',fontsize=8.7)
a=axes[1];a.set_title('Serial: shift one ALU operand',fontsize=10,fontweight='bold',pad=15)
box(a,1.6,5.8,2.2,1.3,'Register file');box(a,4.8,4.7,1.6,1,'Shifter');box(a,8,6,1.4,1.2,'ALU')
arrow(a,[(2.8,6.15),(4,6.15),(4,7),(8,7),(8,6.65)],'A',off=(.2,.4));arrow(a,[(2.8,5.4),(3.3,5.4),(3.3,4.7),(3.95,4.7)],'B',off=(-.1,-.45));arrow(a,[(5.65,4.7),(6.7,4.7),(6.7,5.8),(7.25,5.8)],'shifted B',off=(.1,-.4));arrow(a,[(8.75,6),(9.8,6)])
box(a,8,1.7,2.2,.9,'Data memory');arrow(a,[(8.8,5.7),(9.3,5.7),(9.3,2),(9.15,2)],'address',off=(-.8,-.1))
a.text(4.2,3.1,'Controls: shift amount and ALU operation;\npass shifted B for a shift-only instruction.',ha='center',fontsize=8.2)
a.text(5,.45,'Shift and arithmetic share a serial path.',ha='center',fontsize=8.7)
fig.subplots_adjust(left=.015,right=.99,top=.84,bottom=.03,wspace=.08)
fig.savefig(Path.cwd()/OUT,dpi=100,facecolor='white',transparent=False,metadata={'Software':'codex-wiki Matplotlib'});plt.close(fig)
