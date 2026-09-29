"""Original functional signal comparison; Python 3.14 and Matplotlib. PNG to cwd."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch

def box(ax,x,y,w,h,label,color='#e7f0f6'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.015',facecolor=color,edgecolor='#456078',lw=1.2))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=11)

def arrow(ax,a,b,label=''):
    ax.annotate('',b,a,arrowprops={'arrowstyle':'->','lw':1.5,'color':'#85542e'})
    if label:ax.text((a[0]+b[0])/2+.03,(a[1]+b[1])/2,label,fontsize=10,va='center')

def main():
    fig,axs=plt.subplots(1,3,figsize=(11.5,4.5))
    for ax in axs:ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax=axs[0];ax.set_title('NaI(Tl) scintillation',fontsize=13)
    box(ax,.25,.74,.5,.13,'Energy deposit');box(ax,.25,.43,.5,.13,'Scintillation light');box(ax,.25,.12,.5,.13,'Light readout')
    arrow(ax,(.5,.73),(.5,.58));arrow(ax,(.5,.42),(.5,.27))
    ax.text(.5,.02,'Time dependence is an added observable',ha='center',fontsize=9)
    ax=axs[1];ax.set_title('Cryogenic Ge / Si',fontsize=13)
    box(ax,.25,.74,.5,.13,'Energy deposit');box(ax,.03,.4,.4,.17,'Phonons');box(ax,.57,.4,.4,.17,'Ionization')
    arrow(ax,(.4,.73),(.23,.59));arrow(ax,(.6,.73),(.77,.59))
    box(ax,.15,.12,.7,.13,'Compare charge and energy')
    arrow(ax,(.23,.39),(.34,.27));arrow(ax,(.77,.39),(.66,.27))
    ax.text(.5,.02,'Recoil yield and timing reject backgrounds',ha='center',fontsize=9)
    ax=axs[2];ax.set_title('Dual-phase xenon',fontsize=13)
    ax.add_patch(Rectangle((.1,.2),.8,.62,facecolor='#def0fa',edgecolor='#456078'))
    ax.add_patch(Rectangle((.1,.64),.8,.18,facecolor='#f5f0e4',edgecolor='#456078'))
    ax.text(.15,.74,'Gas: S2 light',fontsize=11);ax.text(.15,.24,'Liquid xenon',fontsize=11)
    ax.plot(.5,.4,'o',color='#b96e23');ax.text(.55,.38,'Recoil',fontsize=10)
    arrow(ax,(.5,.43),(.5,.68),r'$e^-$ drift')
    arrow(ax,(.54,.39),(.78,.21),'S1')
    ax.text(.5,.11,'S1–S2 delay gives depth',ha='center',fontsize=10)
    ax.text(.5,.02,'Light pattern gives position; S2/S1 gives yield',ha='center',fontsize=9)
    fig.text(.5,.98,'Complementary channels measure the same deposited recoil energy',ha='center',va='top',fontsize=13)
    fig.tight_layout(rect=(0,0,1,.95));fig.savefig('paper-1-recoil-signals.png',dpi=160,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
