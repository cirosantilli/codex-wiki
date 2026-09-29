"""Original schematic Galactic views, not a survey map or external photograph.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Writes only CWD basename PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Ellipse
fig,axs=plt.subplots(1,2,figsize=(10.2,4.6),layout='constrained',facecolor='white')
a=axs[0];a.add_patch(Circle((0,0),15,facecolor='#f1eee7',edgecolor='#999999',ls='--'));a.add_patch(Ellipse((0,0),7,2.2,angle=25,facecolor='#d0b5a6',edgecolor='#8a6a59'))
r=np.linspace(3.5,14.5,350)
for phase in [0,np.pi/2,np.pi,3*np.pi/2]:
 th=phase+1.7*np.log(r/3.5);a.plot(r*np.cos(th),r*np.sin(th),color='#367da8',lw=2)
 j=np.arange(25,340,55);a.scatter(r[j]*np.cos(th[j]),r[j]*np.sin(th[j]),s=12,color='#b64846')
a.scatter([8],[0],marker='*',s=90,color='#b78916',zorder=5);a.annotate('Sun, 8 kpc',xy=(8,0),xytext=(8,-5),arrowprops=dict(arrowstyle='->'),fontsize=9);a.text(-1,1.6,'Bar / bulge',fontsize=9,ha='center');a.text(-14,-17,'Bright disk radius ≈15 kpc; young arms',fontsize=9);a.set(xlim=(-18,18),ylim=(-19,18),aspect='equal',title='Face-on (schematic)');a.axis('off')
b=axs[1];b.add_patch(Ellipse((0,0),36,21,facecolor='#f2f1ee',edgecolor='#a5a29a',ls='--'));b.add_patch(Ellipse((0,0),30,3.3,facecolor='#d6c5b6',edgecolor='#ae9680'));b.add_patch(Ellipse((0,0),30,.85,facecolor='#c3d4df',edgecolor='#648aa3'));b.add_patch(Ellipse((0,0),4,5,facecolor='#d0b5a6',edgecolor='#8a6a59'));b.plot([-15,15],[0,0],color='#555555',lw=1.7)
xy=np.array([[-12,6],[-7,-6],[0,8],[8,5],[13,-4],[4,-8],[-14,-2]])
b.scatter(xy[:,0],xy[:,1],s=22,color='#8f5f4e');b.annotate('Old halo / globular clusters',xy=(-12,6),xytext=(-16,10),arrowprops=dict(arrowstyle='->'),fontsize=9);b.annotate('Thick disk',xy=(-9,1),xytext=(-16,4),arrowprops=dict(arrowstyle='->'),fontsize=9);b.annotate('Thin disk, gas and dust',xy=(11,0),xytext=(2,-5),arrowprops=dict(arrowstyle='->'),fontsize=9);b.text(0,-12,'Halo continues to many tens of kpc and beyond',ha='center',fontsize=9);b.set(xlim=(-19,19),ylim=(-14,13),aspect='equal',title='Edge-on (vertical detail enlarged)');b.axis('off')
fig.savefig('2012-s26-milky-way-structure.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
