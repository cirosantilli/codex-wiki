from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def main():
    fig,ax=plt.subplots(figsize=(8.2,5),dpi=100,facecolor='white');ax.set_facecolor('white')
    for vertices in [[(0,0),(1,1),(2,0),(1,-1)],[(0,0),(-1,1),(-2,0),(-1,-1)],[(0,0),(1,1),(0,2),(-1,1)],[(0,0),(1,-1),(0,-2),(-1,-1)]]:ax.add_patch(Polygon(vertices,closed=True,facecolor='#e0eff7',edgecolor='none'))
    for sg in [-1,1]:
        ax.plot([0,sg,2*sg,sg,0],[0,1,0,-1,0],color='#4d4d4d',lw=1.3)
        ax.plot([sg,0,-sg],[1,2,1],color='#bf3b33',ls='--',lw=2)
        ax.plot([sg,0,-sg],[-1,-2,-1],color='#bf3b33',ls='--',lw=2)
        ax.add_patch(Polygon([(0,2),(sg,1),(2*sg,2),(sg,3)],closed=True,facecolor='#f8e8cf',edgecolor='#c89c60',linestyle=':',linewidth=1))
    ax.plot([-2,2],[0,0],color='#17699b',lw=2.5);ax.text(1.35,.12,r'$\Sigma$',color='#17699b',fontsize=13)
    ax.text(0,.78,'future interior\nr− < r < r+',ha='center',fontsize=11);ax.text(0,-.78,'past interior',ha='center',fontsize=11)
    ax.text(1.12,-.38,'right exterior',ha='center',fontsize=10);ax.text(-1.12,-.38,'left exterior',ha='center',fontsize=10)
    ax.text(.75,1.66,'inner Cauchy\nhorizon r−',ha='center',color='#bf3b33',fontsize=10);ax.text(-.75,1.66,'inner Cauchy\nhorizon r−',ha='center',color='#bf3b33',fontsize=10)
    ax.text(1,2.2,'extension\npatch',ha='center',fontsize=11);ax.text(-1,2.2,'extension\npatch',ha='center',fontsize=11)
    ax.text(.7,.35,'r+',fontsize=10);ax.text(-.7,.35,'r+',fontsize=10)
    ax.text(0,-2.35,'Blue: maximal Cauchy development of the complete bridge\nOrange: neighboring smooth extensions (partial diagram)',ha='center',fontsize=11)
    ax.set(xlim=(-2.45,2.45),ylim=(-2.6,3.2));ax.set_aspect('equal');ax.axis('off');ax.set_title('A complete initial slice need not have an inextendible development',fontsize=12)
    fig.tight_layout();fig.savefig(Path.cwd()/'paper-311-cauchy-development.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
