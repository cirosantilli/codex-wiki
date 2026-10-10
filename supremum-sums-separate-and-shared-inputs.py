"""Original deterministic example for supremum of sums; render PNG to current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12})
    fig,axs=plt.subplots(1,2,figsize=(12,6.2),layout='constrained',facecolor='white')
    a=np.linspace(0,1,301);aa,bb=np.meshgrid(a,a)
    norm=matplotlib.colors.Normalize(0,2);cmap=plt.colormaps['viridis']
    im=axs[0].pcolormesh(aa,bb,aa+bb,cmap=cmap,norm=norm,shading='auto',rasterized=True)
    cs=axs[0].contour(aa,bb,aa+bb,levels=[.5,1,1.5],colors='white',alpha=.8,linewidths=1)
    axs[0].clabel(cs,fmt='%g',fontsize=10)
    axs[0].scatter([1],[1],s=110,c='#de562b',edgecolor='white',zorder=5,clip_on=False)
    axs[0].annotate('Sum 2 is attainable',xy=(1,1),xytext=(.1,.92),color='white',fontsize=13,arrowprops={'arrowstyle':'->','color':'white'})
    axs[0].set_title('Separate inputs: all output pairs are allowed')
    axs[1].set_facecolor('#f2f3f4')
    axs[1].plot(a,1-a,lw=5,c=cmap(norm(1)),label=r'Shared input: $a+b=1$')
    axs[1].scatter([0,1],[1,0],s=70,c=[cmap(norm(1))],zorder=5,clip_on=False)
    axs[1].scatter([1],[1],s=130,marker='x',c='#b64335',zorder=5,clip_on=False)
    axs[1].annotate('The pair (1,1) is forbidden',xy=(1,1),xytext=(.12,.96),color='#a83e32',fontsize=12,arrowprops={'arrowstyle':'->','color':'#a83e32'})
    axs[1].text(.38,.16,r'$\sup_x[f(x)+g(x)]=1$',ha='center',fontsize=14)
    axs[1].set_title('Shared input: only the diagonal is allowed')
    for ax in axs:
        ax.set(xlim=(0,1),ylim=(0,1),xlabel=r'$a$: value of $f$',ylabel=r'$b$: value of $g$')
        ax.set_aspect('equal')
        ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
    cb=fig.colorbar(im,ax=axs,orientation='horizontal',shrink=.75,pad=.1,aspect=35)
    cb.set_label(r'Combined value $a+b$');cb.set_ticks([0,.5,1,1.5,2])
    fig.suptitle(r'Suprema and compatible choices: $f(x)=x$, $g(x)=1-x$, $0\leq x\leq1$',fontsize=17)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white');plt.close(fig)


if __name__=='__main__':main()
