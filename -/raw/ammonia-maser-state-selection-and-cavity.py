"""Original functional ammonia-maser schematic, not measured geometry.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
Historical functions: Gordon, Zeiger and Townes, Phys. Rev. 95 (1954),
282–284, Fig. 1; 99 (1955), 1264–1274, pp. 1264–1267.
No voltages, construction dimensions, or measured trajectories are represented.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(11.4, 6.8), facecolor='white')
ax = fig.add_axes((0.025, 0.09, 0.95, 0.78))
ax.set(xlim=(0, 13), ylim=(0, 6.6)); ax.axis('off')
blue, orange, purple, grey = '#17659b', '#b95b15', '#7b4397', '#465465'
fig.text(.5, .955, 'Ammonia maser: select the molecules, then let the field grow',
         ha='center', va='top', fontsize=17, weight='bold', color='#162c40')
fig.text(.5, .902, 'Functional schematic • illustrative paths and spacing', ha='center', color=grey)

def box(x, y, w, h, label, color='#f2f6f9'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor=color,edgecolor=grey,lw=1.4))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center')

def arrow(a,b,color=grey,**kw):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,color=color,lw=1.7,**kw))

ax.add_patch(FancyBboxPatch((.20,1.65),10.4,3.8,boxstyle='round,pad=0.08',facecolor='#fafcfd',edgecolor='#9eacb5',linestyle='--'))
ax.text(.40,5.17,'Vacuum region',color=grey,fontsize=10)
box(.42,2.85,1.1,1.35,'NH₃\nsource')
for yy in (3.07,3.35,3.63,3.91):
    ax.plot([1.32,1.6],[yy,yy],color=grey,lw=3)
ax.text(.95,2.38,'Both inversion\nstates supplied',ha='center',color=grey)
for yy in (2.48,4.58):
    ax.add_patch(Rectangle((2.45,yy),3.15,.19,facecolor='#9eacb5',edgecolor=grey))
ax.text(4.03,4.99,'Electrostatic state selector',ha='center',weight='bold')
x=np.linspace(1.65,6.55,220)
for y0 in (-.55,.0,.55):
    t=np.clip((x-2.45)/3.15,0,1)
    yy=3.60+y0*np.cos(t*np.pi/2)
    ax.plot(x,yy,color=blue,lw=2)
    arrow((6.20,yy[-1]),(6.60,yy[-1]),blue)
for sign in (-1,1):
    xx=np.linspace(1.65,5.6,120);t=np.clip((xx-2.45)/3.15,0,1)
    yy=3.6+sign*(.34+.85*t*t)
    ax.plot(xx,yy,color=orange,lw=1.8,linestyle='--')
    arrow((xx[-7],yy[-7]),(xx[-1],yy[-1]),orange)
ax.text(4.10,2.00,'Lower states rejected',ha='center',color=orange)
ax.text(6.05,3.05,'Upper states\naccepted',ha='center',color=blue,fontsize=10)
box(6.85,2.65,2.25,1.9,'',color='#e9f4fb')
ax.text(7.97,4.15,'Resonant cavity',ha='center',weight='bold')
xx=np.linspace(7.02,8.95,160)
ax.plot(xx,3.62+.24*np.sin((xx-7.02)*5*np.pi),color=purple,lw=2)
ax.text(7.97,3.00,'Stored microwave field',ha='center',fontsize=9,color=purple)
arrow((9.17,3.60),(10.35,3.60),blue)
ax.text(10.10,2.83,'Outgoing\nmolecules',ha='center',fontsize=10,color=grey)
ax.plot([8.05,8.05,10.90],[4.56,5.83,5.83],color=purple,lw=3)
arrow((10.65,5.83),(11.1,5.83),purple)
box(11.12,5.34,1.45,1.00,'Detector /\nreadout')
ax.text(9.78,6.14,'Output guide',ha='center',color=purple,fontsize=10)
arrow((8.0,1.88),(8.0,2.55),grey)
ax.text(8.12,1.94,'External test signal\nfor spectroscopy',va='center',fontsize=10,color=grey)

# Transverse inset: alternating electrode pairs, purely schematic.
cx,cy=2.28,.63
for dx,dy,lab in ((0,.48,'+'),(.57,0,'−'),(0,-.48,'+'),(-.57,0,'−')):
    ax.add_patch(Circle((cx+dx,cy+dy),.17,facecolor='#e6edf2',edgecolor=grey))
    ax.text(cx+dx,cy+dy,lab,ha='center',va='center',color=grey)
for dx,dy in ((.27,0),(-.27,0),(0,.27),(0,-.27)):
    arrow((cx+dx,cy+dy),(cx+.22*dx,cy+.22*dy),blue)
ax.text(3.18,.86,'Selector end view: alternating electrode pairs',va='center',color=grey,fontsize=10)
ax.text(3.18,.42,'Upper branch seeks weaker field near the axis',va='center',color=blue,fontsize=10)
fig.text(.5,.035,'State selection sorts trajectories; it does not optically excite the transmitted molecules.',
         ha='center',fontsize=11,color='#162c40')
fig.savefig(Path(__file__).stem+'.png',dpi=110,facecolor='white',transparent=False)
