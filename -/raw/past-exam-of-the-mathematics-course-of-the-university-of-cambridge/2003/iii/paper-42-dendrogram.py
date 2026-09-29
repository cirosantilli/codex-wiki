"""Reconstruct the derived complete-linkage tree; emit one PNG to caller CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Only declared root dependencies; caller controls MPLCONFIGDIR and backend.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

names=['Philip','Chad','Graham','Tim','Mark','Juliet','Garfield','Nicolas','Frederic','John','Sauli','Fred','Gbenga']
merges=[(-12,-13),(-3,-4),(-2,-8),(-9,3),(-10,4),(-1,-5),(-7,1),(2,6),(5,7),(-11,8),(-6,10),(9,11)]
heights=[0,1/8,1/6,1/3,1/3,3/8,2/5,4/9,1/2,5/8,3/4,7/8]
children={i+1:p for i,p in enumerate(merges)}
def leaves(node):
    if node<0:
        return [node]
    a,b=children[node]
    return leaves(a)+leaves(b)
order=leaves(12)
x={node:position for position,node in enumerate(order)}
y={node:0.0 for node in order}
fig,ax=plt.subplots(figsize=(9.0,4.6),dpi=120,facecolor='white')
ax.set_facecolor('white')
for index,((a,b),height) in enumerate(zip(merges,heights),1):
    ax.plot([x[a],x[a],x[b],x[b]],[y[a],height,height,y[b]],color='#244d73',lw=1.8)
    x[index]=(x[a]+x[b])/2
    y[index]=height
ax.set_xticks(range(13),[names[-node-1] for node in order],rotation=55,ha='right')
ax.set_ylim(-.02,.94)
ax.set_ylabel('Complete-linkage Jaccard distance')
ax.set_title('Binary profiles: reconstructed clustering tree')
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y',color='#dddddd',lw=.6)
fig.tight_layout()
fig.savefig('paper-42-dendrogram.png',facecolor='white',transparent=False)
plt.close(fig)
