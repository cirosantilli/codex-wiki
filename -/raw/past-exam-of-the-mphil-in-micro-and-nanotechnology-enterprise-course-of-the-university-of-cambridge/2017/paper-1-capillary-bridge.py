"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9.6,3.8),layout='constrained')
a=axs[0];a.set_title('Complete-wetting narrow liquid bridge')
r=.48;a0=2;y=np.linspace(-r,r,160);xb=a0-np.sqrt(np.maximum(0,r*r-y*y));poly=np.column_stack([np.r_[-xb,xb[::-1]],np.r_[y,y[::-1]]]);a.add_patch(Polygon(poly,fc='#b5dce7',ec='#287a91',lw=1.5))
for yy in [-r-.16,r]:a.add_patch(Rectangle((-2.35,yy),4.7,.16,fc='#aaa',ec='#555'))
a.annotate('',(2.75,-r),(2.75,r),arrowprops={'arrowstyle':'<->'});a.text(2.87,0,'d',va='center');a.annotate('',(0,r+.16),(0,r+.95),arrowprops={'arrowstyle':'<-','lw':1.6});a.annotate('',(0,-r-.16),(0,-r-.95),arrowprops={'arrowstyle':'<-','lw':1.6})
a.text(.2,r+.65,'separating force');a.text(0,0,r'liquid: $p_l<P_V$',ha='center');a.text(-2.7,1.45,r'vapor: $P_V$',ha='left');a.annotate('',(0,-1.48),(a0,-1.48),arrowprops={'arrowstyle':'<->'});a.text(a0/2,-1.72,'wetted radius a',ha='center');a.set(xlim=(-3,3.3),ylim=(-2,1.9),aspect='equal');a.axis('off')
a=axs[1];a.set_title('Pressure sets the leading attraction');a.axis('off')
for yy,txt in [(0.83,r'$p_l-P_{\rm sat}=\frac{RT}{\overline{V}_l}\ln(P_V/P_{\rm sat})$'),(.59,r'$F_p=\pi a^2(P_V-p_l)$'),(.36,r'$F\simeq\frac{\pi a^2 RT}{\overline{V}_l}\ln(P_{\rm sat}/P_V)$'),(.12,r'For $\theta=0$ and $d\ll a$:  $F\simeq2\pi a^2\gamma/d$')]:a.text(.5,yy,txt,ha='center',va='center',transform=a.transAxes,fontsize=11)
fig.savefig('paper-1-capillary-bridge.png',dpi=160);plt.close(fig)
