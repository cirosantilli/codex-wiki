"""Original Young-tableau illustrations; Python 3.14 and Matplotlib 3.10.
Run in the desired output directory to write the PNG there.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
examples=[([1,2,4,3,5],[[1,2,3,5],[4]],[[1,2,3,5],[4]]),([2,4,3,1],[[1,3],[2],[4]],[[1,2],[3],[4]])]
fig,axes=plt.subplots(2,2,figsize=(9,6),facecolor='white')
for r,(word,P,Q) in enumerate(examples):
 for c,tableau in enumerate([P,Q]):
  ax=axes[r,c];ax.set_facecolor('white')
  for i,row in enumerate(tableau):
   for j,v in enumerate(row):
    ax.add_patch(Rectangle((j,-i-1),1,1,facecolor='#e9f3fa' if i==0 else 'white',edgecolor='#263946',lw=1.4))
    ax.text(j+.5,-i-.5,str(v),ha='center',va='center',fontsize=16)
  ax.set(xlim=(-.15,4.4),ylim=(-3.25,.4),aspect='equal');ax.axis('off')
  ax.set_title(('Insertion $P$' if c==0 else 'Recording $Q$')+'; input '+','.join(map(str,word)),fontsize=11)
fig.suptitle('Two explicit RSK calculations',fontsize=16)
fig.tight_layout(rect=(0,0,1,.94))
fig.savefig(Path.cwd()/'2011-rsk-examples.png',dpi=170,facecolor='white')
