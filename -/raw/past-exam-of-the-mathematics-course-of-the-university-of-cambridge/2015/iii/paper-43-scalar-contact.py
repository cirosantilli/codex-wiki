"""Draw the scalar contact vertex; write only the PNG basename in caller cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=100,facecolor='white')
ax.set_facecolor('white')
ends=[(-2,1.1),(-2,-1.1),(2,1.1),(2,-1.1)]
for j,(x,y) in enumerate(ends):
 ax.plot([x,0],[y,0],color='#24364b',linestyle=(0,(5,4)),linewidth=2)
 start,end=((0.76*x,0.76*y),(0.47*x,0.47*y)) if j<2 else ((0.47*x,0.47*y),(0.76*x,0.76*y))
 ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color='#24364b',lw=1.7))
 ax.text(x*1.12,y*1.1,rf'$p_{j+1}$',ha='center',va='center',fontsize=18)
ax.scatter([0],[0],s=70,color='#b34a28',zorder=4)
ax.text(0,-0.46,r'$i\lambda$',ha='center',va='center',fontsize=19,color='#8f351e')
ax.text(-2,1.55,'Incoming',ha='center',fontsize=13,color='#24364b')
ax.text(2,1.55,'Outgoing',ha='center',fontsize=13,color='#24364b')
ax.text(0,1.85,'Real-scalar contact interaction',ha='center',fontsize=15)
ax.set_xlim(-2.9,2.9);ax.set_ylim(-1.65,2.1);ax.axis('off')
fig.savefig('paper-43-scalar-contact.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
