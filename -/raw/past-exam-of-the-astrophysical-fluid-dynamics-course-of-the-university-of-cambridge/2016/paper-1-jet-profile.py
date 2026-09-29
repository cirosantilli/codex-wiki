"""Original explanatory plot. Tested with Python 3.14, numpy and matplotlib; PNG output goes to the current directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9.5,3.9),layout='constrained');s=np.linspace(0,1,500)
a=axs[0];a.plot(s,1-s*s,color='#357ba0',lw=2,label=r'$u/U_{\max}=1-(s/r_0)^2$');a.axhline(.5,ls='--',color='#bb6b36',label=r'$\bar{u}/U_{\max}=1/2$');a.set(xlim=(0,1),ylim=(0,1.1),xlabel=r'Radial position $s/r_0$',ylabel='Normalized axial speed',title='Confined laminar profile');a.legend(fontsize=9)
a=axs[1];a.plot(s,1-(1-s*s)**4,color='#357ba0',lw=2,label='kinetic-energy flux');a.plot(s,1-(1-s*s)**2,color='#bb6b36',ls='--',label='volume flux');a.plot(s,s*s,color='#888',ls=':',label='area');a.set(xlim=(0,1),ylim=(0,1.05),xlabel=r'Enclosing radius $s/r_0$',ylabel='Fraction inside radius s',title='Cubic speed weighting emphasizes the axis');a.legend(fontsize=9);a.text(.55,.12,r'$\alpha_{\rm kinetic}=2$',fontsize=11)
fig.savefig('paper-1-jet-profile.png',dpi=160);plt.close(fig)
