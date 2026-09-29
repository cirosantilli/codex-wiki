"""Original QED diagrams. Output is a PNG basename in caller cwd.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 system +dfsg1.
Caller-provided MPLCONFIGDIR is preserved.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
fig,axs=plt.subplots(2,2,figsize=(10.5,7.2001),dpi=100,facecolor='white')
def photon(ax,start,end):
 a=np.array(start);b=np.array(end);d=b-a;normal=np.array([-d[1],d[0]])/np.linalg.norm(d)
 t=np.linspace(0,1,260);v=a[:,None]+d[:,None]*t+normal[:,None]*(.12*np.sin(2*np.pi*7*t))
 ax.plot(v[0],v[1],color='#2175a0',lw=1.8)
def diagram(ax,title,left,right,leftph,rightph,route):
 ax.set(xlim=(0,10),ylim=(0,6));ax.axis('off');ax.set_facecolor('white')
 ax.text(5,5.70,title,ha='center',fontsize=14,weight='bold')
 ax.plot([.55,9.45],[2.15,2.15],color='#243546',lw=1.8)
 for x in [1.5,4.0,7.4]:ax.add_patch(FancyArrowPatch((x,2.15),(x+.7,2.15),arrowstyle='-|>',mutation_scale=14,color='#243546',lw=1.3))
 ax.scatter([3,6.8],[2.15,2.15],s=28,color='#243546',zorder=5)
 photon(ax,(3,2.15),(1.2,4.55));photon(ax,(6.8,2.15),(8.6,4.55))
 ax.text(1.35,4.87,leftph,ha='center',fontsize=12)
 ax.text(8.5,4.87,rightph,ha='center',fontsize=12)
 ax.text(1.0,1.20,left,ha='left',fontsize=12)
 ax.text(9.2,1.20,right,ha='right',fontsize=12)
 ax.text(4.9,1.15,route,ha='center',fontsize=12,color='#172636')
diagram(axs[0,0],'Annihilation: t channel',r'$\mu^-\mathrm{\ in},\ p_1$',r'$\mu^+\mathrm{\ in},\ p_2$',r'$\gamma\mathrm{\ out},\ k_1$',r'$\gamma\mathrm{\ out},\ k_2$',r'$q=p_1-k_1$')
diagram(axs[0,1],'Annihilation: u channel',r'$\mu^-\mathrm{\ in},\ p_1$',r'$\mu^+\mathrm{\ in},\ p_2$',r'$\gamma\mathrm{\ out},\ k_2$',r'$\gamma\mathrm{\ out},\ k_1$',r'$q=p_1-k_2$')
diagram(axs[1,0],'Compton scattering: s channel',r'$\mu^-\mathrm{\ in},\ p$',r'$\mu^-\mathrm{\ out},\ p\prime$',r'$\gamma\mathrm{\ in},\ k$',r'$\gamma\mathrm{\ out},\ k\prime$',r'$q=p+k$')
diagram(axs[1,1],'Compton scattering: u channel',r'$\mu^-\mathrm{\ in},\ p$',r'$\mu^-\mathrm{\ out},\ p\prime$',r'$\gamma\mathrm{\ out},\ k\prime$',r'$\gamma\mathrm{\ in},\ k$',r'$q=p-k\prime$')
fig.subplots_adjust(left=.02,right=.98,bottom=.07,top=.93,wspace=.04,hspace=.15)
fig.suptitle('Tree-level muon–photon amplitudes',fontsize=18,weight='bold',y=.985)
fig.text(.5,.028,'Arrows show fermion flow; photon labels specify incoming or outgoing legs.',ha='center',fontsize=12)
fig.savefig('paper-46-tree-diagrams.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
