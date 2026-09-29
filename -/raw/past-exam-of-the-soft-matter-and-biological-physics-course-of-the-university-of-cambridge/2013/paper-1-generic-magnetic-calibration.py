"""Original generic synthetic tether apparatus; no biomolecular depiction."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
fig,axs=plt.subplots(1,2,figsize=(9,4),layout='constrained');ax=axs[0]
ax.add_patch(Rectangle((-.6,3),1.2,.45,color='#b2182b'));ax.text(0,3.23,'Magnet',ha='center',color='white');ax.add_patch(Circle((0,2.1),.26,color='#2166ac'));ax.plot([0,0],[.25,1.84],color='black',lw=2);ax.plot([-.9,.9],[.25,.25],color='grey',lw=5)
ax.annotate('',xy=(0,2.9),xytext=(0,2.45),arrowprops={'arrowstyle':'->','lw':2});ax.text(.12,2.7,r'$F_z$');ax.text(.12,1.05,'Generic tether');ax.annotate('',xy=(-.5,1.84),xytext=(-.5,.25),arrowprops={'arrowstyle':'<->'});ax.text(-.66,1,r'$h$');ax.text(0,-.2,'Optical position tracking',ha='center');ax.set(xlim=(-1.1,1.1),ylim=(-.45,3.7),title='Generic force clamp');ax.axis('off');ax.set_aspect('equal')
x=np.linspace(-2.7,2.7,400);axs[1].plot(x,.5*x*x,lw=2);axs[1].set(xlabel=r'$x/\sqrt{k_BTh/F_z}$',ylabel=r'$\Delta U/(k_BT)$',title='Transverse restoring potential');axs[1].text(-2.3,3,r'$\Delta U=F_zx^2/(2h)$');axs[1].grid(alpha=.2)
fig.savefig('paper-1-generic-magnetic-calibration.png',dpi=170,facecolor='white');plt.close(fig)
