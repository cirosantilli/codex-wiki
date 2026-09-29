"""Original valence-only O2 MO diagram; Python 3.14 and matplotlib.

Energies are qualitative. The PNG is written to the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(10.2,6.4),layout='constrained')
fig.patch.set_facecolor('white')
ax.set(xlim=(-.2,12.2),ylim=(-6.5,4.7))
ax.axis('off')
ax.annotate('',xy=(.05,3.4),xytext=(.05,-6),arrowprops={'arrowstyle':'->','lw':1.3})
ax.text(-.1,-1.3,'Energy',rotation=90,ha='right',fontsize=11)

def level(x1,x2,y,occ='',label=None):
    ax.plot([x1,x2],[y,y],color='#2c465c',lw=1.6)
    ax.text((x1+x2)/2,y+.10,occ,ha='center',va='bottom',fontsize=15)
    if label:ax.text((x1+x2)/2,y-.27,label,ha='center',va='top',fontsize=10.5,
        bbox={'fc':'white','ec':'none','pad':.7})

for shift in [0,9.2]:
    level(.9+shift,2.0+shift,-4.3,'↑↓',r'$2s$')
    for i,(lab,occ) in enumerate([(r'$2p_x$','↑↓'),(r'$2p_y$','↑'),(r'$2p_z$','↑')]):
        level(.55+shift+.83*i,1.12+shift+.83*i,.6,occ,lab)
    ax.text(1.6+shift,4.1,'O: valence 2s²2p⁴',ha='center',fontsize=12)
levels=[(-5.6,'↑↓',r'$\sigma_g(2s)$'),(-3.4,'↑↓',r'$\sigma_u^*(2s)$'),
        (-1.6,'↑↓',r'$\sigma_g(2p_z)$'),(3.0,'',r'$\sigma_u^*(2p_z)$')]
for y,occ,lab in levels:level(4.85,7.15,y,occ,lab)
for y,occs,lab in [(-.1,['↑↓','↑↓'],r'$\pi_u(2p_x),\ \pi_u(2p_y)$'),
                   (1.45,['↑','↑'],r'$\pi_g^*(2p_x),\ \pi_g^*(2p_y)$')]:
    level(4.45,5.45,y,occs[0])
    level(6.55,7.55,y,occs[1])
    ax.text(6,y-.27,lab,ha='center',va='top',fontsize=10.5)
for xa,xb in [(2.1,4.7),(9.8,7.3)]:
    for a,b in [(-4.3,-5.6),(-4.3,-3.4),(.6,-1.6),(.6,3.0)]:
        ax.plot([xa,xb],[a,b],ls=':',color='#b0b5bb',lw=.8,zorder=0)
ax.text(6,4.1,'O₂: 12 valence electrons',ha='center',fontsize=13,weight='bold')
ax.text(6,-6.35,'1s core orbitals omitted; level spacings are not to scale',ha='center',fontsize=10,color='#555f68')
fig.savefig('paper-1-additional-oxygen-mo.png',dpi=160,facecolor='white')
plt.close(fig)
