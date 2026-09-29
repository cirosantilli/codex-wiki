"""Original lens sketch; Python 3.14, root numpy/matplotlib dependencies.

Writes PNG basename to caller CWD, respecting caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
th=np.linspace(0,2*np.pi,1001)
t=np.linspace(0,np.pi/2,501)
fig,ax=plt.subplots(figsize=(6,6),dpi=120,facecolor='white');ax.set_facecolor('white')
ax.plot(np.cos(th),np.sin(th),color='#91a8b4',linewidth=1.2)
ax.plot(1+np.cos(th),1+np.sin(th),color='#bba999',linewidth=1.2)
arc0=np.column_stack([np.cos(t),np.sin(t)])
arc1=np.column_stack([1-np.cos(t),1-np.sin(t)])
lens=np.vstack([arc0,arc1])
ax.fill(lens[:,0],lens[:,1],facecolor='#dbeef5',edgecolor='none')
ax.plot(arc0[:,0],arc0[:,1],color='#18567b',linewidth=2.4)
ax.plot(arc1[:,0],arc1[:,1],color='#a36332',linewidth=2.4)
ax.scatter([1,0],[0,1],s=48,facecolors='white',edgecolors='#333333',zorder=4)
ax.text(1.06,-.12,'1',fontsize=12);ax.text(-.12,1.08,'i',fontsize=12)
ax.plot([0,1],[0,1],'.',color='#555555')
ax.text(-.15,-.15,'0');ax.text(1.04,1.08,'1+i')
ax.text(.5,.5,'A',ha='center',va='center',fontsize=16)
ax.axhline(0,color='#dddddd',linewidth=.7);ax.axvline(0,color='#dddddd',linewidth=.7)
ax.set(xlim=(-1.15,2.15),ylim=(-1.15,2.15),xlabel='Re z',ylabel='Im z',title='Intersection of two open unit discs')
ax.set_aspect('equal');fig.tight_layout();fig.savefig('paper-1-circular-lens.png',facecolor='white',transparent=False);plt.close(fig)
