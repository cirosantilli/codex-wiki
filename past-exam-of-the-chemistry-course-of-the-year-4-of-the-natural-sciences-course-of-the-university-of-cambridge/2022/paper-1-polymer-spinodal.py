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

N=20;p=np.linspace(.015,.985,500);chi=(1/(N*p)+1/(1-p))/2
pc=1/(1+np.sqrt(N));chic=(1+1/np.sqrt(N))**2/2
fig,ax=plt.subplots(figsize=(6.6,4.4),layout='constrained')
ax.fill_between(p,chi,4,color='#ffe2cc');ax.plot(p,chi,color='#9d430a',lw=2.4)
ax.scatter([pc],[chic],color='black',zorder=3)
ax.annotate('critical point',(pc,chic),(.37,.92),arrowprops={'arrowstyle':'->'})
ax.text(.29,2.7,"Locally unstable: f'' < 0",fontsize=12)
ax.text(.45,.48,"Locally stable: f'' > 0",fontsize=11)
ax.set(xlim=(0,1),ylim=(0,3.5),xlabel=r'Polymer volume fraction $\phi$',ylabel=r'Interaction parameter $\chi$',title='Spinodal for an illustrative chain length N = 20')
ax.grid(alpha=.15);save(fig,OUT)
