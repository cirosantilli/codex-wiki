import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

x=np.linspace(.5,3.5,1400);p=8/(3*x-1)-3/x**2
fig,ax=plt.subplots(figsize=(6.5,4.3),layout='constrained');ax.plot(x,p);ax.plot(1,1,'ro');ax.plot([.7,1.4],[1,1],'--',color='.5',lw=1);ax.annotate(r'Critical point: $(V_c,p_c)$'+'\n'+r'$p_V=p_{VV}=0$',xy=(1,1),xytext=(1.6,2.4),arrowprops={'arrowstyle':'->'});ax.set(xlabel=r'$V/V_c$',ylabel=r'$p/p_c$',title=r'Critical isotherm: $p/p_c=8/(3x-1)-3/x^2$',xlim=(.5,3.5),ylim=(0,4.3));ax.grid(alpha=.15)
fig.savefig('paper-1-critical-isotherm.png',dpi=155)
