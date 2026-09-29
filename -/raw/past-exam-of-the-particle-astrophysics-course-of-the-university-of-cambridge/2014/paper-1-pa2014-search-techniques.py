"""Original physics flow schematic, Python3.14/Matplotlib3.10; saves basename PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(10,4),layout='constrained');ax.set(xlim=(0,12),ylim=(0,5));ax.axis('off')
def box(x,y,w,text,color):
 ax.add_patch(FancyBboxPatch((x,y),w,.9,boxstyle='round,pad=.1',ec=color,fc='#f4f8fb'));ax.text(x+w/2,y+.45,text,ha='center',va='center',fontsize=10)
def arrow(x,y,z):ax.annotate('',(z,y),(x,y),arrowprops={'arrowstyle':'->','lw':2,'color':'#666666'})
box(.2,3,2.5,'halo particle','#235789');box(3.5,3,3.2,'nuclear recoil\nin underground xenon','#235789');box(7.7,3,3.6,'S1 light + S2 charge\nposition and recoil type','#235789');arrow(2.8,3.45,3.3);arrow(6.9,3.45,7.5)
box(.2,.9,2.5,'halo annihilation\nor decay','#ce5a24');box(3.5,.9,3.2,'charged secondary\ntravels through Galaxy','#ce5a24');box(7.7,.9,3.6,'space spectrometer\ncharge, momentum, species','#ce5a24');arrow(2.8,1.35,3.3);arrow(6.9,1.35,7.5)
ax.text(.2,4.5,'Direct scattering search',weight='bold',color='#235789');ax.text(.2,2.4,'Indirect search: astrophysical sources are competing explanations',weight='bold',color='#ce5a24')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
