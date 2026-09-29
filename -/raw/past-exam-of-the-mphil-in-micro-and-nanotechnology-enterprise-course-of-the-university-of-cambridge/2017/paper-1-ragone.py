"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
from matplotlib.patches import Ellipse
fig,a=plt.subplots(figsize=(7.7,4.5),layout='constrained');a.set_xscale('log');a.set_yscale('log')
# Draw qualitative regions in logarithmic coordinates, not measured performance boundaries.
for ex,py,wx,wy,color,name in [(-1,4.7,2.2,2.1,'#b9d9ea','capacitors'),(1,3.5,2.0,2.0,'#ead5ad','supercapacitors'),(2,1.7,2.0,2.3,'#c5dfc3','batteries')]:
 t=np.linspace(0,2*np.pi,300);a.fill(10**(ex+wx/2*np.cos(t)),10**(py+wy/2*np.sin(t)),fc=color,ec='#666',alpha=.75);a.text(10**ex,10**py,name,ha='center',va='center')
x=np.logspace(-3,4,300)
for sec in [1,60,3600]:
 y=3600*x/sec;a.plot(x,y,ls='--',lw=.9,color='#888');xx={1:.04,60:1,3600:400}[sec];a.text(xx,3600*xx/sec*1.16,{1:'1 s',60:'1 min',3600:'1 h'}[sec],color='#666',fontsize=9,rotation=30)
a.set(xlim=(.002,2500),ylim=(1,2e6),xlabel='Specific energy / Wh kg⁻¹',ylabel='Specific power / W kg⁻¹',title='Qualitative Ragone map: consistent total-device mass')
a.grid(alpha=.17,which='major');fig.savefig('paper-1-ragone.png',dpi=160);plt.close(fig)
