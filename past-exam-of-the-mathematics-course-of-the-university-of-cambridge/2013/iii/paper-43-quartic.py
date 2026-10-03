"""Opaque quartic vertex diagram, Python3.14.4/matplotlib3.10.7.
Write the PNG basename to caller cwd; caller owns MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.2,4.2),dpi=100,facecolor='white')
ax.set_facecolor('white')
legs=[(-1.6,1.0,r'$\varphi$'),(-1.6,-1.0,r'$\varphi$'),(1.6,1.0,r'$\varphi^*$'),(1.6,-1.0,r'$\varphi^*$')]
for x,y,label in legs:
 ax.plot([0,x],[0,y],color='#233e50',lw=2)
 ax.text(x*1.13,y*1.12,label,ha='center',va='center',fontsize=22,color='#233e50')
ax.scatter([0],[0],s=60,color='#233e50',zorder=4)
ax.text(0,-1.7,r'$\mathcal{L}_{\mathrm{int}}=-|g|^2\varphi^{*2}\varphi^2\qquad\Longrightarrow\qquad -4i|g|^2$',ha='center',fontsize=17)
ax.text(0,1.75,'Complex-scalar quartic vertex',ha='center',fontsize=17)
ax.text(0,-2.1,'Two legs of each field type; all external momenta taken incoming',ha='center',fontsize=10)
ax.set_xlim(-2.4,2.4);ax.set_ylim(-2.4,2.2);ax.axis('off')
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.02)
fig.savefig('paper-43-quartic.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
