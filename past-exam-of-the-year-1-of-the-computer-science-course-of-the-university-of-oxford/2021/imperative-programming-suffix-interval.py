"""Original suffix-array illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the matching PNG to CWD, without copying examination artwork.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

text='banana'
suffixes=sorted(range(len(text)),key=lambda i:text[i:])
fig,ax=plt.subplots(figsize=(6.6,3.4),dpi=120,facecolor='white')
ax.set_facecolor('white');ax.set_xlim(0,10);ax.set_ylim(-.7,6.5);ax.axis('off')
ax.text(.4,6.15,'start',fontsize=11,weight='bold');ax.text(2.1,6.15,'suffix in dictionary order',fontsize=11,weight='bold')
for row,i in enumerate(suffixes):
 y=5.4-row
 if text[i:].startswith('ana'):ax.add_patch(Rectangle((.25,y-.3),7.4,.67,color='#e3f1e9',zorder=0))
 ax.text(.72,y,str(i),ha='center',va='center',fontsize=12)
 for j,c in enumerate(text[i:]):ax.text(2.15+.49*j,y,c,ha='center',va='center',fontfamily='monospace',fontsize=15,color='#176b47'if text[i:].startswith('ana')and j<3 else '#243441')
ax.annotate('shared prefix\nlength 3',xy=(5.1,3.9),xytext=(7.35,3.9),ha='left',va='center',fontsize=11,arrowprops={'arrowstyle':'->','color':'#176b47'},color='#176b47')
ax.text(5,-.55,'Two occurrences start at 1 and 3; overlap is allowed.',ha='center',fontsize=10)
fig.suptitle('A repeated prefix occupies a suffix-array interval',fontsize=12,y=.98)
fig.subplots_adjust(left=.02,right=.99,top=.87,bottom=.08)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
