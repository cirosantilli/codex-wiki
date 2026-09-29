"""Original formal valence-MO diagram for C2; NST IA Chemistry 2024 Q2."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(8.5,5.5),facecolor='white');ax.set(xlim=(-.4,11.4),ylim=(-4.9,4.5));ax.axis('off')
def level(x,y,label='',occ=0,width=.7):
    ax.plot([x-width/2,x+width/2],[y,y],color='black',lw=1.4)
    if label:ax.text(x+.55,y,label,va='center',fontsize=11)
    if occ:ax.text(x,y+.08,'↑↓' if occ==2 else '↑',ha='center',va='bottom',fontsize=15)
for x in [1.0,10.0]:
    level(x,-2.8,occ=2)
    for off,oc in zip([-.65,0,.65],[1,1,0]):level(x+off,1.0,occ=oc,width=.43)
    ax.text(x,3.9,'C atom',ha='center',fontsize=12,weight='bold')
    ax.text(x,-3.35,'2s²',ha='center',fontsize=11);ax.text(x,1.8,'2p²',ha='center',fontsize=11)
for y,label,occ in [(-4,r'$\sigma_g(2s)$',2),(-2,r'$\sigma_u^*(2s)$',2),(1.2,r'$\sigma_g(2p)$',0),(3.3,r'$\sigma_u^*(2p)$',0)]:level(5,y,label,occ)
for y,label,occ in [(0,r'$\pi_u(2p)$',2),(2.4,r'$\pi_g^*(2p)$',0)]:
    level(4.55,y,occ=occ,width=.6);level(5.45,y,occ=occ,width=.6);ax.text(6.1,y,label,va='center',fontsize=11)
for x in [1.4,9.6]:
    for ya,yb in [(-2.8,-4),(-2.8,-2),(1,0),(1,1.2),(1,2.4),(1,3.3)]:ax.plot([x,4.1 if x<5 else 5.9],[ya,yb],color='#aaaaaa',ls=':',lw=.7,zorder=0)
ax.annotate('',(-.15,3.6),(-.15,-4.2),arrowprops={'arrowstyle':'->'});ax.text(-.3,-.4,'Energy',rotation=90,va='center')
ax.text(5,3.9,'C₂ valence orbitals',ha='center',fontsize=12,weight='bold')
ax.text(5.5,-4.7,'Eight valence electrons; formal bond order 2. Relative levels are schematic.',ha='center',fontsize=10)
fig.tight_layout();fig.savefig('paper-1-carbon-orbitals.png',dpi=140,facecolor='white',bbox_inches='tight');plt.close(fig)
