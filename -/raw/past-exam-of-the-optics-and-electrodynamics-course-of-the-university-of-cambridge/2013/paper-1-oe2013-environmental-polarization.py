"""Original physical scattering/reflection schematics; PNG basename to cwd.
Python 3.14, NumPy, Matplotlib.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,axes=plt.subplots(1,2,figsize=(9.4,3.9),layout='constrained')
a,b=axes
def arrow(ax,start,end,color='#284e82'):
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','color':color,'lw':2,'mutation_scale':15})
for ax in axes:ax.set(xlim=(-1.25,1.25),ylim=(-1,1.4),aspect='equal');ax.axis('off')
a.set_title('Single scattering through 90°',fontsize=12)
arrow(a,(-1.1,0),(0,0));arrow(a,(0,0),(0,1.05));a.plot(0,0,'o',color='#a66a31',ms=9)
a.text(-.65,-.20,'Incident unpolarized light',ha='center',fontsize=9)
a.text(.12,.65,'Polarization out\nof this plane',fontsize=9)
a.add_patch(Circle((0,1.12),.075,fill=False,lw=1.2));a.plot(0,1.12,'o',color='black',ms=2.5)
a.text(-.2,-.65,'Scattering plane = page\nOnly the perpendicular component survives',ha='center',fontsize=9)
b.set_title('Reflection near Brewster incidence',fontsize=12)
b.fill_between([-1.25,1.25],[-1,-1],[0,0],color='#e6eef5');b.axhline(0,color='0.4',lw=1.2);b.plot([0,0],[-.85,1.15],ls='--',color='0.6',lw=.9)
arrow(b,(-.96,.72),(0,0));arrow(b,(0,0),(.96,.72));arrow(b,(0,0),(.60,-.80))
b.text(-.94,1.05,'Unpolarized input',fontsize=9)
b.text(.35,1.05,'Reflected: s only',fontsize=9)
b.add_patch(Circle((.85,.62),.075,fill=False,lw=1.2));b.plot(.85,.62,'o',color='black',ms=2.5)
b.text(.10,-.95,'p reflection vanishes; s is out of page',ha='center',fontsize=9)
fig.savefig('paper-1-oe2013-environmental-polarization.png',dpi=140,facecolor='white')
