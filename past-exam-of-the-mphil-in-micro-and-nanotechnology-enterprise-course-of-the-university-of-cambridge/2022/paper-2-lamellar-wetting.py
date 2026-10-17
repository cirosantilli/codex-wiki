"""Original idealized copolymer film diagrams; Python 3.14/matplotlib.

Equal A/B bulk widths. One neutral boundary does not force perpendicular order.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

A,B='#e5b296','#9ecbd9'
fig,axes=plt.subplots(2,2,figsize=(9.4,6.8),layout='constrained')
fig.patch.set_facecolor('white')
def layers(ax,x,width,count,first='A'):
    spans=[.25]+[.5]*(count-2)+[.25]
    y=0
    for i,h in enumerate(spans):
        label=first if i%2==0 else ('B' if first=='A' else 'A')
        ax.add_patch(Rectangle((x,y),width,h,facecolor=A if label=='A' else B,edgecolor='white'))
        ax.text(x+width/2,y+h/2,label,ha='center',va='center',fontsize=10)
        y+=h
    return y
for ax in axes.flat:
    ax.set(xlim=(0,6),ylim=(-.35,3.55),xticks=[],yticks=[0,1,2,3],ylabel=r'Height / $L_0$')
    ax.axhline(0,color='.25',lw=2)
    ax.spines[['top','right','bottom']].set_visible(False)
ax=axes[0,0];layers(ax,0,6,5)
ax.axhline(2,color='.3');ax.set_title('Symmetric A / A; thickness 2L0')
ax.text(3,2.2,'A-selective atmosphere',ha='center',fontsize=9)
ax.text(3,-.28,'A-selective substrate',ha='center',fontsize=9)
ax=axes[0,1];layers(ax,0,6,6,'B')
ax.axhline(2.5,color='.3');ax.set_title('Asymmetric B / A; thickness 2.5L0')
ax.text(3,2.7,'A-selective atmosphere',ha='center',fontsize=9)
ax.text(3,-.28,'B-selective substrate',ha='center',fontsize=9)
ax=axes[1,0];layers(ax,0,3.9,5);layers(ax,3.9,2.1,7)
ax.plot([0,3.9,3.9,6],[2,2,3,3],color='.3')
ax.set_title('One terrace example: mean thickness 2.35L0')
ax.text(1.9,2.15,'2L0',ha='center',fontsize=9)
ax.text(4.95,3.13,'3L0',ha='center',fontsize=9)
ax.text(3,-.28,'Both local stacks terminate in A',ha='center',fontsize=9)
ax=axes[1,1]
ax.add_patch(Rectangle((0,0),6,.25,facecolor=A,edgecolor='white'))
ax.text(3,.125,'A wetting layer',ha='center',va='center',fontsize=9)
# Preserve total equal A/B amounts: bottom A=0.25, upper A=0.75, B=1.0.
xx=0
for i in range(8):
    label='A' if i%2==0 else 'B'
    width=(6/4)*(.75/1.75 if label=='A' else 1/1.75)
    ax.add_patch(Rectangle((xx,.25),width,1.75,facecolor=A if label=='A' else B,edgecolor='white'))
    ax.text(xx+width/2,1.2,label,ha='center',va='center',fontsize=9)
    xx+=width
ax.axhline(2,color='.3',ls='--');ax.set_title('One possible mixed morphology; not compulsory')
ax.text(3,2.25,'Neutral top; equal total A and B retained',ha='center',fontsize=9)
ax.text(3,-.28,'A-selective substrate remains',ha='center',fontsize=9)
fig.savefig('paper-2-lamellar-wetting.png',dpi=150,facecolor='white')
plt.close(fig)
