"""Original residue-lifting tree modulo successive powers of two."""
from pathlib import Path
import matplotlib.pyplot as plt


def levels(depth):
    rows=[[0]]
    for n in range(depth):
        rows.append([child for r in rows[-1] for child in (r,r+2**n)])
    return rows


def main():
    rows=levels(4);assert all(set(row)==set(range(2**n)) for n,row in enumerate(rows))
    fig,ax=plt.subplots(figsize=(12.6,6.4),dpi=100,facecolor='white')
    fig.suptitle('One 2-adic integer follows a compatible path through finite residues',fontsize=17,y=.97)
    coordinates={}
    for n,row in enumerate(rows):
        for j,r in enumerate(row):coordinates[n,j]=((j+.5)/len(row),4-n)
    for n in range(4):
        for j,r in enumerate(rows[n]):
            for c in (2*j,2*j+1):
                x,y=coordinates[n,j];xx,yy=coordinates[n+1,c]
                chosen=(r==13%(2**n) and rows[n+1][c]==13%(2**(n+1)))
                ax.plot([x,xx],[y,yy],color='#cb7926' if chosen else '#bdcbd5',lw=2.8 if chosen else 1.05,zorder=1)
    for n,row in enumerate(rows):
        for j,r in enumerate(row):
            x,y=coordinates[n,j];chosen=r==13%(2**n)
            ax.text(x,y,str(r),ha='center',va='center',fontsize=12 if n<4 else 11,bbox={'boxstyle':'circle,pad=.35','fc':'#f5d5b5' if chosen else '#f5f8fa','ec':'#a36625' if chosen else '#738b9b','lw':1.4 if chosen else 1},zorder=3)
        ax.text(-.055,4-n,f'mod {2**n}',ha='right',va='center',fontsize=12)
    ax.text(.5,-.65,'Highlighted residues: 0 mod 1 → 1 mod 2 → 1 mod 4 → 5 mod 8 → 13 mod 16',ha='center',fontsize=12)
    ax.text(.5,-1.0,'Each level adds one binary digit; reduction to the previous modulus follows the upward edge.',ha='center',fontsize=11)
    ax.set(xlim=(-.1,1.03),ylim=(-1.18,4.55));ax.axis('off')
    fig.subplots_adjust(left=.075,right=.99,bottom=.08,top=.86)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)


if __name__=='__main__':main()
