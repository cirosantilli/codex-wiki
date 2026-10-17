"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Writes one PNG basename to cwd; no source-image pixels or hardcoded media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(12,6.8),layout='constrained');a,b,c,d=axs.flat
for x0,txt in [(0,'H oven'),(1.7,'electron\nexcitation'),(3.4,'microwaves\n+ static B'),(5.1,'metal target\ncurrent')]:
 a.add_patch(Rectangle((x0,0),1.3,.7,facecolor='#e2edf7',edgecolor='gray'));a.text(x0+.65,.35,txt,ha='center',va='center',fontsize=9)
 if x0<5:a.annotate('',(x0+1.65,.35),(x0+1.3,.35),arrowprops=dict(arrowstyle='->'))
a.text(3.9,-.55,'On resonance: metastable population quenched',ha='center',fontsize=9);a.set(xlim=(-.2,6.65),ylim=(-.9,1.2),title='Metastable-beam readout (schematic)');a.axis('off')
for y,t,col in [(0,r'$2P_{1/2}$','#1766a5'),(.9,r'$2S_{1/2}$','#c33c29'),(2.5,r'$2P_{3/2}$','#1766a5')]:
 c.plot([.2,1.2],[y,y],color=col,lw=2);c.text(1.3,y,t,va='center')
c.annotate('',(.6,.85),(.6,.05),arrowprops=dict(arrowstyle='<->'));c.text(-.05,.45,'Lamb\nshift',ha='right',fontsize=9);c.text(.2,-.6,'Not to energy scale; microwave quenching locates levels',fontsize=9);c.set(xlim=(-.5,3.5),ylim=(-.9,3),title='Radiative shift removes Dirac degeneracy');c.axis('off')
for y,txt,style in [(0,r'$|g\rangle$','-'),(1.1,'virtual contribution','--'),(2.5,r'$|f\rangle$','-')]:
 b.plot([0,1.2],[y,y],ls=style,color='gray' if style=='--' else '#1766a5');b.text(1.35,y,txt,va='center',fontsize=9)
b.annotate('',(.4,1.04),(.4,.05),arrowprops=dict(arrowstyle='->',color='#c33c29',lw=2));b.annotate('',(.8,2.45),(.8,1.15),arrowprops=dict(arrowstyle='->',color='#c33c29',lw=2));b.text(.05,.6,r'$\hbar\omega_1$');b.text(.9,1.8,r'$\hbar\omega_2$');b.set(xlim=(-.15,4),ylim=(-.3,3),title='Two absorptions; both time orderings contribute');b.axis('off')
d.add_patch(Ellipse((0,0),1.1,.7,facecolor='#e2edf7',edgecolor='gray'));d.text(0,0,'atoms',ha='center');d.annotate('',(-.5,0),(-2.3,0),arrowprops=dict(arrowstyle='->',color='#c33c29',lw=3));d.annotate('',(.5,0),(2.3,0),arrowprops=dict(arrowstyle='->',color='#1766a5',lw=3));d.text(-1.9,.25,r'$\mathbf{k}_1$');d.text(1.3,.25,r'$\mathbf{k}_2=-\mathbf{k}_1$');d.text(0,-.8,'Opposite photons cancel first-order Doppler shift',ha='center',fontsize=9);d.set(xlim=(-2.7,2.7),ylim=(-1.2,1.2),title='Counterpropagating equal-frequency beams');d.axis('off')
fig.savefig('paper-1-lamb-two-photon.png',dpi=165);plt.close(fig)
