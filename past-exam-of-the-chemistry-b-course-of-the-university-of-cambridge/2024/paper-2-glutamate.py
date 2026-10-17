"""Five original local catalytic schematics; full substrate omitted; output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(5,1,figsize=(11,9.3),facecolor='white')
rows=[('General acid',r'E–CO₂H ··· N1=C6(NH₂)',r'E–CO₂⁻ + HN1⁺=C6(NH₂)','Carboxyl proton activates the ring; it may also protonate the leaving group.'),('General base',r'E–CO₂⁻ ··· H–OH + C6',r'E–CO₂H + HO–C6','Base accepts a proton as water oxygen attacks; other ring bonds change.'),('Covalent pathway',r'E–CO₂⁻ + activated C6',r'E–C(O)–O–C6 intermediate','A temporary enzyme–substrate bond must later be hydrolyzed.'),('Electrostatic / H-bond',r'E–CO₂⁻ ··· N⁺ in reacting substrate','Preferential stabilization','Charge or hydrogen bonding must favor the reacting configuration.'),('Orientation',r'E–CO₂H ··· N1—C6 ··· OH₂','Productive alignment','Protein contacts orient the purine and the oxygen nucleophile.')]
for a,(title,left,right,note) in zip(axs,rows):
 a.axis('off');a.set(xlim=(0,11),ylim=(0,1.6));a.text(.05,1.38,title,fontsize=12,weight='bold',color='#2268a0')
 a.text(.1,.83,left,fontsize=13,va='center');a.annotate('',(7,.83),(5.8,.83),arrowprops=dict(arrowstyle='->',lw=1.5));a.text(7.2,.83,right,fontsize=12,va='center');a.text(.1,.2,note,fontsize=11,color='#444')
fig.text(.5,.012,'E denotes the protein tether. These are possible catalytic contributions, not five demonstrated mechanisms for the same enzyme.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,1));fig.savefig('paper-2-glutamate.png',dpi=160,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)
