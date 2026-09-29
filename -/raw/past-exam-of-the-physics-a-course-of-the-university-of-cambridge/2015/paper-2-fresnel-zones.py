"""Original explanatory figure; run under Python 3.14 with numpy and matplotlib.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(12,3.8),layout='constrained')
a=axs[0];a.plot([0,0],[-1.3,1.3],color='gray',lw=3);a.plot([-.5,3],[0,0],':',color='gray')
a.plot([0,2.5],[.95,0],color='#1766a5',lw=2);a.plot(2.5,0,'ko');a.text(2.55,0,'P')
a.annotate('',(0,-.9),(2.5,-.9),arrowprops=dict(arrowstyle='<->'));a.text(1.2,-1.1,'b')
a.annotate('',(.15,0),(.15,.95),arrowprops=dict(arrowstyle='<->'));a.text(.24,.5,'r')
a.plot([0,.85],[.95,.95],':',color='gray');ang=np.linspace(-np.arctan(.95/2.5),0,35);a.plot(.6*np.cos(ang),.95+.6*np.sin(ang),color='black');a.text(.72,.72,r'$\theta$')
a.text(1.0,.58,r'$R=\sqrt{b^2+r^2}$');a.text(-.3,1.4,'aperture');a.text(1.6,-.42,r'$R-b\simeq r^2/(2b)$')
a.axis('off');a.set(xlim=(-.55,3.2),ylim=(-1.3,1.7),title='Fresnel propagation geometry')
a=axs[1];lim=np.sqrt(7);xy=np.linspace(-lim,lim,600);X,Y=np.meshgrid(xy,xy);s=X*X+Y*Y
n=np.floor(s).astype(int)+1;img=np.ones_like(s);img[(n%2==0)&(s<7)]=.12;img[s>=7]=.8
a.imshow(img,extent=(-lim,lim,-lim,lim),cmap='gray',vmin=0,vmax=1,origin='lower')
for j in [1,3,5]:a.text(np.sqrt(j)-.19,.08,str(j),color='#c33c29',weight='bold',fontsize=11)
a.text(0,-3.16,'Odd zones open; even zones blocked',ha='center');a.set_title('Illustrative amplitude zone plate');a.axis('off')
a=axs[2]
# With phase variable t, the cumulative integral is sin(t)+i(1-cos(t)).
t=np.linspace(0,4*np.pi,400);a.plot(np.sin(t),1-np.cos(t),color='gray',alpha=.45)
for j in range(4):
 start=np.array([0.,0.]) if j%2==0 else np.array([0.,2.]);end=np.array([0.,2.]) if j%2==0 else np.array([0.,0.])
 a.annotate('',end+.03*j*np.array([1,0]),start+.03*j*np.array([1,0]),arrowprops=dict(arrowstyle='->',color='#1766a5' if j%2==0 else '#c33c29',lw=1.5))
a.text(-1.1,-.42,'All zones: alternate phasors cancel',fontsize=9)
a.annotate('',(2,2),(2,0),arrowprops=dict(arrowstyle='->',color='#1766a5',lw=2));a.annotate('',(2,4),(2,2),arrowprops=dict(arrowstyle='->',color='#1766a5',lw=2))
a.text(2.2,1.1,'zone 1');a.text(2.2,3.1,'zone 3');a.text(1.45,-.85,'Open-zone sum',fontsize=9)
a.axhline(0,color='gray',lw=.6);a.set(xlim=(-1.6,4.2),ylim=(-1.3,4.6),xlabel='Real amplitude',ylabel='Imaginary amplitude',title='Integrated zone phasors (schematic)');a.set_xticks([]);a.set_yticks([])
fig.savefig('paper-2-fresnel-zones.png',dpi=170);plt.close(fig)
