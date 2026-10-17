"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(7,4));x=np.linspace(-3,3,500);n=10**x
S=1/(1+np.exp(x));sig=1/(1+np.exp(-1.7*(x-.3)));kap=.18+.82*sig;zt=S*S*sig/kap;zt/=zt.max()
for y,t,c in [(S,'|S|','#126ca0'),(sig,'Electrical conductivity','#c06a13'),(kap,'Total thermal conductivity','#2f8a51'),(zt,'ZT (scaled)','#a14b9d')]:ax.semilogx(n,y,label=t,color=c,lw=2)
ax.axvspan(.2,2,color='#e9e0f0',alpha=.45);ax.text(.6,1.08,'Doped-semiconductor compromise',ha='center',fontsize=9)
ax.set(xlabel='Carrier concentration (arbitrary logarithmic scale)',ylabel='Separately scaled qualitative properties',ylim=(0,1.2));ax.set_yticks([]);ax.legend(frameon=False,fontsize=9,loc='center left');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
