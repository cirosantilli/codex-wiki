"""Original analytical diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10. Writes basename into cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
x=np.linspace(0,.16,250);a=axes[0]
for y,label,color in [(-x*x/6,r'$J=0,m=0$','#8a4e9f'),(x*x/10,r'$J=1,m=0$','#ce5a24'),(-x*x/20,r'$J=1,|m|=1$','#235789')]:a.plot(x,y,label=label,color=color,lw=2)
a.set(xlabel=r'$\eta=pE/B$',ylabel=r'$\delta E/B$',title='Weak-field level shifts');a.legend(fontsize=9);a.grid(alpha=.2)
z=np.linspace(0,1.4,250);a=axes[1]
a.plot(z,(4/15)*21.4*z*z,label=r'$\Delta m=0$',color='#ce5a24',lw=2)
a.plot(z,(7/60)*21.4*z*z,label=r'$|\Delta m|=1$',color='#235789',lw=2)
a.annotate('',(1,5.706666667),(1,2.496666667),arrowprops={'arrowstyle':'<->','color':'#555555'})
a.text(1.03,4.05,'3.21 MHz',fontsize=10,va='center')
a.set(xlabel=r'$E/(10^5\ \mathrm{V\,m^{-1}})$',ylabel=r'$(\nu-\nu_{01})/\mathrm{MHz}$',title='OCS transition shifts from inferred dipole')
a.legend(fontsize=9,loc='upper left');a.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
