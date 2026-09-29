"""Original functional sketch and analytic probability plots, not source data.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Writes only CWD basename PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Ellipse,Circle,FancyArrowPatch
fig,axs=plt.subplots(1,2,figsize=(10.5,4.3),layout='constrained',facecolor='white')
a=axs[0]
a.add_patch(Rectangle((-.2,.5),3.7,.34,facecolor='#ebe1cd',edgecolor='#ad9a78'))
a.add_patch(Ellipse((1.45,.67),.9,.6,facecolor='#83b5d0',edgecolor='#27678e',lw=1.5))
a.add_patch(Rectangle((1.34,.8),.22,1,facecolor='#83b5d0',edgecolor='#27678e'))
a.add_patch(Rectangle((2.48,.68),.13,1.6,facecolor='#b4b4b4',edgecolor='#666666'))
a.plot([1.5,2.55],[2.2,2.2],color='#666666',lw=3)
for x,y,label,color in [(1.05,2.08,'O','#f0d9ae'),(1.85,2.08,'L','#bad4b0'),(1.45,1.65,'T','#e6b5b0')]:
 a.add_patch(Circle((x,y),.34,facecolor=color,edgecolor='#555555'));a.text(x,y,label,ha='center',va='center',fontsize=12)
a.text(1.45,2.62,r'$F_1:\ \alpha_3\beta_3$ head',ha='center')
a.text(.05,1.25,r'$\gamma$ shaft',fontsize=10);a.annotate('',xy=(1.35,1.3),xytext=(.82,1.3),arrowprops=dict(arrowstyle='->'))
a.text(2.72,1.7,'Stator',rotation=90,ha='center',va='center')
a.text(1.4,.12,r'$F_o$ rotor / $c$ ring',ha='center')
a.text(-.1,.94,r'$H^+$');a.annotate('',xy=(.83,.64),xytext=(.2,.99),arrowprops=dict(arrowstyle='->',color='#b55d21',lw=1.8))
a.text(2.3,.12,r'$H^+$');a.annotate('',xy=(2.32,.3),xytext=(1.9,.65),arrowprops=dict(arrowstyle='->',color='#b55d21',lw=1.8))
a.text(1.45,-.25,'Downhill proton flow can drive ATP synthesis',ha='center',fontsize=9)
a.set(xlim=(-.3,3.55),ylim=(-.4,2.85),aspect='equal');a.axis('off');a.set_title('Functional architecture (schematic)')
t=np.linspace(0,5,600);ka,kb=2.,1.;p1=np.exp(-t);p2=ka*kb/(ka-kb)*(np.exp(-kb*t)-np.exp(-ka*t));eq=t*np.exp(-t)
b=axs[1];b.plot(t,p1,label=r'$P_1$: $k_1c=1$',lw=2);b.plot(t,p2,label=r'$P_2$: $k_a=2,\ k_b=1$',lw=2);b.plot(t,eq,'--',label=r'Equal-rate limit: $k=1$',lw=1.7)
b.set(xlabel='Illustrative time (arbitrary unit)',ylabel='Probability density (inverse time)',xlim=(0,5),ylim=(0,1.05));b.grid(alpha=.22);b.legend(fontsize=9);b.set_title('Analytic shapes; rates are illustrative')
fig.savefig('2012-s12-atp-synthase-and-dwell-distributions.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
