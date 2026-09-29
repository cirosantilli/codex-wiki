#!/usr/bin/env python3
"""Original planetary-dynamics figure; outputs its same-basename PNG to CWD.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Dependencies match the repository pyproject; no external visual assets.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
blue='#22577a'; orange='#c66a24'; green='#387c58'; gray='#666666'
def finish(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(10,4.4),dpi=100)
e0=99/101; C=(200/101)*e0**(-.8)
e=np.linspace(.00001,e0,2500); q=C*e**.8/(1+e); Q=C*e**.8/(1-e)
for ax in axes:
    ax.plot(q,Q,color=blue,lw=2);ax.plot([0,1.1],[0,1.1],'--',color=gray,label='Circular limit Q = q')
    ax.set(xlabel=r'$q/q_0$',ylabel=r'$Q/q_0$',xlim=(0,1.07));ax.grid(alpha=.15)
axes[0].set(ylim=(0,104),title='Initial apocentre contraction')
axes[0].annotate('Start',(1,100),(.45,93),arrowprops={'arrowstyle':'->','color':gray})
axes[0].annotate('Almost fixed pericentre',(.995,58),(.12,48),arrowprops={'arrowstyle':'->','color':orange},color=orange)
axes[1].set(ylim=(0,4),title='Magnified late evolution')
ehalf=.5;qhalf=C*ehalf**.8/(1+ehalf);Qhalf=C*ehalf**.8/(1-ehalf)
axes[1].plot(qhalf,Qhalf,'o',color=orange);axes[1].annotate('e = 1/2',(qhalf,Qhalf),(.35,3.1),arrowprops={'arrowstyle':'->','color':orange})
axes[1].annotate('Inward migration',(.28,.4),(.04,1.5),arrowprops={'arrowstyle':'->','color':green},color=green)
axes[1].legend(loc='upper left');fig.tight_layout();finish(fig)
