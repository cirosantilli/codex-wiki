"""Original schematic of selected plant epigenetic pathways.
Tested with Python 3.14 and Matplotlib 3.10. Writes PNG basename to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


fig, ax = plt.subplots(figsize=(10, 6.3), layout='constrained')
ax.set(xlim=(0,1),ylim=(0,1))
ax.axis('off')


def box(x,y,w,h,label,color):
    patch=FancyBboxPatch((x-w/2,y-h/2),w,h,
                         boxstyle='round,pad=0.008,rounding_size=0.01',
                         facecolor=color,edgecolor='#365064',lw=1)
    ax.add_patch(patch)
    ax.text(x,y,label,ha='center',va='center',fontsize=9,color='#183142')


def arrow(a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,
                                 color='#365064',lw=1.2))


ax.text(.5,.98,'Selected routes for plant epigenetic states',ha='center',va='top',
        fontsize=15,weight='bold')
ax.text(.02,.88,'Sequence-guided establishment: canonical RdDM',fontsize=11,weight='bold')
xs=[.12,.37,.62,.87]
labels=['Pol IV + RDR2\nRNA precursor','DCL3\n24-nt siRNA','AGO4 + Pol V\nmatching and scaffold','DRM2\nDNA methylation']
for x,label in zip(xs,labels):box(x,.76,.21,.13,label,'#e3eef8')
for a,b in zip(xs[:-1],xs[1:]):arrow((a+.115,.76),(b-.115,.76))
ax.text(.02,.61,'Persistence after replication and reinforcing chromatin pathways',fontsize=11,weight='bold')
box(.165,.48,.28,.16,'MET1\nrestores CG methylation\nafter DNA replication','#e4f1e5')
box(.5,.48,.30,.16,'H3K9me2 ↔ CHG methylation\nCMT3 and SUVH4/5/6\nreinforce the two states','#e4f1e5')
box(.835,.48,.28,.16,'DDM1: chromatin access\nCMT2: a major contributor\nto heterochromatic CHH','#e4f1e5')
ax.text(.02,.32,'Erasure and a separate developmental-memory example',fontsize=11,weight='bold')
box(.255,.20,.43,.15,'ROS1 / DME with DNA repair\nactive DNA demethylation\nroles depend on locus and cell type','#f9e9d9')
box(.745,.20,.43,.15,'PRC2 → H3K27me3 at selected loci\nFLC silencing records prolonged cold\nELF6 contributes to reproductive reset','#eee7f5')
ax.text(.5,.045,'Simplified overview: routes overlap, and DNA methylation is distinct from histone methylation.',
        ha='center',va='center',fontsize=9,color='#365064')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
