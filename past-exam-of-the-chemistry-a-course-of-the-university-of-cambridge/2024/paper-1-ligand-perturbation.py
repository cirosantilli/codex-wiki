"""Original qualitative metal-only correlation diagram for eclipsed [Mo2Cl8]4-."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(12.0,7.8),facecolor='white')
ax.set(xlim=(-.2,12.6),ylim=(-4.1,6.4));ax.axis('off')
ax.annotate('',xy=(.15,5.7),xytext=(.15,-3.45),arrowprops={'arrowstyle':'->','lw':1.4})
ax.text(-.1,1.1,'Energy (schematic)',rotation=90,ha='center',va='center',fontsize=11)
# Bare energy, final energy, offset within column, label, occupied after mixing.
levels=[(-3,-2.65,0,r'$a_{1g}\ (\sigma)$',True),
        (-1.8,-1.65,-.65,r'$e_u\ (\pi)$',True),
        (-1.8,-1.65,.65,None,True),
        (-.6,-.6,-.65,r'$b_{2g}\ (\delta)$',True),
        (-.6,4.5,.65,r'$b_{1g}$',False),
        (.6,.6,-.65,r'$b_{1u}\ (\delta^*)$',False),
        (.6,5.25,.65,r'$b_{2u}$',False),
        (1.8,2.05,-.65,r'$e_g\ (\pi^*)$',False),
        (1.8,2.05,.65,None,False),
        (3,3.5,0,r'$a_{2u}\ (\sigma^*)$',False)]
left,right=3.4,8.4
for before,after,offset,label,occupied in levels:
    x1,x2=left+offset,right+offset
    unchanged=abs(before-after)<1e-9
    strong=after-before>4
    color='#a34f26' if strong else '#245f8a'
    ax.plot([x1+.42,x2-.42],[before,after],color=color,ls='--' if unchanged else ':',lw=1.2,alpha=.75,zorder=1)
    ax.plot([x1-.43,x1+.43],[before,before],color='black',lw=1.8,zorder=2)
    ax.plot([x2-.43,x2+.43],[after,after],color=color,lw=2,zorder=2)
    if occupied:
        for xpos,direction in [(x2-.12,1),(x2+.12,-1)]:
            bottom,top=after+.10,after+.55
            start,end=((bottom,top) if direction==1 else (top,bottom))
            ax.annotate('',xy=(xpos,end),xytext=(xpos,start),arrowprops={'arrowstyle':'->','lw':1.2,'color':'black'})
    if label:
        ax.text(9.7,after,label,ha='left',va='center',fontsize=13)
for y,label in [(-3,r'$a_{1g}$'),(-1.8,r'$e_u$'),(-.6,r'$b_{2g},b_{1g}$'),(.6,r'$b_{1u},b_{2u}$'),(1.8,r'$e_g$'),(3,r'$a_{2u}$')]:
    ax.text(2.0,y,label,ha='right',va='center',fontsize=12)
ax.text(left,5.9,'Metal pair',ha='center',fontsize=13,weight='bold')
ax.text(right,5.9,'With lower-energy ligand σ donors',ha='center',fontsize=13,weight='bold')
ax.text(10.7,4.95,'Strong metal–ligand\nantibonding character',ha='center',va='center',fontsize=10,color='#a34f26')
ax.text(6.4,-3.65,'Eight d electrons fill σ²π⁴δ². Lower ligand-dominated bonding partners are not shown.',ha='center',fontsize=11)
ax.text(6.4,-3.98,'Relative spacings are illustrative; π shifts can vanish in the local nearest-neighbour σ-only limit.',ha='center',fontsize=10)
fig.tight_layout()
fig.savefig('paper-1-ligand-perturbation.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
