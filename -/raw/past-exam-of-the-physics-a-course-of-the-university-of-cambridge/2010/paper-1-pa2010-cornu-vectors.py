"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
positive=np.linspace(0,7,80001);phase=np.pi*positive**2/2;ds=positive[1]-positive[0]
C=np.r_[0,np.cumsum((np.cos(phase[:-1])+np.cos(phase[1:]))*ds/2)]
S=np.r_[0,np.cumsum((np.sin(phase[:-1])+np.sin(phase[1:]))*ds/2)]
def F(w):
 return np.sign(w)*np.array([np.interp(abs(w),positive,C),np.interp(abs(w),positive,S)])
w=np.linspace(-5,5,12001);curve=np.array([F(v) for v in w]);wg=.5/np.sqrt(.01*16/2)
fig,ax=plt.subplots(figsize=(7.2,7),layout='constrained');ax.plot(curve[:,0],curve[:,1],color='#b0b0b0',lw=1)
vectors=[(np.array([-.5,-.5]),np.array([.5,.5]),'#555555','No fence'),(F(0),F(wg),'#296ea1','Existing grazing gap'),(F(-1.209378),F(1.209378),'#b34d29','Freely selected optimum'),(F(-1.215779),F(2.340538),'#28815d','Optimum retaining existing gap')]
for start,end,color,label in vectors:
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'lw':2});ax.plot([],[],color=color,label=label)
ax.scatter([0],[0],color='black',s=14)
ax.set(xlabel='C(w)',ylabel='S(w)',title='Received fields as computed Fresnel chords',xlim=(-.88,.88),ylim=(-.88,.88),aspect='equal');ax.legend(fontsize=9,loc='upper left');ax.grid(alpha=.2)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
