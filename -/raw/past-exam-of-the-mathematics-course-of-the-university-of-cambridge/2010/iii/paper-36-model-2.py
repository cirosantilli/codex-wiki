"""Write paper-36-model-2.png in the caller's current directory.

Tested: Python 3.14.4, Matplotlib 3.10.7 (existing root dependencies).
The caller supplies MPLCONFIGDIR as needed; this generator leaves it unchanged.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, FancyArrowPatch, Rectangle

fig, ax = plt.subplots(figsize=(11.6, 8.3), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set(xlim=(0,14), ylim=(0,10))
ax.axis('off')
fig.subplots_adjust(left=.01,right=.99,bottom=.01,top=.99)
positions = {'delta':(1.2,8.6),'tau':(3.1,8.6),'theta':(5,8.6),
             'psi':(6.9,8.6),'beta':(8.8,8.6),'gamma':(10.7,8.6),
             'q':(12.6,8.6),'alpha':(2.5,6.0),'base':(6.7,6.0),
             'baseline':(11.7,6.0),'time':(2.5,2.9),'mean':(6.7,2.9),
             'follow':(11.7,2.9)}
ax.text(7,9.72,'Latent baseline and repeated follow-up model',ha='center',va='center',fontsize=16,weight='bold')
ax.add_patch(Rectangle((.25,.55),13.5,6.6,facecolor='none',edgecolor='#688099',linewidth=1.4))
ax.add_patch(Rectangle((.7,1.05),12.6,3.35,facecolor='#f8fafc',edgecolor='#a2b1be',linewidth=1.1))
ax.text(.48,.77,'Children: i = 1, ..., 106',fontsize=11,color='#34495e')
ax.text(.94,1.31,'Follow-up visits: j = 1, 2, 3',fontsize=11,color='#34495e')
labels={'delta':r'$\delta$'+'\nUniform(-100, 100)',
        'tau':r'$\tau$'+'\nUniform(0, 100)',
        'theta':r'$\theta$'+'\nUniform(-100, 100)',
        'psi':r'$\psi$'+'\nUniform(0, 100)',
        'beta':r'$\beta$'+'\nUniform(-100, 100)',
        'gamma':r'$\gamma$'+'\nUniform(-100, 100)',
        'q':r'$q=1/\sigma^2$'+'\nGamma(.001, .001)',
        'alpha':r'$\alpha_i$'+'\nChild intercept',
        'base':r'$\mu_{0i}$'+'\nTrue log-baseline',
        'baseline':r'$y_{0i}$'+'\nBaseline assay',
        'time':r'$\log t_{ij}$'+'\nKnown log-time',
        'mean':r'$\mu_{ij}$'+'\nFollow-up mean',
        'follow':r'$y_{ij}$'+'\nFollow-up assay'}
node_patches={}
for key,(x,y) in positions.items():
    if key in ('delta','tau','theta','psi','beta','gamma','q'):
        patch=FancyBboxPatch((x-.83,y-.49),1.66,.98,boxstyle='round,pad=0.06',facecolor='white',edgecolor='#34495e',linewidth=1.3)
    elif key=='mean':
        patch=Rectangle((x-1.15,y-.49),2.3,.98,facecolor='white',edgecolor='#34495e',linewidth=1.3)
    else:
        patch=Ellipse((x,y),2.3,1.04,facecolor='#dce8f3' if key in ('baseline','time','follow') else 'white',edgecolor='#34495e',linewidth=1.3)
    ax.add_patch(patch);node_patches[key]=patch
    ax.text(x,y,labels[key],ha='center',va='center',fontsize=9 if key in ('delta','tau','theta','psi','beta','gamma','q') else 11,zorder=4)

def arrow(source,target,rad=0):
    ax.add_patch(FancyArrowPatch(positions[source],positions[target],patchA=node_patches[source],patchB=node_patches[target],arrowstyle='-|>',mutation_scale=13,linewidth=1.35,color='#42596e',connectionstyle=f'arc3,rad={rad}',shrinkA=3,shrinkB=4,zorder=3))

for source,target,rad in [('delta','alpha',0),('tau','alpha',0),('theta','base',0),('psi','base',0),('alpha','mean',0),('base','mean',0),('base','baseline',0),('beta','mean',-.15),('gamma','mean',-.20),('q','baseline',0),('q','follow',-.37),('time','mean',0),('mean','follow',0)]:
    arrow(source,target,rad)
ax.text(7,1.95,r'$\mu_{ij}=\alpha_i+\beta\log t_{ij}+\gamma\mu_{0i}$',ha='center',fontsize=12)
ax.text(7,.27,'Blue: observed     Ellipse: stochastic     Rectangle: deterministic     Rounded box: prior parameter',ha='center',fontsize=8,color='#34495e')
ax.text(7,.05,'Gamma priors use shape and rate',ha='center',fontsize=8,color='#34495e')
fig.savefig('paper-36-model-2.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
