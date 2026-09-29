"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(2,2,figsize=(9,7),layout='constrained')
ax=axs[0,0];edges=[0,.45,1.3,1.8,2.9,3.5,4.2]
for j in range(len(edges)-1):
 for sign in [-1,1]:
  lo,hi=sorted([sign*edges[j],sign*edges[j+1]]);ax.axvspan(lo,hi,color=['#b45e57','#93b7d1'][j%2],alpha=.9)
ax.axvline(0,color='k');ax.annotate('',xy=(-3.6,.5),xytext=(-.3,.5),arrowprops={'arrowstyle':'->','lw':2});ax.annotate('',xy=(3.6,.5),xytext=(.3,.5),arrowprops={'arrowstyle':'->','lw':2})
ax.set(xlim=(-4.2,4.2),ylim=(0,1),yticks=[],xlabel='distance from ridge (arbitrary scale)',title='Paired rock-polarity bands, schematic');ax.text(-.5,.12,'ridge',fontsize=8);ax.text(-4,.85,'alternating polarity; widths need not be equal',fontsize=8)
ax=axs[0,1];x=np.linspace(0,2,120);z=np.linspace(0,1,80);X,Z=np.meshgrid(x,z);U=np.pi*np.sin(np.pi*X)*np.cos(np.pi*Z);W=-np.pi*np.cos(np.pi*X)*np.sin(np.pi*Z)
ax.contourf(X,Z,1-Z,levels=25,cmap='coolwarm');ax.streamplot(x,z,U,W,color='k',density=.65,linewidth=.8,arrowsize=1)
ax.set(xlim=(0,2),ylim=(0,1),xticks=[],yticks=[],title='Convection rolls, schematic');ax.text(.04,.03,'hot bottom',fontsize=8);ax.text(.04,.9,'cold top',fontsize=8)
ax=axs[1,0];event=np.array([.25,.2]);stations=[(-.65,-.55),(.7,-.5),(.5,.85)];theta=np.linspace(0,2*np.pi,500)
for st,col in zip(stations,['#3b6f9c','#ba654d','#57975a']):
 st=np.array(st);r=np.linalg.norm(event-st);ax.plot(st[0]+r*np.cos(theta),st[1]+r*np.sin(theta),color=col,lw=1);ax.plot(*st,'^',color=col)
ax.plot(*event,'k*',ms=12);ax.set(xlim=(-1.2,1.2),ylim=(-1,1.2),aspect='equal',xticks=[],yticks=[],title='Ideal distance constraints in a plane');ax.text(-1.15,-.93,'triangles: stations; star: source',fontsize=8)
ax=axs[1,1];t=np.array([0,1,1,2,2,3,3]);stress=np.array([.25,1,.25,1,.25,1,.25]);ax.plot(t,stress,color='#5c608d',lw=2)
ax.set(xlabel='time (arbitrary scale)',ylabel='shear stress (arbitrary scale)',ylim=(0,1.15),title='Idealized elastic loading and release');ax.text(.12,.95,'slow loading',fontsize=8);ax.annotate('rapid release',xy=(1,.6),xytext=(1.4,.1),fontsize=8,arrowprops={'arrowstyle':'->'});ax.grid(alpha=.15)
fig.suptitle('Original concept diagrams; no measured anomaly, flow or earthquake data')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
