"""Original calculated illustration; Python3.14,NumPy,Matplotlib; PNG output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
h=1.054571817e-34;m=9.1093837139e-31;e=1.602176634e-19;Eg=.18;mc=.14;mh=.4;kc=np.sqrt(2*m*(mc*mh/(mc+mh))*.32*e)/h/1e9
fig,axs=plt.subplots(1,2,figsize=(10,4.3),facecolor='white',layout='constrained')
k=np.linspace(-1.4,1.4,500);Ec=Eg+h*h*(1e9*k)**2/(2*mc*m*e);Ev=-h*h*(1e9*k)**2/(2*mh*m*e)
axs[0].plot(k,Ec,color='#296c9e',label='Conduction band');axs[0].plot(k,Ev,color='#ad5932',label='Valence band');ei=-.32*mc/(mc+mh);ef=Eg+.32*mh/(mc+mh)
axs[0].annotate('',xy=(kc,ef),xytext=(kc,ei),arrowprops=dict(arrowstyle='->',lw=2,color='#286747'));axs[0].text(kc-.05,(ef+ei)/2,'0.500 eV photon',rotation=90,ha='right',va='center',fontsize=9);axs[0].scatter([kc,kc],[ei,ef],color='#286747',s=20)
axs[0].set(xlabel=r'$k$ / $10^9$ m$^{-1}$',ylabel='Electron energy / eV',ylim=(-.27,.7),title='Direct transition at the same wavevector');axs[0].legend(fontsize=8,loc='upper center');axs[0].grid(alpha=.2)
a=axs[1];a.axhspan(-.05,0,color='#ad5932',alpha=.18);a.axhspan(.18,.24,color='#296c9e',alpha=.18);a.axhline(0,color='#ad5932');a.axhline(.18,color='#296c9e');a.plot([.1,.42],[.158,.158],color='#296c9e',lw=2);a.plot([.58,.9],[.022,.022],color='#ad5932',lw=2)
a.text(.25,.14,'Shallow donor',ha='center',fontsize=9);a.text(.74,.04,'Shallow acceptor',ha='center',fontsize=9);a.text(.04,.19,'Conduction edge');a.text(.04,-.035,'Valence edge');a.text(.5,.1,'Gap\nPositions schematic',ha='center',va='center',fontsize=10)
a.set(xlim=(0,1),ylim=(-.05,.24),title='Separate n-type and p-type impurity cases');a.axis('off')
fig.savefig('paper-2-semiconductor-bands.png',dpi=150,facecolor='white');plt.close(fig)
