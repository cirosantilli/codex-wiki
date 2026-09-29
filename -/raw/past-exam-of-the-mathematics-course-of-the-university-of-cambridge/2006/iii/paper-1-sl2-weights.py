"""sl2 tensor weight diagrams. Outputs paper-1-sl2-weights.png in caller CWD.
Tested Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5; respects caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(9.3,4.6),layout='constrained')
rows=[(3,[-5,-3,-1,1,3,5],[1,2,3,3,2,1],r'$S^3V\otimes S^2V$'),
      (2,[-5,-3,-1,1,3,5],[1]*6,r'$\Gamma_5$'),
      (1,[-3,-1,1,3],[1]*4,r'$\Gamma_3$'),
      (0,[-1,1],[1]*2,r'$\Gamma_1$')]
colors=['#176fac','#3a7c42','#cb6b20','#954d9b']
for k,(y,weights,mults,title) in enumerate(rows):
    ax.plot([min(weights),max(weights)],[y,y],color=colors[k],alpha=.45,zorder=1)
    ax.scatter(weights,[y]*len(weights),s=360,c='white',edgecolors=colors[k],linewidths=2,zorder=2)
    for x,m in zip(weights,mults):ax.text(x,y,str(m),ha='center',va='center',fontsize=12,zorder=3)
    ax.text(-6.6,y,title,ha='right',va='center',fontsize=14,color=colors[k])
    if k:ax.text(max(weights)+.35,y,'highest',va='center',fontsize=10,color=colors[k])
ax.set_xlim(-8.5,7.2);ax.set_ylim(-.7,3.8)
ax.set_xticks(range(-5,6,2));ax.set_yticks([])
ax.set_xlabel(r'Weight (eigenvalue of $H$)',fontsize=12)
ax.set_title('Weight multiplicities and irreducible strings',fontsize=15)
for side in ['left','right','top']:ax.spines[side].set_visible(False)
ax.text(.98,.98,'Number at a point = multiplicity',transform=ax.transAxes,ha='right',va='top',fontsize=11)
fig.savefig('paper-1-sl2-weights.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
