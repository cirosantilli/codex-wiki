"""Original schematic of ten d orbitals of an isolated metal pair, with D4h labels."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(8.2,6.2),facecolor='white')
ax.set(xlim=(0,10),ylim=(-4,4));ax.axis('off')
ax.annotate('',xy=(.7,3.6),xytext=(.7,-3.6),arrowprops={'arrowstyle':'->','lw':1.5})
ax.text(.3,0,'Energy (schematic)',rotation=90,ha='center',va='center',fontsize=11)
levels=[(-3,[4.7],r'$a_{1g}$',r'$\sigma\ (d_{z^2})$'),
        (-1.8,[4.0,5.4],r'$e_u$',r'$\pi\ (d_{xz},d_{yz})$'),
        (-.6,[4.0,5.4],r'$b_{2g},\ b_{1g}$',r'$\delta\ (d_{xy},d_{x^2-y^2})$'),
        (.6,[4.0,5.4],r'$b_{1u},\ b_{2u}$',r'$\delta^*$'),
        (1.8,[4.0,5.4],r'$e_g$',r'$\pi^*$'),
        (3,[4.7],r'$a_{2u}$',r'$\sigma^*$')]
for energy,centers,irrep,kind in levels:
    for x in centers:ax.plot([x-.48,x+.48],[energy,energy],lw=2,color='#245f8a')
    ax.text(2.8,energy,irrep,ha='right',va='center',fontsize=13)
    ax.text(6.2,energy,kind,ha='left',va='center',fontsize=12)
ax.axhline(0,xmin=.27,xmax=.63,color='gray',ls=':',lw=1)
ax.text(4.7,3.65,'Metal 4d combinations before ligand mixing',ha='center',fontsize=13,weight='bold')
ax.text(4.8,-3.75,'Ten orbitals; no electron filling assumed here.\nThe two δ families are degenerate for an isolated cylindrical metal pair.',ha='center',va='center',fontsize=10)
fig.tight_layout()
fig.savefig('paper-1-metal-orbitals.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
