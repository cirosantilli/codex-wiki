"""Original functional gate/readout diagram and stipulated zero-temperature model."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

e=1.602176634e-19;hbar=6.62607015e-34/(2*np.pi);v=1e6;cg=.010
V=np.linspace(-1,1,801);alpha=e**3/(np.pi*(hbar*v)**2*cg)
u=2*np.abs(V)/(1+np.sqrt(1+4*alpha*np.abs(V)))
n=np.sign(V)*e**2*u**2/(np.pi*(hbar*v)**2)
cq=2*e**3*u/(np.pi*(hbar*v)**2);cdiff=cg*cq/(cg+cq)
fig=plt.figure(figsize=(12,5.7),dpi=140,facecolor='white');gs=fig.add_gridspec(2,2,width_ratios=[.95,1.18],hspace=.44,wspace=.31)
ax=fig.add_subplot(gs[:,0]);ax.set(xlim=(-.7,7.8),ylim=(-.1,7));ax.axis('off')
ax.text(3.2,6.55,'Separate density control and transport readout',ha='center',fontsize=11,weight='bold')
ax.add_patch(Rectangle((.5,4.2),5.5,.8,facecolor='#fae6ce',edgecolor='#bb733b',lw=1.5))
for x in [.3,5.8]:ax.add_patch(Rectangle((x,4.12),.45,.96,facecolor='#aaa',edgecolor='#555'))
for x in [1.5,4.7]:
    ax.plot([x,x],[5,5.65],color='#555');ax.scatter([x],[5],s=18,c='#555')
ax.plot([1.5,4.7],[5.65,5.65],color='#555');ax.text(3.1,5.65,r' $V_{xx}$ ',ha='center',va='center',bbox=dict(facecolor='white',edgecolor='none'),fontsize=12)
for yy in [4.2,5]:
    ax.plot([3.2,6.8],[yy,yy],color='#777',ls=':');ax.scatter([3.2],[yy],s=18,c='#555')
ax.text(6.7,5.75,r'$\odot\,B_z$',ha='center',fontsize=12)
ax.annotate('',(6.8,5),(6.8,4.2),arrowprops=dict(arrowstyle='<->',color='#444'))
ax.text(7.1,4.6,r'$V_{xy}$',va='center',fontsize=12)
ax.annotate('',(4.6,4.6),(1.4,4.6),arrowprops=dict(arrowstyle='->',lw=2,color='#555'))
ax.text(3,4.33,r'$I_x$',ha='center',fontsize=12)
ax.text(3.1,3.55,'Hall-bar contacts: functional layout only',ha='center',fontsize=10)
ax.add_patch(Rectangle((.7,1.05),5.5,.65,facecolor='#ddd',edgecolor='#777'))
ax.add_patch(Rectangle((.7,1.7),5.5,.65,facecolor='#e4eff8',edgecolor='#88a8c2'))
ax.plot([.7,6.2],[2.35,2.35],color='#d07a32',lw=4)
ax.text(3.45,2.67,'Graphene + reservoir contact',ha='center',fontsize=11)
ax.text(3.45,2.02,'Insulator',ha='center',va='center',fontsize=11)
ax.text(3.45,1.37,'Gate',ha='center',va='center',fontsize=11)
ax.plot([3.45,3.45],[1.05,.5],color='#555');ax.text(3.45,.20,r'Applied $V_g$; geometric capacitance per area $c_g$',ha='center',fontsize=10)
ax2=fig.add_subplot(gs[0,1]);ax2.plot(V,n/1e16,color='#356fa3',lw=2.4,label='Self-consistent cone model')
ax2.plot(V,cg*V/e/1e16,'--',color='#bd7738',lw=1.8,label='Geometric approximation')
ax2.scatter([1],[n[-1]/1e16],s=28,color='#222',zorder=4)
ax2.set(xlabel=r'$V_g-V_0$ (V)',ylabel=r'$n$ ($10^{12}$ cm$^{-2}$)',title='Some voltage shifts the Fermi energy');ax2.legend(fontsize=9,loc='upper left',frameon=False);ax2.grid(alpha=.17)
ax3=fig.add_subplot(gs[1,1]);ax3.plot(V,cdiff/cg,color='#3a8560',lw=2.4)
ax3.set(xlabel=r'$V_g-V_0$ (V)',ylabel=r'$c_{\rm diff}/c_g$',ylim=(0,1),title='Few available states reduce differential capacitance');ax3.grid(alpha=.17)
fig.suptitle('Graphene gate control: geometric and quantum capacitance in series',fontsize=15,y=.98)
fig.text(.5,.025,r'Chosen model: $c_g=0.010$ F/m$^2$, $v_F=10^6$ m/s, $T=0$, $V_0=0$; no traps or spatial inhomogeneity. Not laboratory data.',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.98,bottom=.14,top=.86)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
