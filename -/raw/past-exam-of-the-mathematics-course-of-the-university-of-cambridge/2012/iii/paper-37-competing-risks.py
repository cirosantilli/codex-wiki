"""Generate the original transition diagram in the caller's cwd.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (system +dfsg1).
The caller supplies MPLCONFIGDIR; this script leaves it unchanged.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
fig,ax=plt.subplots(figsize=(10.5,4.6001),dpi=100,facecolor='white')
ax.set(xlim=(0,10.5),ylim=(0,4.6));ax.axis('off')
def box(x,y,w,h,label,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10',facecolor=color,edgecolor='#243546',linewidth=1.5))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=13,color='#172636')
box(.35,1.65,2.05,1.05,'0: Alive after\nsurgery','#e8f1f8')
box(7.20,3.05,2.70,1.05,'1: Lung-cancer death\n(absorbing)','#fcebe5')
box(7.20,.50,2.70,1.05,'2: Other death\n(absorbing)','#eaf3e8')
for end in [(7.05,3.55),(7.05,1.05)]:
 ax.add_patch(FancyArrowPatch((2.55,2.18),end,arrowstyle='-|>',mutation_scale=19,linewidth=1.8,color='#243546'))
ax.text(4.6,3.63,r'$\widehat q_{01}(t\mid z)=\widehat\lambda_{10}(t)e^{1.3113z}$',ha='center',va='center',fontsize=14)
ax.text(4.55,.77,r'$\widehat q_{02}(t\mid z)=\widehat\lambda_{20}(t)e^{0.5903z}$',ha='center',va='center',fontsize=14)
ax.text(5.25,4.46,'Treatment-specific cause-specific transition intensities',ha='center',va='center',fontsize=16,weight='bold')
ax.text(5.25,.12,'z = 0: radiotherapy     z = 1: chemotherapy     t: years since surgery',ha='center',va='center',fontsize=12)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig('paper-37-competing-risks.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
