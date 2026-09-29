"""Original phase-estimation circuit. Run with Python 3.14 / matplotlib 3.10.7.
Writes an opaque white same-basename PNG to the current working directory.
Rename beside the published paper to paper-324-phase-estimation.py.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def box(ax,x,y,w,h,label,size=16):
 ax.add_patch(Rectangle((x-w/2,y-h/2),w,h,facecolor='white',edgecolor='#263746',linewidth=1.6,zorder=3))
 ax.text(x,y,label,ha='center',va='center',fontsize=size,zorder=4,color='#142736')

def main():
 fig=plt.figure(figsize=(11.8,5.6),dpi=100,facecolor='white');ax=fig.add_axes((.02,.12,.96,.77));ax.set_xlim(0,11.6);ax.set_ylim(-.05,5.35);ax.axis('off')
 rows=[4.65,3.55,1.85];target=.65
 for y in rows:ax.plot([1.65,10.8],[y,y],color='#263746',lw=1.4,zorder=1)
 ax.plot([1.65,10.8],[target,target],color='#263746',lw=1.4,zorder=1)
 for y,label in zip(rows,[r'$q_0:\ |0\rangle$',r'$q_1:\ |0\rangle$',r'$q_{n-1}:\ |0\rangle$']):
  ax.text(1.5,y,label,ha='right',va='center',fontsize=16);box(ax,2.1,y,.5,.55,r'$H$')
 ax.text(1.5,target,r'$|\psi\rangle$',ha='right',va='center',fontsize=18)
 ax.text(2.1,2.7,r'$\vdots$',ha='center',va='center',fontsize=24)
 ax.text(5.4,2.7,r'$\cdots$',ha='center',va='center',fontsize=23)
 for x,y,label,w in [(3.3,rows[0],r'$U$',.8),(4.5,rows[1],r'$U^2$',.9),(6.3,rows[2],r'$U^{2^{n-1}}$',1.35)]:
  ax.plot([x,x],[target,y],color='#263746',lw=1.4,zorder=2);ax.plot(x,y,'o',color='#263746',markersize=6,zorder=4);box(ax,x,target,w,.58,label)
 box(ax,8.25,3.25,1.35,3.48,r'$F_{2^n}^{-1}$',22)
 for y in rows:box(ax,10.1,y,.65,.56,'M',16)
 ax.text(11.4,3.3,r'$|c\rangle$',ha='right',va='center',fontsize=20)
 ax.text(11.4,target,r'$|\psi\rangle$',ha='right',va='center',fontsize=18)
 fig.text(.5,.955,'Exact phase estimation on a dyadic eigenphase',ha='center',va='center',fontsize=18,color='#142736')
 fig.text(.5,.05,r'$x=\sum_{j=0}^{n-1}2^jx_j$;  $q_0$ is the least significant bit.  M = computational-basis measurement.',ha='center',va='center',fontsize=12,color='#263746')
 out=Path.cwd()/(Path(__file__).stem+'.png');fig.savefig(out,dpi=100,facecolor='white',transparent=False);plt.close(fig);print(out)
if __name__=='__main__':main()
