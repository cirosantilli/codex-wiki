"""Original solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
OUT='digital-systems-linear-algebra-introduction-to-formal-proof-barrel-shifter.png'
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,ax=plt.subplots(figsize=(8.4,3.2),dpi=100,facecolor='white');ax.set_xlim(0,12);ax.set_ylim(0,5);ax.axis('off')
ax.text(.2,4.6,'A 32-bit logical left shifter uses five optional shifts',fontweight='bold',fontsize=12)
xs=[2,4,6,8,10]
for j,x in enumerate(xs):
 ax.add_patch(FancyBboxPatch((x-.65,2.45),1.3,1.05,boxstyle='round,pad=.05',ec='#2166ac',fc='white',lw=1.4))
 ax.text(x,2.98,f'0 or {1<<j}\nbits',ha='center',va='center')
 ax.annotate('',(x,3.52),(x,4.05),arrowprops={'arrowstyle':'->','color':'#a85a12'});ax.text(x,4.15,f's{j}',ha='center',color='#a85a12')
 ax.annotate('',(x-.7,2.98),(x-1.25,2.98),arrowprops={'arrowstyle':'->','lw':1.3})
 ax.text(x,2.0,'32 one-bit muxes',ha='center',fontsize=8)
ax.text(.15,2.98,'input',va='center');ax.annotate('',(11.55,2.98),(10.7,2.98),arrowprops={'arrowstyle':'->','lw':1.3});ax.text(11.6,2.98,'output',va='center',ha='left')
ax.text(6,1.25,r'$s=s_0+2s_1+4s_2+8s_3+16s_4$',ha='center',fontsize=13)
ax.text(6,.65,'At stage j, each mux selects its own bit or the bit 2ʲ positions lower; missing bits are zero.',ha='center',fontsize=9)
ax.text(6,.16,r'One mux: $y=(\neg s\wedge u)\vee(s\wedge v)$',ha='center',fontsize=11)
fig.subplots_adjust(left=.01,right=.965,top=.99,bottom=.02)
fig.savefig(Path.cwd()/OUT,dpi=100,facecolor='white',transparent=False,metadata={'Software':'codex-wiki Matplotlib'});plt.close(fig)
