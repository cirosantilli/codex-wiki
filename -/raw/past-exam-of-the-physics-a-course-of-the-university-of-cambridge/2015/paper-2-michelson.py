"""Original explanatory figure; run under Python 3.14 with numpy and matplotlib.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","savefig.facecolor":"white"})
fig=plt.figure(figsize=(11,6),layout='constrained');gs=fig.add_gridspec(2,2,width_ratios=[1,1.5]);a=fig.add_subplot(gs[:,0]);b=fig.add_subplot(gs[0,1]);d=fig.add_subplot(gs[1,1])
a.plot([-1.8,1.55],[0,0],color='#1766a5',lw=2);a.plot([0,0],[0,1.65],color='#1766a5',lw=2);a.plot([0,0],[0,-1.6],color='#c33c29',lw=2)
a.plot([-.25,.25],[-.25,.25],lw=5,color='gray');a.plot([1.65,1.65],[-.45,.45],lw=5,color='black');a.plot([-.45,.45],[1.8,1.8],lw=5,color='black')
for st,en in [((-1.5,0),(-.75,0)),((.3,0),(1.05,0)),((0,.2),(0,1)),((0,-.4),(0,-1.2))]:a.annotate('',en,st,arrowprops=dict(arrowstyle='->',color='#1766a5' if st[1]>=0 else '#c33c29'))
a.text(-1.9,.2,'source');a.text(.38,-.52,'beam splitter');a.text(1.3,.62,'M1 (movable)');a.text(.45,1.8,'M2');a.add_patch(Rectangle((-.5,-1.9),1,.25,color='slategray'));a.text(-.5,-2.15,'detector')
a.annotate('',(2.12,.16),(1.82,.16),arrowprops=dict(arrowstyle='<->'));a.text(.15,-2.55,r'$x=2(L_1-L_2)$',ha='center')
a.set(xlim=(-2.2,2.35),ylim=(-2.8,2.5),aspect='equal',title='Michelson: returning beams recombine');a.axis('off')
c=299792458.;nu=5e14;dn=1e13
for ax,w in [(b,75),(d,3)]:
 x=np.linspace(-w,w,24001);env=np.sinc(dn*x*1e-6/c);I=1+np.cos(2*np.pi*nu*x*1e-6/c)*env
 ax.plot(x,I,lw=.7,color='#1766a5');ax.plot(x,1+abs(env),'--',lw=1,color='#c33c29');ax.plot(x,1-abs(env),'--',lw=1,color='#c33c29');ax.axhline(1,lw=.6,color='gray');ax.set(xlabel=r'Optical path difference $x$ ($\mu$m)',ylabel='Normalized intensity',ylim=(-.1,2.18))
for x in [-c/dn*1e6,c/dn*1e6]:b.axvline(x,color='gray',ls=':');b.text(x,2.08,f'{x:.1f}',ha='center',fontsize=9)
b.set_title(r'Top-hat spectrum: first zeros at $\pm30\,\mu$m');d.set_title(r'Central detail: fringe period $0.600\,\mu$m')
fig.savefig('paper-2-michelson.png',dpi=170);plt.close(fig)
