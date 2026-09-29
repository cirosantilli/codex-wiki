"""Original charged-colloid schematic; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Illustrative positions and parameters, not experimental data. Output is in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

plt.rcParams.update({'font.size':10, 'figure.facecolor':'white'})
fig,(ax,profiles)=plt.subplots(1,2,figsize=(9,4.1),layout='constrained')
for radius, alpha in [(2.1,.08),(1.8,.10),(1.5,.13)]:
    ax.add_patch(Circle((0,0), radius, color='#6cb2df', alpha=alpha, lw=0))
ax.add_patch(Circle((0,0),1,facecolor='#fce2bc',edgecolor='#c7771b',lw=2))
for t in np.linspace(0,2*np.pi,12,endpoint=False):
    ax.text(.87*np.cos(t),.87*np.sin(t),'+',ha='center',va='center',color='#a45200',fontsize=13)
for rad, count, shift in [(1.25,11,0),(1.7,8,.3),(2.15,7,.1)]:
    for t in np.linspace(0,2*np.pi,count,endpoint=False)+shift:
        ax.text(rad*np.cos(t),rad*np.sin(t),'−',ha='center',va='center',color='#2269a1',fontsize=13)
for x,y in [(-2,.5),(1.6,1.75),(1.8,-1.6),(-1.1,-1.8),(-2.0,-1.2)]:
    ax.text(x,y,'2+',ha='center',va='center',color='#aa3e53',fontsize=10)
ax.text(0,0,'$Q>0$',ha='center',va='center',fontsize=13)
ax.annotate('',xy=(-.68,-.68),xytext=(-.07,-.07),arrowprops={'arrowstyle':'->','color':'0.35'})
ax.text(-.52,-.28,'$a$',color='0.25')
ax.text(-2.35,-2.65,'Blue −: Cl⁻ (counterions)\nRed 2+: Mg²⁺ (coions)',va='top',fontsize=10)
ax.set(xlim=(-2.55,2.55),ylim=(-3.15,2.65),aspect='equal')
ax.set_title('Diffuse screening cloud (schematic)')
ax.axis('off')
s=np.linspace(0,5,400)
u=.08*np.exp(-s)/(1+s)  # a*kappa=1; beta*e*phi(a)=0.08.
profiles.plot(s,np.exp(u),color='#2269a1',label=r'$n_{\rm Cl}/(2c)=e^u$')
profiles.plot(s,np.exp(-2*u),color='#aa3e53',label=r'$n_{\rm Mg}/c=e^{-2u}$')
profiles.axhline(1,color='0.55',ls=':',lw=1)
profiles.set(xlabel=r'Distance from surface $(r-a)/\lambda_D$',ylabel='Density / own bulk density',xlim=(0,5),ylim=(.83,1.12))
profiles.set_title('Small positive potential: $u=\u03b2e\u03c6$')
profiles.legend(loc='lower right',frameon=False,fontsize=10)
profiles.spines[['top','right']].set_visible(False)
profiles.text(.36,1.102,r'$n_{\rm Cl,\infty}=2c,\quad n_{\rm Mg,\infty}=c$',fontsize=10)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
