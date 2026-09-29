"""Original lemniscate/map-boundary diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; the PNG is written to caller CWD.
The caller's MPLCONFIGDIR is used unchanged.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=math.sqrt(math.pi)*math.gamma(.25)/(4*math.gamma(.75))
fig,axes=plt.subplots(1,3,figsize=(10.8,3.6),dpi=130,facecolor='white')
colors=['#c4473a','#187fab','#53813b','#9863ac']
t=np.linspace(0,1,1001)
x=t*np.sqrt((1+t*t)/2);y=t*np.sqrt((1-t*t)/2)
for sx in [-1,1]:
 for sy in [-1,1]:axes[0].plot(sx*x,sy*y,color='#374151',lw=1.8)
axes[0].plot(x,y,color=colors[0],lw=2.4)
axes[0].set_title('Lemniscate of Bernoulli',fontsize=11)
axes[0].set_xlim(-1.2,1.2);axes[0].set_ylim(-.72,.72)
axes[0].set_xlabel('$x$');axes[0].set_ylabel('$y$',rotation=0)
angle=np.linspace(0,2*np.pi,801)
axes[1].plot(np.cos(angle),np.sin(angle),color='#374151',lw=1.7)
axes[1].fill(np.cos(angle),np.sin(angle),color='#edf4f9')
vertices=[1,1j,-1,-1j];labels=['$1$','$i$','$-1$','$-i$']
for z,color,label in zip(vertices,colors,labels):
 axes[1].plot(z.real,z.imag,'o',color=color,ms=6)
 axes[1].text(1.17*z.real,1.17*z.imag,label,ha='center',va='center',fontsize=11)
axes[1].set_title('Disc: four boundary prevertices',fontsize=11)
axes[1].set_xlim(-1.37,1.37);axes[1].set_ylim(-1.37,1.37)
poly=np.array([B,1j*B,-B,-1j*B,B])
axes[2].fill(poly.real,poly.imag,color='#edf4f9')
axes[2].plot(poly.real,poly.imag,color='#374151',lw=1.8)
for z,color,label in zip(vertices,colors,['$B$','$iB$','$-B$','$-iB$']):
 axes[2].plot(B*z.real,B*z.imag,'o',color=color,ms=6)
 axes[2].text(1.16*B*z.real,1.16*B*z.imag,label,ha='center',va='center',fontsize=11)
axes[2].set_title('Image of the lemniscatic integral',fontsize=11)
axes[2].set_xlim(-1.38*B,1.38*B);axes[2].set_ylim(-1.38*B,1.38*B)
for ax in axes:
 ax.set_aspect('equal',adjustable='box');ax.set_facecolor('white')
for ax in axes[1:]:
 ax.set_xticks([]);ax.set_yticks([])
 for spine in ax.spines.values():spine.set_visible(False)
fig.text(.69,.04,r'$B=\int_0^1 (1-t^4)^{-1/2}\,dt$; matching colours show corner correspondence.',ha='center',fontsize=9)
fig.subplots_adjust(left=.075,right=.995,bottom=.17,top=.85,wspace=.23)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
