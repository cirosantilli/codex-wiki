"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained')
for ax,aa in zip(axs,[(1,2,3),(.1,1,5)]):
 a1,a2,a3=aa;s1=sum(aa);s2=a1*a2+a1*a3+a2*a3;Nm=(s1+np.sqrt(s1*s1-3*s2))/3;P=lambda n:(a1-n)*(a2-n)*(a3-n);ET=P(0);EM=P(Nm);x=np.linspace(0,a3+.1,600);ax.plot(x,P(x));ax.axhline(0,color='.6');ax.axhline(ET,color='#b9692c',ls='--',label=fr'$E_T={ET:.2g}$');ax.axhline(EM,color='#228b73',ls=':',label=fr'$E_M={EM:.2g}$');ax.scatter([0,Nm],[ET,EM],color='black');ax.set(xlabel='Population N',ylabel='Per-capita growth P(N)',title=('Upper pair disappears first' if EM<ET else 'Extinction and high population coexist'),ylim=(min(-1,-.2*max(ET,EM)),max(ET,EM)*1.2));ax.legend(fontsize=9)
fig.savefig(Path.cwd()/'2010-population-harvest.png',dpi=150,facecolor='white');plt.close(fig)
