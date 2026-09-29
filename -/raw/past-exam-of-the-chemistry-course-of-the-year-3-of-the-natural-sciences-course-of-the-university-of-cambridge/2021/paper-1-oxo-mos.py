"""Original qualitative MO occupancy diagram; outputs basename to cwd."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def draw():
    fig,ax=plt.subplots(figsize=(9.7,5.8),layout='constrained')
    ax.set(xlim=(0,10),ylim=(-.7,5.3));ax.axis('off')
    ax.annotate('',(.35,5),(.35,0),arrowprops={'arrowstyle':'->','lw':1.3})
    ax.text(.1,2.7,'Energy',rotation=90,ha='center')
    def level(x,y,label,filled=True,w=.55):
        ax.plot([x-w/2,x+w/2],[y,y],color='#273c52',lw=2)
        if filled:
            ax.text(x,y+.04,'↑↓',ha='center',va='bottom',fontsize=14)
        if label:ax.text(x,y-.15,label,ha='center',va='top',fontsize=11)
    level(1.7,1.7,r'O $p_y$ (2e)')
    for i in range(3):level(8+i*.6,2.7,None)
    ax.text(8.6,3.30,r'Ru $t_{2g}$ set: 9 orbitals, 16e',ha='center',fontsize=11)
    # Peripheral occupation is a total, not an assignment to individual localized Ru orbitals.
    for l in ax.texts[-4:-1]:
        if l.get_text()=='↑↓':l.set_visible(False)
    level(4.8,.45,'π bonding')
    level(4.8,4.5,'π* antibonding',False)
    for i in range(8):level(3.25+i*.44,2.75,None,w=.34)
    ax.text(4.8,2.28,'8 nonbonding orbitals (16e)',ha='center',fontsize=11)
    ax.text(4.8,1.82,r'$2(d_{yz}\ {\rm SALCs})+3d_{xy}+3d_{xz}$',ha='center',fontsize=11)
    ax.text(4.8,-.35,'Neutral formula: 16 Ru d electrons + 2 O π electrons = 18e',ha='center',fontsize=12,weight='bold')
    for x,y in [(1.7,1.7),(8.6,2.7)]:
        for yy in [.45,4.5]:ax.plot([x,4.8],[y,yy],color='#aaa',ls='--',lw=.8,zorder=0)
    ax.text(4.8,5.07,'One O orbital couples to one of three Ru dᵧz combinations',ha='center',fontsize=12)
    fig.savefig('paper-1-oxo-mos.png',dpi=155,facecolor='white');plt.close(fig)

if __name__=='__main__':draw()
