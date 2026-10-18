from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
plt.rcParams.update({'font.size':11})
fig,axs=plt.subplots(1,3,figsize=(12,4),layout='constrained',facecolor='white')
blue='#126782';rust='#b14c2e'
ax=axs[0];ax.set(xlim=(0,10),ylim=(0,8));ax.axis('off');ax.set_title('Ideal pump: volume and valves')
ax.add_patch(FancyBboxPatch((.8,3.1),3,3,boxstyle='round,pad=.08',facecolor='#e2eff2',edgecolor=blue,lw=2));ax.text(2.3,4.6,'Receiver\nvolume V',ha='center',va='center')
ax.plot([3.9,5.8],[3.8,3.8],color=blue,lw=2);ax.plot([5.8,5.8],[3.8,2.9],color=blue,lw=2);ax.add_patch(Rectangle((4.8,1.2),3.1,1.7,facecolor='#f1e6df',edgecolor=rust,lw=2));ax.plot([7,7],[1.2,2.9],color=rust,lw=4);ax.plot([7,8.9],[2.05,2.05],color=rust,lw=2);ax.text(6.1,1.9,'v',ha='center',va='center');ax.plot([4.65,4.65],[3.4,4.2],color='black',lw=3);ax.text(4.7,4.65,'Valve',ha='center');ax.annotate('Outlet / reset',xy=(5.1,1.2),xytext=(3,.2),arrowprops={'arrowstyle':'->'},ha='center');ax.text(5,6.9,'Withdraw, isolate, expel; repeat',ha='center',fontsize=10)
ax=axs[1];N=np.arange(31)
for ratio in [.1,.25,.5]:ax.plot(N,(1/(1+ratio))**N,label=f'v/V = {ratio:g}')
ax.set(xlabel='Ideal pumping cycles N',ylabel='Receiver pressure / initial pressure',title='Same instructions, different pressures',ylim=(0,1.02));ax.grid(alpha=.2);ax.legend(fontsize=10)
ax=axs[2];ax.set(xlim=(0,10),ylim=(0,8));ax.axis('off');ax.set_title('Closed boundary: count the gas too')
for xpos,metal,gas,title in [(1,50,10,'Before'),(6,54,6,'After')]:
 ax.add_patch(FancyBboxPatch((xpos,2.1),2.8,3.9,boxstyle='round,pad=.05',facecolor='#e2eff2',edgecolor=blue,lw=2))
 ax.add_patch(Rectangle((xpos+.3,2.4),2.2,.8,facecolor=rust,alpha=.85));ax.text(xpos+1.4,2.8,f'Metal: {metal}',ha='center',va='center',color='white',fontsize=10);ax.text(xpos+1.4,4.5,f'Gas: {gas}',ha='center',va='center');ax.text(xpos+1.4,6.5,title,ha='center');ax.text(xpos+1.4,1.2,f'Total: {metal+gas}',ha='center',weight='bold')
ax.annotate('',xy=(6,3.7),xytext=(4,3.7),arrowprops={'arrowstyle':'->'});ax.text(5,.2,'Illustrative mass units; sealed vessels',ha='center',fontsize=10)
fig.suptitle('Modern explanatory models, not reconstructions of a specific historical instrument or measurement',fontsize=11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
