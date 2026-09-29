"""Original pH-11 ZnO growth-inhibition schematic; Python 3.14/matplotlib.

Based on the sign-specific chemical observation in Joo et al. (2011), not a
copy of its figures. Effective solution surface charge is not crystal polarity.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle

fig,axes=plt.subplots(1,3,figsize=(12.8,4.7),layout='constrained')
fig.patch.set_facecolor('white')
for ax in axes:
    ax.set(xlim=(0,6),ylim=(0,6),aspect='equal');ax.axis('off')
ax=axes[1];ax.set_title('Positive complexes block the negative top',fontsize=11)
ax.add_patch(Rectangle((1,1.4),4,1,facecolor='#c4dce2',edgecolor='.25'))
ax.text(3,1.9,'ZnO platelet',ha='center',va='center',fontsize=12)
for x in [1.3,2.1,2.9,3.7,4.5]:
    ax.text(x,2.42,'−',ha='center',fontsize=13,color='#2d718b')
    ax.add_patch(Circle((x,2.98),.17,facecolor='#e4b8a1'))
    ax.text(x,2.98,'+',ha='center',va='center',fontsize=11)
ax.text(3,3.5,'Cd-containing positive complexes',ha='center',fontsize=9)
ax.annotate('',(3,4.2),(3,3.75),arrowprops={'arrowstyle':'-|>','color':'.4'})
ax.text(3,4.5,'Axial growth inhibited\nlow height / diameter',ha='center',fontsize=11)
ax=axes[2];ax.set_title('Negative complexes block positive sidewalls',fontsize=11)
ax.add_patch(Rectangle((2.3,1),1.4,3.9,facecolor='#c4dce2',edgecolor='.25'))
ax.text(3,2.9,'ZnO wire',ha='center',va='center',rotation=90,fontsize=12)
for y in [1.4,2.2,3,3.8,4.6]:
    for x,outer in [(2.25,1.72),(3.75,4.28)]:
        ax.text(x,y,'+',ha='center',va='center',fontsize=12,color='#b6623e')
        ax.add_patch(Circle((outer,y),.17,facecolor='#bdd1e5'))
        ax.text(outer,y,'−',ha='center',va='center',fontsize=12)
ax.text(3,.35,'Al-containing negative complexes\nhigh height / diameter',ha='center',fontsize=10)
ax.annotate('',(3,5.7),(3,5),arrowprops={'arrowstyle':'->','color':'#2d718b','lw':2})
ax=axes[0];ax.set_title('Crystallographic faces',fontsize=11)
ax.add_patch(Rectangle((2,1.3),2,3.3,facecolor='#c4dce2',edgecolor='.25'))
ax.plot([2,4],[4.6,4.6],color='#b6623e',lw=3)
ax.plot([2,4],[1.3,1.3],color='#2d718b',lw=3)
ax.text(3,4.95,r'Zn-terminated $(0001)$',ha='center',fontsize=9)
ax.text(3,.8,r'O-terminated $(000\bar1)$',ha='center',fontsize=9)
ax.text(3,3.1,r'Prismatic side faces',ha='center',fontsize=9)
ax.text(3,2.7,r'$\{10\bar10\}$: nonpolar',ha='center',fontsize=9)
ax.annotate('',(4.55,4.5),(4.55,1.5),arrowprops={'arrowstyle':'->','color':'.3'})
ax.text(4.85,3,'+c',ha='center',fontsize=10)
ax.text(3,.25,'Termination is not net solution charge.',ha='center',fontsize=8)
fig.suptitle('Crystal polarity and condition-specific surface charge at pH 11',fontsize=13)
fig.savefig('paper-2-zno-facets.png',dpi=150,facecolor='white')
plt.close(fig)
