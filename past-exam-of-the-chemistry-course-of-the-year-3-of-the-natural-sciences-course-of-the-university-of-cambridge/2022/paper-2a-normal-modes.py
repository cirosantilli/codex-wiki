"""Original solution figure. Tested with Python 3.14, numpy and matplotlib.
The PNG basename is written to the current working directory for Make's _media target.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, flow, finish, save

fig,axs=plt.subplots(2,2,figsize=(10,4.8))
def model(a,title,arrows,lab,anchor=False):
 bond(a,(0,0),(2.1,0));atom(a,(0,0),'a');atom(a,(2.1,0),'b')
 if anchor:
  a.plot([-.75,-.75],[-.45,.45],color='.4');bond(a,(-.75,0),(0,0),style='dotted')
 for x,d in zip([0,2.1],arrows):flow(a,(x,.45),(x+d,.45))
 a.text(1.05,-.65,lab,ha='center',fontsize=11)
 finish(a,(-1.2,3.4),(-1,1.1),title)
model(axs[0,0],'Free: translation',(.65,.65),r'$\delta y_a=\delta y_b$')
model(axs[0,1],'Free: internal stretch',(-.8,.4),r'$m_a\delta y_a=-m_b\delta y_b$'+'\n'+r'Illustration: $m_b=2m_a$')
model(axs[1,0],'Weak one-end anchoring: low mode',(.65,.65),r'$\omega^2\simeq k_2/(2m)$; translation-like',True)
model(axs[1,1],'Weak one-end anchoring: high mode',(-.6,.6),r'$\omega^2\simeq 2k_1/m+k_2/(2m)$',True)
fig.text(.5,.015,'Surface-bound arrows show leading-order free-mode shapes; anchoring mixes them at first order.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.045,1,1));save(fig,'paper-2a-normal-modes.png')
