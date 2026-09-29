"""Original silver/silver-sulfate reference schematic, Python 3.14.

Use matplotlib only; output basename is relative to the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle

fig,ax=plt.subplots(figsize=(8.4,5.5),layout='constrained')
fig.patch.set_facecolor('white')
ax.set(xlim=(0,10),ylim=(0,7))
ax.axis('off')
ax.add_patch(Rectangle((.65,1.0),8.7,3.0,fc='#e8f0f8',ec='none'))
ax.plot([.65,.65,9.35,9.35],[4.6,1,1,4.6],color='#465662',lw=1.7)
ax.text(6.0,1.4,'Sulfate sample',ha='center',fontsize=12)
ax.add_patch(Rectangle((1.3,2.05),3.1,3.25,fc='white',ec='#46665e',lw=1.6))
ax.add_patch(Rectangle((1.32,2.07),3.06,2.05,fc='#e6f2ec',ec='none'))
ax.add_patch(Rectangle((1.32,2.07),3.06,.34,fc='#c6c6bf',ec='none',hatch='..'))
ax.add_patch(Rectangle((2.05,2.55),.18,2.8,fc='#909aa2',ec='#46525b'))
ax.text(2.8,5.5,'Ag wire',ha='center',fontsize=11)
ax.text(2.9,3.6,'Controlled sulfate\nfilling electrolyte',ha='center',va='center',fontsize=10.5)
ax.text(2.9,2.75,r'Excess Ag$_2$SO$_4$(s)',ha='center',fontsize=10)
ax.add_patch(Rectangle((4.31,2.3),.18,.7,fc='#b7c9cc',ec='#537381',hatch='////'))
ax.annotate('Porous frit',xy=(4.4,2.65),xytext=(5.0,2.2),fontsize=10.5,
    arrowprops={'arrowstyle':'->','color':'#526976'})
ax.add_patch(Rectangle((7.15,2.65),.22,2.7,fc='#8a6e53',ec='#624b37'))
ax.text(7.7,4.8,'Working\nelectrode',ha='left',fontsize=11)
ax.plot([2.14,2.14,4.6],[5.35,6.3,6.3],color='#4c5864',lw=1.5)
ax.plot([7.26,7.26,5.4],[5.35,6.3,6.3],color='#4c5864',lw=1.5)
ax.add_patch(Circle((5,6.3),.4,fc='white',ec='#4c5864',lw=1.5))
ax.text(5,6.3,'V',ha='center',va='center',fontsize=15)
ax.text(4.35,6.55,'−',fontsize=15)
ax.text(5.5,6.55,'+',fontsize=15)
ax.text(5,5.45,'High-input-impedance voltmeter',ha='center',fontsize=10.5)
ax.text(5,.35,r'$V_{\rm meas}\approx E_{\rm working}-E_{\rm reference}$',ha='center',fontsize=13)
fig.savefig('paper-1-additional-reference.png',dpi=160,facecolor='white')
plt.close(fig)
