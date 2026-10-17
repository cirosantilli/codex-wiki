"""Original explanatory figure; run under Python 3.14 with numpy and matplotlib.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(11,3.8),layout='constrained');a=axs[0];k=np.linspace(-1,1,300)
a.plot(k,-k*k,label='valence-electron band');a.plot(k,k*k,label='hole energy');a.axhline(0,color='gray',lw=.6);a.set(xlabel='Wave number (schematic)',ylabel='Energy from band edge',title='Missing-electron description');a.legend(loc='lower center',fontsize=8,frameon=False);a.set_xticks([]);a.set_yticks([])
a=axs[1];a.add_patch(Rectangle((-.9,-.45),1.8,.9,facecolor='#e8edf6',edgecolor='black'));a.annotate('',(.65,0),(-.65,0),arrowprops=dict(arrowstyle='->',color='#1766a5',lw=2));a.text(-.15,.1,r'$j_x$')
for yy in [-.45,.45]:a.plot([0,0],[yy,yy*1.8],color='black')
a.annotate('',(1.15,.5),(1.15,-.3),arrowprops=dict(arrowstyle='->',color='#c33c29'));a.text(1.22,.2,r'$E_y$');a.text(-.68,.26,'−  −  −',color='#1766a5');a.text(-.68,-.37,'+  +  +',color='#c33c29');a.text(-.9,.95,r'$B_z$ out of page: $\odot$');a.text(-.87,-1.0,r'$R_H=E_y/(j_xB_z)>0$');a.set(xlim=(-1.2,1.6),ylim=(-1.3,1.4),aspect='equal',title='Hole-dominated Hall bar');a.axis('off')
a=axs[2]
a.add_patch(Rectangle((0,-.8),1.5,.8,facecolor='#cbdcf0'));a.add_patch(Rectangle((0,1.3),1.5,.45,facecolor='#e3e9ee'));a.plot([0,1.5],[.3,.3],color='#c33c29',lw=2);a.annotate('',(.75,.29),(.75,0),arrowprops=dict(arrowstyle='->',color='#1766a5'));a.text(.8,.11,r'$e^-$');a.text(.05,-.55,'valence band');a.text(.05,1.44,'conduction');a.text(.1,.44,'acceptor level');a.text(.1,.77,'energy ↑');a.text(.2,-1.08,'electron accepted;\nmobile hole left behind',ha='left',fontsize=9);a.set(xlim=(-.1,1.75),ylim=(-1.3,1.85),title='Shallow acceptor (schematic)');a.axis('off')
fig.savefig('paper-2-holes.png',dpi=170);plt.close(fig)
