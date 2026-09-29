"""Original explanatory figure; output basename to the current directory.

Tested with the repository Python 3.14 / NumPy / Matplotlib environment.
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, atom, wedge, ring, flow, finish, save
OUT=Path(__file__).stem+'.png'

p=np.linspace(0,.99,300)
fig,ax=plt.subplots(figsize=(7.6,4.5),layout='constrained')
ax.plot(p,1/(1-p),label='Step growth: 1/(1-p)',lw=2.4)
ax.plot(p,1+99*p,label='Fixed-chain-number insertion limit',lw=2.4)
ax.plot(p,np.full_like(p,100),label='Radical growth: illustrative chain size',lw=2.4)
ax.set(xlabel='Conversion p',ylabel='Number-average degree of polymerization',yscale='log',xlim=(0,1),ylim=(.9,160))
ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=9)
ax.set_title('Growth mechanisms: qualitative comparison')
ax.text(.015,125,'Scale choices are illustrative; radical-chain length is condition-dependent.',fontsize=8)
save(fig,OUT)
