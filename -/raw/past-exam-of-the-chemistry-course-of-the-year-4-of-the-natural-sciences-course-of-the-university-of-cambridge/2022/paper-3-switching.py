"""Original solution diagram. Python 3.14, NumPy and Matplotlib.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, wedge, save
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
t=np.linspace(0,375,501)
fig,ax=plt.subplots(figsize=(7.1,3.7))
ax.plot([-40,0],[0,0],color='#175e91');ax.plot([0,0],[0,1],color='#175e91',lw=2)
ax.plot(t,2**(-t/75),color='#175e91',lw=2)
ax.scatter([75,150,225],[.5,.25,.125],color='#175e91')
ax.axvline(0,color='0.6',ls=':',lw=1);ax.annotate('one fuel addition',xy=(0,.98),xytext=(75,1.12),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Time after addition / min',ylabel=r'Excess 512 nm signal, normalized',xlim=(-40,375),ylim=(-.05,1.25),xticks=[0,75,150,225,300,375])
ax.spines[['right','top']].set_visible(False)
ax.text(165,.65,'Fast initial redistribution;\nfirst-order fuel-decay limit',color='#175e91')
fig.tight_layout();save(fig,'paper-3-switching.png')
