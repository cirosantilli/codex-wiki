"""Original crossed-field trajectories, Cambridge 2017 II paper 1 Q35.
Output same-basename PNG in CWD. Python 3.14.4, matplotlib 3.10.7+dfsg1,
numpy 2.3.5 tested; project pins Python3.14/matplotlib3.10.7/numpy2.3.5.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/2017-ii-paper-1-mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
fig,axs=plt.subplots(1,2,figsize=(10.4,4.5),dpi=100,facecolor='white')
for ax,beta,uc,label in zip(axs,[.005,.5],[.5,.05],['Small drift: nearly closed loops','Large drift: progressing oscillations']):
 d=beta/uc;gamma=1/np.sqrt(1-beta**2);s=np.linspace(0,6*np.pi,2401)
 x=gamma*(d*s+np.sin(s));y=np.cos(s)
 ax.plot(x,y,color='#0072B2',lw=1.7)
 for i in [250,850,1450,2050]:ax.annotate('',xy=(x[i+20],y[i+20]),xytext=(x[i],y[i]),arrowprops={'arrowstyle':'->','color':'#0072B2','lw':1.3})
 ax.set(xlabel=r'$\widetilde x$',ylabel=r'$\widetilde y$',ylim=(-1.3,1.3),title=label+'\n'+rf'$\beta={beta:g},\ u/c={uc:g},\ 2\pi\beta/(u/c)={2*np.pi*d:.3g}$')
 ax.axhline(0,color='gray',lw=.5)
 if d<1:ax.set_aspect('equal',adjustable='box')
 else:ax.text(.5,-.30,'Horizontal scale compressed to show three periods',transform=ax.transAxes,ha='center',fontsize=9)
fig.subplots_adjust(left=.07,right=.99,top=.80,bottom=.24,wspace=.35)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
