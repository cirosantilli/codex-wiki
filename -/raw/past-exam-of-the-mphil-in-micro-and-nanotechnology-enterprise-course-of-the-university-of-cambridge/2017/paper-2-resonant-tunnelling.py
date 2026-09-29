"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

def prop(q,d):return np.array([[np.cos(q*d),np.sin(q*d)/q],[-q*np.sin(q*d),np.cos(q*d)]],dtype=complex)
def trans(energy,double):
 k=np.sqrt(energy);q=np.sqrt(energy-1+0j);P=prop(q,1.3)
 if double:P=P@prop(k,4.)@P
 vp=np.array([1,1j*k]);vm=np.array([1,-1j*k]);r,t=np.linalg.solve(np.column_stack((P@vm,-vp)),-P@vp);return abs(t)**2
fig,axs=plt.subplots(1,2,figsize=(8.5,3.7));e=np.linspace(.005,.995,1600);axs[0].plot(e,[trans(x,False) for x in e],label='Single barrier',color='#b67825');axs[0].plot(e,[trans(x,True) for x in e],label='Symmetric double barrier',color='#176b9a');axs[0].set(xlabel='Energy / barrier height',ylabel='Transmission probability',ylim=(0,1.05));axs[0].legend(fontsize=8,frameon=False)
v=np.linspace(0,2,600);i=v*(.15+2*np.exp(-((v-.7)/.28)**2))+.5*np.maximum(v-1.35,0)**2;axs[1].plot(v,i,color='#176b9a');axs[1].axvspan(.75,1.1,color='#eadde8',alpha=.7);axs[1].text(.95,1.35,'NDR',ha='center');axs[1].set(xlabel='Bias (schematic)',ylabel='Current (schematic)');axs[1].set_xticks([]);axs[1].set_yticks([]);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
