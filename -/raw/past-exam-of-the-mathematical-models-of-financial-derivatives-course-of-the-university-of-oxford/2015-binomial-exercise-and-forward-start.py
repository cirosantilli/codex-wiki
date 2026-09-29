"""Original two-step valuation trees; save the matching PNG in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig,axes=plt.subplots(1,2,figsize=(11.4,5.0),layout='constrained')
    coordinates=[(0,0),(1,1.1),(1,-1.1),(2,1.7),(2,.55),(2,-.55),(2,-1.7)]
    edges=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
    prices=[9,12,6,16,8,8,4]
    values=[['1.08','0.30','3','0','1','1','5'],['1.80','2.40','1.20','4','0','2','0']]
    for panel,(ax,label) in enumerate(zip(axes,['P','C'])):
        for a,b in edges:
            ax.plot([coordinates[a][0],coordinates[b][0]],[coordinates[a][1],coordinates[b][1]],color='#aaaaaa',lw=1.3,zorder=1)
        for i,((x,y),price,value) in enumerate(zip(coordinates,prices,values[panel])):
            color='#b13a25' if panel==0 and i==2 else ('#bd691c' if panel==1 and i in [4,5] else '#145885')
            second='Payoff' if panel==1 and i>=3 else label
            ax.text(x,y,f'$S={price}$\n{second} = {value}',ha='center',va='center',fontsize=10.5,
                    bbox=dict(boxstyle='round,pad=.38',facecolor='white',edgecolor=color,lw=1.5),zorder=3)
        ax.set(xlim=(-.35,2.55),ylim=(-2.15,2.25));ax.axis('off')
        for x,title in [(0,'Now'),(1,'After one step'),(2,'Expiry')]:ax.text(x,2.15,title,ha='center',fontsize=10,color='#555555')
    axes[0].set_title('American put: exercise at the red node',fontsize=12,pad=12)
    axes[1].set_title('Forward-start call: retain the path history',fontsize=12,pad=12)
    axes[0].text(1,-1.63,'Exercise pays 3;\ncontinuation pays 2.10.',ha='center',fontsize=9.5,color='#b13a25')
    axes[1].text(.7,-2.02,'The two orange nodes share price 8,\nbut their fixed strikes differ.',ha='center',fontsize=9.5,color='#9a5418')
    fig.suptitle('Risk-neutral up probability 2/3; one-step discount factor 9/10',fontsize=12)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
