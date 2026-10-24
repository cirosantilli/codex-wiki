"""Sampled smoother architecture. Writes its opaque PNG into the current directory.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig,ax=plt.subplots(figsize=(10,5.6),dpi=120)
fig.patch.set_facecolor('white')
ax.set_facecolor('white');ax.set_xlim(0,12);ax.set_ylim(0,7);ax.axis('off')
blue='#1e5074';dark='#21303b'
def box(x,y,w,h,label,color='#eaf3f8'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08,rounding_size=0.08',edgecolor=blue,facecolor=color,linewidth=1.5))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=12,color=dark)
def arrow(x,y,u,v):
 ax.annotate('',xy=(u,v),xytext=(x,y),arrowprops=dict(arrowstyle='->',color=dark,lw=1.6))
ax.text(6,6.65,'Three sampled smoother designs',ha='center',fontsize=18,weight='bold',color=dark)
ax.text(6,6.18,'Signals shown immediately before the active clock edge',ha='center',fontsize=11,color=dark)
ax.text(.5,5.1,r'$a=a_n$',fontsize=13,ha='center',color=dark)
arrow(.95,5.2,2,5.2);box(2,4.75,1.8,.9,'D flip-flop')
arrow(3.9,5.2,5.2,5.2);box(5.2,4.75,1.8,.9,'D flip-flop')
arrow(7.1,5.2,8.15,5.2)
ax.text(4.5,5.55,r'$b=a_{n-1}$',ha='center',fontsize=13,color=dark)
ax.text(8.75,5.2,r'$c=a_{n-2}$',ha='center',fontsize=13,color=dark)
box(3.25,2.85,3.35,1.05,'Combinational function\n'+r'$f(a,b,c,q)$')
for y,label in [(3.12,'a'),(3.42,'b'),(3.72,'c')]:
 ax.text(2.55,y,'$'+label+'$',ha='center',va='center',fontsize=12,color=dark)
 arrow(2.75,y,3.17,y)
arrow(6.7,3.38,7.7,3.38);box(7.8,2.9,1.8,.95,'Output DFF')
arrow(9.7,3.38,11.25,3.38)
ax.text(10.6,3.75,r'$z_n=q^+$',ha='center',fontsize=13,color=dark)
ax.plot([10.2,10.2,4.9,4.9],[3.38,2.15,2.15,2.72],color=dark,lw=1.5)
ax.annotate('',xy=(4.9,2.78),xytext=(4.9,2.5),arrowprops=dict(arrowstyle='->',color=dark,lw=1.5))
ax.text(7.4,2.35,r'old output $q=z_{n-1}$',ha='center',fontsize=11,color=dark)
ax.text(6,1.48,r'(c) $f=ab+ac+bc$     (d) $f=abc+aq+bq+cq$     (e) $f=ab+cq$',ha='center',fontsize=13,color=dark)
ax.text(6,.82,'All flip-flops share one clock. At the edge: history captures a and b; output captures f.',ha='center',fontsize=10,color=dark)
ax.text(6,.34,'The old-output feedback is unused in (c). Initialize the stored output to zero in (d).',ha='center',fontsize=10,color=dark)
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
fig.savefig('digital-systems-2013-smoother.png',facecolor='white',transparent=False,metadata={'Software':'digital-systems-2013-smoother.py'})
plt.close(fig)
