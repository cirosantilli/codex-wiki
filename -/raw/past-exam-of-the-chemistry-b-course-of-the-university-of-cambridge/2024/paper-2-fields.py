"""Qualitative d-level correlations, arbitrary vertical energies; output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(12,4.6),facecolor='white')
levels=[[(1,['xy','xz','yz']),(3.7,['z²','x²−y²'])],[(.65,['xz','yz']),(1.65,['xy']),(2.8,['z²']),(4.2,['x²−y²'])],[(.4,['xz','yz']),(1.7,['xy']),(2.7,['z²']),(4.4,['x²−y²'])]]
titles=['Octahedral reference','Axially elongated: high-spin d⁴','Square pyramidal: usual order']
for i,(a,ls,t) in enumerate(zip(axs,levels,titles)):
 a.set(xlim=(0,4),ylim=(-.2,5));a.axis('off');a.set_title(t,weight='bold',fontsize=11)
 a.annotate('',(.18,4.8),(.18,.1),arrowprops=dict(arrowstyle='->'));a.text(.03,2.6,'Energy',rotation=90,va='center',fontsize=10)
 for y,names in ls:
  xs={1:[2],2:[1.4,2.7],3:[1,2,3]}[len(names)]
  for x,n in zip(xs,names):
   a.plot([x-.37,x+.37],[y,y],color='#2268a0',lw=2);a.text(x,y-.28,'d'+n,ha='center',va='top',fontsize=11)
   if i==1:a.text(x,y+.05,'↑',ha='center',fontsize=17) if n!='x²−y²' else None
fig.text(.5,.03,'Axial elongation lowers z-containing orbitals. Removing one axial donor gives C₄ᵥ symmetry; the middle pair can cross as axial strength varies.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.08,1,1));fig.savefig('paper-2-fields.png',dpi=170,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)
