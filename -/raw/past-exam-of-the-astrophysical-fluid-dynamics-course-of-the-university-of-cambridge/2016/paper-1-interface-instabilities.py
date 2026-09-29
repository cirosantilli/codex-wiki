"""Original explanatory plot. Tested with Python 3.14, numpy and matplotlib; PNG output goes to the current directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');x=np.linspace(0,2*np.pi,600);eta=.18*np.cos(2*x)
for a,title in zip(axs,['Rayleigh–Taylor: heavy above light','Kelvin–Helmholtz: shear across interface']):
 a.fill_between(x,eta,1.2,color='#e5b69f');a.fill_between(x,-1.2,eta,color='#b3d2e6');a.plot(x,eta,color='#395e71',lw=2);a.axhline(0,ls=':',color='#888',lw=.7);a.set(xlim=(0,2*np.pi),ylim=(-1.6,1.4),title=title);a.axis('off')
axs[0].text(np.pi,.85,'upper heavy fluid',ha='center');axs[0].text(np.pi,-.85,'lower light fluid',ha='center')
for xx,sgn in [(np.pi,1),(np.pi/2,-1),(3*np.pi/2,-1)]:
 yy=.18*np.cos(2*xx);axs[0].annotate('',(xx,yy+sgn*.5),(xx,yy),arrowprops={'arrowstyle':'->','color':'#965533','lw':1.7})
axs[0].annotate('gravity',(5.65,-.8),(5.65,.5),ha='center',arrowprops={'arrowstyle':'->','lw':1.5});axs[0].text(np.pi,-1.3,r'Growth: $s^2=\mathcal{A}gk$ (no surface tension)',ha='center',fontsize=9)
for yy,left,right in [(.65,1,4),(-.65,4,1)]:axs[1].annotate('',(right,yy),(left,yy),arrowprops={'arrowstyle':'->','color':'#204c67','lw':2})
axs[1].text(4.45,.65,r'$U_2$',va='center');axs[1].text(4.45,-.65,r'$U_1$',va='center');axs[1].text(np.pi,1.1,'equal densities allowed',ha='center');axs[1].text(np.pi,-1.3,r'Equal density: $s=k|U_1-U_2|/2$',ha='center',fontsize=9)
fig.savefig('paper-1-interface-instabilities.png',dpi=160);plt.close(fig)
