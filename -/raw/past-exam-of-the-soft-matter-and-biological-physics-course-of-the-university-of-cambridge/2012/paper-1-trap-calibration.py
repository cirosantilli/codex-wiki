"""Original functional trap/readout diagram and normalized calibration curves."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def main():
 plt.rcParams.update({'font.size':10})
 fig=plt.figure(figsize=(8.5,5.5),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[.8,1.2]);top=fig.add_subplot(gs[0,:]);ax=fig.add_subplot(gs[1,0]);bx=fig.add_subplot(gs[1,1])
 top.set(xlim=(0,10),ylim=(0,2));top.axis('off')
 labels=['Laser and\nbeam steering','High-NA\nobjective','Trapped bead\nin liquid','Condenser and\nposition detector']
 for x,label in zip([.1,2.6,5.1,7.6],labels):
  top.add_patch(FancyBboxPatch((x,.75),2.05,.8,boxstyle='round,pad=.04',facecolor='#e4edf3',edgecolor='#487391'));top.text(x+1.025,1.15,label,ha='center',va='center',fontsize=9)
 for x in [2.2,4.7,7.2]:top.annotate('',(x+.35,1.15),(x,1.15),arrowprops={'arrowstyle':'->','lw':1.4,'color':'#a34949'})
 top.annotate('Calibrated stage motion',(6.1,.72),(6.1,.2),arrowprops={'arrowstyle':'->'},ha='center',fontsize=9)
 top.set_title('Functional apparatus; synthetic handle calibration',fontsize=11)
 q=np.linspace(-2,2,300);ax.plot(q,q,c='#337aa6',label=r'$F_{ext}/\sqrt{kk_BT}=x/\sigma_x$');ax.set(xlabel=r'$x/\sigma_x$',ylabel='Normalized inferred force',title='Local static force readout');ax.axhline(0,c='.6',lw=.6);ax.axvline(0,c='.6',lw=.6)
 f=np.logspace(-2,2,500);bx.loglog(f,1/(1+f*f),c='#337aa6',lw=2);bx.scatter([1],[.5],c='black',s=25);bx.axvline(1,c='.6',ls=':',lw=1);bx.text(1.25,.55,'Corner',fontsize=9)
 bx.set(xlabel=r'$f/f_c$',ylabel=r'$S_x(f)/S_x(0)$',title='Thermal spectrum and relaxation')
 for p in [ax,bx]:p.grid(alpha=.18);p.spines[['top','right']].set_visible(False)
 fig.savefig('paper-1-trap-calibration.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
