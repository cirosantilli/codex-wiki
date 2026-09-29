"""Original shared-array double stack; Python 3.14 / Matplotlib 3.10.7.
The PNG is always written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig,ax=plt.subplots(figsize=(8,2.7),dpi=120,facecolor='white');ax.set_facecolor('white')
for i in range(12):
 color='#cce8da'if i<4 else '#d9e5f5'if i>=9 else 'white'
 ax.add_patch(Rectangle((i,0),1,1,facecolor=color,edgecolor='#405569',lw=1.1))
 ax.text(i+.5,-.23,str(i),ha='center',fontsize=9)
 if i<4:ax.text(i+.5,.48,str([8,3,6,2][i]),ha='center',fontsize=12)
 elif i>=9:ax.text(i+.5,.48,str([7,4,9][i-9]),ha='center',fontsize=12)
ax.text(2,1.38,'stack a',ha='center',fontsize=11,color='#176b47');ax.text(10.5,1.38,'stack b',ha='center',fontsize=11,color='#274c8b')
ax.text(6.5,.45,'free space',ha='center',fontsize=11,color='#66727e')
ax.annotate('top',xy=(3.5,.12),xytext=(3.5,-1),ha='center',fontsize=10,arrowprops={'arrowstyle':'->','color':'#176b47'})
ax.annotate('top',xy=(9.5,.12),xytext=(9.5,-1),ha='center',fontsize=10,arrowprops={'arrowstyle':'->','color':'#274c8b'})
ax.annotate('',xy=(5.4,1.15),xytext=(2.7,1.15),arrowprops={'arrowstyle':'->','color':'#176b47','lw':2})
ax.annotate('',xy=(7.7,1.15),xytext=(10.5,1.15),arrowprops={'arrowstyle':'->','color':'#274c8b','lw':2})
ax.text(4,-.62,'left = 4',ha='center',fontsize=10);ax.text(9,-.62,'right = 9',ha='center',fontsize=10)
ax.text(6,-1.45,'Occupied = left + (MAX − right); full exactly when left = right.',ha='center',fontsize=10)
ax.set_xlim(-.4,12.4);ax.set_ylim(-1.7,1.7);ax.axis('off');fig.subplots_adjust(left=.02,right=.98,bottom=.07,top=.9)
fig.suptitle('One fixed array; both stacks share every free position',fontsize=12,y=.98)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
