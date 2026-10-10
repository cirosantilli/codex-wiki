"""Original functional four-roll geometry and a separate optical readout; no historical dimensions."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc,Rectangle
import numpy as np
fig,(a,b)=plt.subplots(1,2,figsize=(12.4,6.1),gridspec_kw={'width_ratios':[1.25,1]})
fig.patch.set_facecolor('white');fig.suptitle('Stretch a dilute polymer solution; probe its optical anisotropy',fontsize=16,y=.97)
a.set(xlim=(-2,2),ylim=(-2,2),aspect='equal');a.axis('off')
y,x=np.mgrid[-1.7:1.7:130j,-1.7:1.7:130j];vx=x.copy();vy=-y.copy();mask=np.zeros_like(x,dtype=bool)
for cx,cy in [(-1.12,1.12),(1.12,1.12),(-1.12,-1.12),(1.12,-1.12)]:mask|=(x-cx)**2+(y-cy)**2<.66**2
vx[mask]=np.nan;vy[mask]=np.nan
a.streamplot(x,y,vx,vy,color='#97b9c8',density=.65,linewidth=1,arrowsize=1.3)
for cx,cy,sg in [(-1.12,1.12,-1),(1.12,1.12,1),(-1.12,-1.12,1),(1.12,-1.12,-1)]:
 a.add_patch(Circle((cx,cy),.66,facecolor='#edf0f2',edgecolor='#45606e',lw=1.7))
 t=np.linspace(.3,4.9,100);xx=cx+.4*np.cos(sg*t);yy=cy+.4*np.sin(sg*t);a.plot(xx,yy,color='#45606e',lw=1.5)
 a.annotate('',xy=(xx[-1],yy[-1]),xytext=(xx[-6],yy[-6]),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#45606e'})
 a.text(cx,cy,'Roller',ha='center',va='center',fontsize=10)
a.plot(0,0,'o',color='#a63348',ms=6)
a.add_patch(Rectangle((-.52,-.52),1.04,1.04,fill=False,edgecolor='#a63348',ls='--'))
a.text(0,-1.95,r'Central idealization: $v_x=\dot\epsilon x$, $v_y=-\dot\epsilon y$',ha='center',fontsize=11)
a.text(0,1.92,'Inflow',ha='center',fontsize=11)
a.text(1.9,0,'Exit',ha='center',fontsize=11,rotation=90)
b.set(xlim=(0,5),ylim=(0,5));b.axis('off');b.set_title('A possible optical comparison',fontsize=13,pad=10)
for y0,label,col in [(4.0,'Polarizer','#d4e4ee'),(2.5,'Solution in the flow region','#e4efdf'),(1.0,'Analyzer / optical detector','#d4e4ee')]:
 b.add_patch(Rectangle((.5,y0),4,.45,facecolor=col,edgecolor='#555'))
 b.text(2.5,y0+.225,label,ha='center',va='center',fontsize=11)
for y0,y1 in [(3.93,3.02),(2.42,1.52)]:b.annotate('',xy=(2.5,y1),xytext=(2.5,y0),arrowprops={'arrowstyle':'->','lw':2,'color':'#a87515'})
b.text(2.5,.2,'Compare flowing and quiescent solution.\nBirefringence measures anisotropic response,\nnot a direct image of individual chains.',ha='center',fontsize=11,linespacing=1.5)
fig.text(.5,.035,'Functional teaching schematic; central flow and optical arrangement are illustrative, not a historical apparatus reconstruction.',ha='center',fontsize=10,color='#555')
fig.subplots_adjust(left=.02,right=.98,top=.86,bottom=.13,wspace=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white');plt.close(fig)
