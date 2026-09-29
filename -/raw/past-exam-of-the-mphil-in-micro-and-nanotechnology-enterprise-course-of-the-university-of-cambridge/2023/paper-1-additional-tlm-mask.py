"""Original positive-resist TLM lift-off layout, Python 3.14 and matplotlib.

Schematic dimensions only; save the PNG basename into the current directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig,axes=plt.subplots(2,1,figsize=(9,5.3),layout='constrained')
fig.patch.set_facecolor('white')
positions=[.8,2.6,5.0,8.1]
width=.75
for ax in axes:
    ax.set(xlim=(0,10),ylim=(0,3.1))
    ax.axis('off')
ax=axes[0]
ax.add_patch(Rectangle((.1,.35),9.8,2.25,fc='#3b434b',ec='#26313a'))
for x in positions:ax.add_patch(Rectangle((x,.8),width,1.35,fc='white',ec='#c1c9cf'))
ax.text(5,2.9,'Positive-resist mask: clear windows become metal pads',ha='center',fontsize=12)
ax.text(5,.48,'Chrome background blocks exposure',ha='center',color='white',fontsize=10)
ax=axes[1]
ax.add_patch(Rectangle((.1,.35),9.8,2.25,fc='#f2f5f7',ec='#8b9aa5'))
ax.add_patch(Rectangle((.6,.8),8.6,1.35,fc='#dceceb',ec='none'))
for x in positions:ax.add_patch(Rectangle((x,.8),width,1.35,fc='#666d76',ec='#39424c'))
for i,(x,y) in enumerate(zip(positions[:-1],positions[1:]),1):
    a=x+width;b=y
    ax.annotate('',xy=(b,.55),xytext=(a,.55),arrowprops={'arrowstyle':'<->','lw':1.1})
    ax.text((a+b)/2,.2,rf'$d_{i}$',ha='center',fontsize=11)
ax.annotate('',xy=(.4,2.15),xytext=(.4,.8),arrowprops={'arrowstyle':'<->','lw':1.1})
ax.text(.24,1.45,r'$W$',ha='right',va='center',fontsize=12)
ax.text(5,2.9,'After lift-off: equal-width contacts, variable edge spacing',ha='center',fontsize=12)
fig.savefig('paper-1-additional-tlm-mask.png',dpi=160,facecolor='white')
plt.close(fig)
