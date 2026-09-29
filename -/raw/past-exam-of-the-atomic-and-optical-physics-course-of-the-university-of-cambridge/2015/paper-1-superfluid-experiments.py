"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Writes one PNG basename to cwd; no source-image pixels or hardcoded media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(12,3.9),layout='constrained');a,b,c=axs
a.add_patch(Ellipse((0,0),4,1.4,facecolor='#d7e9f5',edgecolor='#1766a5'));a.plot([0,0],[-1,1],color='#c33c29',lw=9,alpha=.7);a.annotate('',(1,.95),(-1,.95),arrowprops=dict(arrowstyle='<->',color='black'));a.text(0,1.2,'scan speed v',ha='center');a.text(0,-1.25,'Compare moving and stationary obstacle',ha='center',fontsize=9);a.set(xlim=(-2.5,2.5),ylim=(-1.7,1.7),aspect='equal',title='Repulsive optical obstacle in sodium');a.axis('off')
b.add_patch(Ellipse((0,0),2.8,1.8,angle=25,facecolor='#d7e9f5',edgecolor='#1766a5'));th=np.linspace(.2,5.8,180);b.plot(1.55*np.cos(th),1.55*np.sin(th),color='#c33c29');b.annotate('',(1.55*np.cos(5.8),1.55*np.sin(5.8)),(1.55*np.cos(5.55),1.55*np.sin(5.55)),arrowprops=dict(arrowstyle='->',color='#c33c29'));b.text(0,-2,'Rotate weak anisotropy; release and image',ha='center',fontsize=9);b.set(xlim=(-2.4,2.4),ylim=(-2.3,2),aspect='equal',title='Stirred rubidium condensate');b.axis('off')
x=np.linspace(-1,1,400);X,Y=np.meshgrid(x,x);r2=X*X+Y*Y;rho=np.maximum(1-r2,0)*r2/(r2+.035);c.imshow(rho,extent=(-1,1,-1,1),origin='lower',cmap='Blues');c.text(0,1.15,r'$\oint\mathbf{v}_s\cdot d\mathbf{l}=h/m$',ha='center');c.text(0,-1.25,'Illustrative core profile; not experimental data',ha='center',fontsize=9);c.set(xlim=(-1.35,1.35),ylim=(-1.4,1.4),title='Single quantized vortex');c.axis('off')
fig.savefig('paper-1-superfluid-experiments.png',dpi=165);plt.close(fig)
