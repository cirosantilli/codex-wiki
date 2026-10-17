"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(12,4.2),layout='constrained')
a=axs[0];a.set_title('Ewald construction (curvature exaggerated)');C=np.array([0.,-2.]);r=2.;a.add_patch(Circle(C,r,fill=False,ec='#436e8a',lw=1.5));O=np.zeros(2);G=np.array([1.,-2+np.sqrt(3)])
for x in [-1.6,-.8,0,.8,1.6]:a.plot([x,x],[-.82,.82],color='#b7c6ca',lw=2);a.plot(x,0,'o',color='#4b5963',ms=3)
for start,end,t,off in [(C,O,r'$\mathbf{k}_0$',(-.5,-1.15)),(C,G,r'$\mathbf{k}_s$',(.8,-1.3)),(O,G,r'$\mathbf{g}$',(.5,.12))]:
 a.annotate('',end,start,arrowprops={'arrowstyle':'->','color':'#135985','lw':1.7});a.text(*off,t,color='#135985')
a.plot(*C,'ko');a.text(-.25,-2.15,'C');a.text(-.25,.07,'O');a.text(1.03,G[1]+.05,'G');a.text(-1.9,.95,'foil-normal rods: width ~ 1/t',fontsize=8.5);a.set(xlim=(-2.4,2.4),ylim=(-4.3,1.3),aspect='equal');a.axis('off')
pts=np.array([[np.sqrt(2)*h,l] for h,l in [(-1,-1),(-1,1),(1,-1),(1,1),(0,-2),(0,2)]])/.4046
for a,title in zip(axs[1:],['One fcc [110] domain','Five rotated domains: illustrative model']):
 a.set_title(title);a.axhline(0,color='#e0e0e0',lw=.7);a.axvline(0,color='#e0e0e0',lw=.7);a.add_patch(Circle((0,0),1/.19,fill=False,ec='#888',ls='--'));a.plot(0,0,'ko',ms=4);a.set(xlim=(-5.8,5.8),ylim=(-5.8,5.8),aspect='equal',xlabel=r'$g_x$ / nm$^{-1}$',ylabel=r'$g_y$ / nm$^{-1}$')
axs[1].scatter(pts[:,0],pts[:,1],color=['#2d77a0']*4+['#c9792b']*2,s=38);axs[1].text(.2,4.75,'002',fontsize=8);axs[1].text(3.6,2.3,r'$1\bar{1}1$',fontsize=8);axs[1].text(-5.4,-5.1,'Dashed: 0.19 nm image cutoff',fontsize=8)
for i in range(5):
 t=np.deg2rad(72*i);rot=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]]);q=pts@rot.T;axs[2].scatter(q[:,0],q[:,1],s=22,alpha=.85,label=str(i+1))
axs[2].text(-5.4,-5.1,'Geometric construction, not a fitted FFT',fontsize=8)
fig.savefig('paper-1-ewald-and-gold.png',dpi=160);plt.close(fig)
