"""Original payoff-set solution plots. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-38-bargaining.png in the caller's cwd, respecting MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,2,figsize=(8.6,4.2),dpi=100,facecolor='white')
for ax,poly,d,ans,title in zip(axes,[[[0,0],[4,0],[3,2],[2,3]],[[0,0],[3,0],[4,2],[2,3]]],[(2.4,0),(2.4,2)],[(3.2,1.6),(3.2,2.4)],['Original column payoff matrix','Transposed column payoff matrix']):
 p=np.array(poly);ax.fill(p[:,0],p[:,1],color='#e7f0f5',edgecolor='#305a72',linewidth=1.7)
 ax.plot(*d,'o',color='#ab512d',markersize=6,label='Security point')
 ax.plot(*ans,'*',color='#165663',markersize=13,label='Bargaining solution')
 ax.annotate(f'd = ({d[0]:g}, {d[1]:g})',d,xytext=(-65,10),textcoords='offset points',fontsize=9)
 ax.annotate(f'N = ({ans[0]:g}, {ans[1]:g})',ans,xytext=(-55,18),textcoords='offset points',fontsize=9)
 ax.axvline(d[0],color='#ab512d',linestyle=':',alpha=.7)
 ax.axhline(d[1],color='#ab512d',linestyle=':',alpha=.7)
 ax.set_xlim(-.2,4.3);ax.set_ylim(-.2,3.5);ax.set_xlabel('Row payoff');ax.set_ylabel('Column payoff');ax.set_title(title,fontsize=11)
 ax.grid(alpha=.18);ax.set_facecolor('white');ax.legend(loc='upper left',fontsize=8,framealpha=1)
fig.subplots_adjust(left=.07,right=.985,bottom=.15,top=.88,wspace=.3)
fig.savefig('paper-38-bargaining.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
