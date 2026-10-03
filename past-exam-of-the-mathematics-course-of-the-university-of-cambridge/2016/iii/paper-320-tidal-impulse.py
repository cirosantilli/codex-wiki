"""Original tidal-encounter geometry. Python 3.14; matplotlib 3.10.7.

Run in the output cwd. Main Make renders the final PNG in mirrored _media.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def main():
 fig,axes=plt.subplots(1,2,figsize=(10,4.4),dpi=100,facecolor='white')
 ax=axes[0];ax.set_facecolor('white');ax.add_patch(Circle((0,0),.63,facecolor='#e8eef5',edgecolor='#235d99',lw=1.8));ax.scatter([0],[0],s=25,color='#235d99');ax.text(-.40,-.25,'Galaxy centre',fontsize=10)
 ax.plot([2,2],[-1.5,1.5],color='#b23838',lw=1.7);ax.annotate('',xy=(2,1.4),xytext=(2,.95),arrowprops=dict(arrowstyle='-|>',color='#b23838',lw=2));ax.text(2.13,1.12,r'$v\hat z$',color='#b23838',fontsize=13)
 ax.scatter([2],[.72],s=60,color='#b23838');ax.text(2.12,.67,r'$m_p$',fontsize=13,color='#b23838');ax.annotate('',xy=(2,.72),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#666666',lw=1.3));ax.text(.86,.46,r'$\mathbf{r}_p$',fontsize=13)
 ax.annotate('',xy=(2,0),xytext=(0,0),arrowprops=dict(arrowstyle='<->',lw=1.2,color='black'));ax.text(.93,-.20,r'$p$',fontsize=13)
 ax.set(xlim=(-.9,2.7),ylim=(-1.65,1.65),xlabel='x',ylabel='z',aspect='equal',title='Encounter in the x–z plane');ax.axhline(0,color='#aaaaaa',lw=.6,zorder=0);ax.axvline(0,color='#aaaaaa',lw=.6,zorder=0)
 ax=axes[1];ax.set_facecolor('white');ax.add_patch(Circle((0,0),1,facecolor='#f5f7fa',edgecolor='#235d99',lw=1.5))
 pts=[(x/4,y/4) for x in range(-3,4) for y in range(-3,4) if 0<x*x+y*y<=12]
 for x,y in pts:ax.arrow(x,y,.22*x,-.22*y,width=.008,head_width=.055,head_length=.045,length_includes_head=True,color='#277a66',alpha=.85)
 ax.scatter([0],[0],s=20,color='black');ax.text(-1.02,1.10,r'$\Delta\mathbf{v}\propto(x,-y,0)$',fontsize=13,color='#277a66')
 ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),xlabel='x',ylabel='y',aspect='equal',title='Integrated kicks in the x–y plane');ax.axhline(0,color='#aaaaaa',lw=.6,zorder=0);ax.axvline(0,color='#aaaaaa',lw=.6,zorder=0)
 for ax in axes:ax.tick_params(labelsize=9)
 fig.subplots_adjust(left=.07,right=.97,bottom=.13,top=.86,wspace=.30)
 fig.savefig('paper-320-tidal-impulse.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
