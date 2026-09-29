"""2017 II3 Q30. Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.
Solid: stable; dashed: unstable. Leading local normal-form sketches.
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/2017-ii-paper-3-mplconfig")
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(13.5,4.5),dpi=100,facecolor='white')
neg=np.linspace(-.24,0,500);pos=np.linspace(0,.24,500)
for ax,title in zip(axs,['a < 1: supercritical','a > 1: subcritical','a = 1: degenerate subcritical']):
 ax.plot(neg,neg*0,color='#1e537a',lw=2);ax.plot(pos,pos*0,color='#a34a35',ls='--',lw=2)
 ax.set(xlim=(-.25,.25),ylim=(-.65,.65),xlabel='μ = r − 1',ylabel='Centre coordinate u',title=title);ax.axvline(0,color='.8',lw=1);ax.grid(alpha=.15)
for sign in [-1,1]:
 axs[0].plot(pos,sign*np.sqrt(pos),color='#1e537a',lw=2)
 axs[1].plot(neg,sign*np.sqrt(-neg),color='#a34a35',ls='--',lw=2)
 axs[2].plot(neg,sign*(-neg/2)**.25,color='#a34a35',ls='--',lw=2)
fig.suptitle('Local equilibria: solid stable, dashed unstable (transverse directions stable)',fontsize=12)
fig.tight_layout(rect=(0,0,1,.92));fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False);plt.close(fig)
