"""Original protein-import control matrix; qualitative expectations, not measured data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(10.2,4.6),facecolor='white');ax.axis('off')
rows=[['Lumenal / matrix cargo','Protected','Degraded','Recovered'],
      ['Outer surface-bound cargo','Degraded','Degraded','Recovered'],
      ['Protease-resistant aggregate','May resist','May resist','May pellet']]
colors=[['#f2f5f7','#dceee7','#f6e5dd','#e8edf4'],['#f2f5f7','#f6e5dd','#f6e5dd','#e8edf4'],['#f2f5f7','#fff0ce','#fff0ce','#fff0ce']]
table=ax.table(cellText=rows,colLabels=['Protein location / state','Intact organelles\n+ protease','Disrupted organelles\n+ protease','No protease'],cellColours=colors,colWidths=[.33,.23,.23,.18],cellLoc='center',loc='center')
table.auto_set_font_size(False);table.set_fontsize(11);table.scale(1,3.2)
for (r,c),cell in table.get_celld().items():
    cell.set_edgecolor('white')
    if r==0:cell.set_facecolor('#245f8a');cell.set_text_props(color='white',weight='bold')
ax.set_title('Crossing a membrane is different from binding to its surface',fontsize=14,pad=18)
fig.text(.5,.065,'Require a sealed-organelle control, an accessible surface control and a no-organelle aggregation control.\nMembrane-protein import may protect only a mapped fragment; the whole protein need not be shielded.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.12,1,1))
fig.savefig('paper-4-import-controls.png',dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
