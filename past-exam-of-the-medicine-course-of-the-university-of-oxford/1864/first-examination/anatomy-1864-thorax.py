"""Original anatomical schematics; output PNG in the current directory.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).resolve().parents[3] / '_out' / 'matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch, Ellipse, Polygon, FancyBboxPatch
from matplotlib.path import Path as MPath
import numpy as np
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig=plt.figure(figsize=(12,8),facecolor='white')
a=fig.add_axes([.03,.10,.58,.80]); b=fig.add_axes([.65,.28,.33,.54])
def curve(ax,pts,**kw):
 codes=[MPath.MOVETO]+[MPath.CURVE4]*(len(pts)-1)
 patch=PathPatch(MPath(pts,codes),**kw);ax.add_patch(patch);return patch
# Body wall and ribs are deliberately schematic rather than a surface-level atlas.
curve(a,[(4.0,10.6),(2.4,10.4),(.8,7.8),(1.0,2.0),(1.5,.9),(8.5,.9),(9.0,2.0),(9.2,7.8),(7.7,10.4),(6.0,10.6)],fill=False,edgecolor='#a07c52',lw=3)
for y in np.linspace(4.2,9.2,6):
 curve(a,[(1.2,y-.6),(2.1,y+.1),(3.0,y+.2),(4.7,y-.1)],fill=False,edgecolor='#dcc5a3',lw=6,zorder=0)
 curve(a,[(5.3,y-.1),(7.0,y+.2),(7.9,y+.1),(8.8,y-.6)],fill=False,edgecolor='#dcc5a3',lw=6,zorder=0)
# Patient's right lung (viewer left), left lung with cardiac indentation.
curve(a,[(4.3,10.0),(3.3,10.6),(1.6,8.5),(1.6,4.0),(1.7,2.8),(3.2,3.1),(4.3,3.5),(4.3,5.6),(4.1,7.8),(4.3,10.0)],facecolor='#d6eaf3',edgecolor='#397b98',lw=2)
curve(a,[(5.7,10.0),(6.7,10.6),(8.4,8.5),(8.4,3.6),(8.2,2.5),(7.4,2.8),(6.9,3.1),(7.1,4.0),(6.0,5.3),(5.7,6.4),(5.7,7.6),(5.9,8.7),(5.7,10.0)],facecolor='#d6eaf3',edgecolor='#397b98',lw=2)
a.plot([5,5],[11.0,8.1],color='#657d83',lw=10,solid_capstyle='round')
a.plot([5,3.6],[8.1,7.1],color='#657d83',lw=7);a.plot([5,6.4],[8.1,7.1],color='#657d83',lw=7)
a.add_patch(Ellipse((5.6,4.8),2.6,3.4,angle=32,facecolor='#c96673',edgecolor='#8d3f4b',lw=2))
a.add_patch(Ellipse((5.6,4.8),2.95,3.7,angle=32,fill=False,edgecolor='#8d3f4b',lw=1,ls=':'))
a.plot([4.9,4.9],[10.2,6.0],color='#bd986d',lw=5,alpha=.7)
curve(a,[(1.0,1.8),(2.3,3.3),(3.3,3.7),(4.4,2.4),(5.2,1.8),(6.0,3.0),(7.0,2.6),(8.0,2.4),(8.5,2.0),(9.0,1.7)],fill=False,edgecolor='#63548b',lw=3)
# Pleural limits are below the lung margins, marking the basal recesses.
curve(a,[(1.3,3.1),(1.4,2.6),(1.6,2.1),(2.2,2.0)],fill=False,edgecolor='#397b98',lw=2,ls='--')
curve(a,[(8.6,3.0),(8.6,2.3),(8.4,1.9),(7.8,1.8)],fill=False,edgecolor='#397b98',lw=2,ls='--')
def lab(ax,text,xy,xytext,ha='left'):
 ax.annotate(text,xy,xytext=xytext,ha=ha,va='center',fontsize=10,arrowprops={'arrowstyle':'-','color':'#555','lw':1},bbox={'facecolor':'white','edgecolor':'none','pad':1})
lab(a,'Ribs + intercostal wall',(1.0,7.4),(.1,11.4))
lab(a,'Trachea and bronchi',(5,8.2),(6.4,11.1))
lab(a,'Sternum\n(surface projection)',(4.9,9.5),(6.7,9.9))
a.text(2.7,6.2,'Right lung',ha='center',color='#235b72');a.text(7.5,7.0,'Left lung',ha='center',color='#235b72')
lab(a,'Heart in pericardium',(5.6,4.9),(6.5,4.1))
lab(a,'Diaphragm',(3.0,3.2),(1.0,.5))
lab(a,'Basal pleural recess',(8.5,2.0),(6.0,.7))
a.annotate('',(1.8,2.2),(1.8,3.0),arrowprops={'arrowstyle':'->','lw':2,'color':'#397b98'})
a.text(4.8,-.3,'Inspiration: lung expands; diaphragm descends',ha='center',fontsize=10)
a.set(xlim=(0,10),ylim=(-.7,11.8));a.set_aspect('equal');a.axis('off')
a.set_title('Anterior projection',fontsize=14,pad=10)
# Transverse view, viewed from below: anterior is up, subject right is image left.
b.add_patch(Ellipse((5,5.4),9.4,6.7,facecolor='#fbf7f0',edgecolor='#a07c52',lw=3))
for x in (2.5,7.5):b.add_patch(Ellipse((x,5.4),3.0,4.7,facecolor='#d6eaf3',edgecolor='#397b98',lw=2))
b.add_patch(Ellipse((5.2,6.0),3.0,3.4,angle=20,facecolor='#c96673',edgecolor='#8d3f4b',lw=2))
b.add_patch(Ellipse((5,8.7),1.4,.35,facecolor='#bd986d',edgecolor='#a07c52'))
b.add_patch(Ellipse((5,2.2),1.5,1.0,facecolor='#dcc5a3',edgecolor='#a07c52'))
b.add_patch(Ellipse((5.1,3.6),.65,.55,facecolor='#dcb991',edgecolor='#886d4b'))
b.add_patch(Ellipse((6.1,3.3),.7,.7,facecolor='#c96673',edgecolor='#8d3f4b'))
b.text(5,10.0,'Anterior: sternum',ha='center',fontsize=10)
b.text(5,.5,'Posterior: vertebra',ha='center',fontsize=10)
lab(b,'Oesophagus',(5.1,3.6),(.0,1.2))
lab(b,'Aorta',(6.1,3.3),(7.6,1.6))
b.text(5.2,6,'Heart',ha='center',fontsize=10,color='white')
b.text(1.0,9.2,'R',fontweight='bold');b.text(9,9.2,'L',fontweight='bold')
b.set(xlim=(-.5,10.5),ylim=(0,10.5));b.set_aspect('equal');b.axis('off');b.set_title('Transverse relationships',fontsize=13,pad=15)
fig.suptitle('Thoracic walls and viscera',fontsize=19,y=.97)
fig.text(.67,.13,'Schematic; not to scale.\nRespiratory phase and posture\nchange the projected boundaries.',fontsize=11,ha='left')
fig.savefig('anatomy-1864-thorax.png',dpi=150,facecolor='white',metadata={'Software':'codex-wiki anatomical generator'})
