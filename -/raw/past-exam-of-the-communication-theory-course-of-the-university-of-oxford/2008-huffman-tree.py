"""Python 3.14.4; Matplotlib 3.10.7. Write PNG into the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(9,4.9),layout='constrained',facecolor='white');ax.set_facecolor('white');ax.axis('off')
positions={'':(0,0),'0':(-2.2,-1),'1':(2.2,-1),'00':(-3.3,-2),'01':(-1.1,-2),'10':(1.1,-2),'11':(3.3,-2),'110':(2.6,-3),'111':(4,-3)}
labels={'':'1','0':'7/16','1':'9/16','00':r'$x_3:\ 3/16$','01':r'$x_4:\ 1/4$','10':r'$x_5:\ 5/16$','11':'1/4','110':r'$x_1:\ 1/8$','111':r'$x_2:\ 1/8$'}
for code,(x,y) in positions.items():
 if code:
  px,py=positions[code[:-1]];ax.plot([px,x],[py,y],color='#52677c',lw=1.8,zorder=1);ax.text((px+x)/2,(py+y)/2+.08,code[-1],ha='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
 ax.text(x,y,labels[code],ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.35','facecolor':'#e5eff9'if code in ['','0','1','11']else '#ecf5e7','edgecolor':'#52677c'},zorder=3)
ax.set(xlim=(-4.1,4.7),ylim=(-3.55,.55),title='Huffman merges: 2+2=4, 3+4=7, 4+5=9, 7+9=16')
fig.savefig(Path.cwd()/'2008-huffman-tree.png',dpi=170,facecolor='white')
