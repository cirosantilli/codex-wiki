"""Original plant-symbiosis control schematic; Python 3.14 and matplotlib.

Write PNG to the current working directory, never beside this source by default.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(9.2,6.3), layout='constrained')
fig.patch.set_facecolor('white')
ax.set(xlim=(0,10), ylim=(0,7.5))
ax.axis('off')

def box(x,y,text,w=3.0,h=0.75,color='#eaf4ef'):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.06',facecolor=color,edgecolor='#38585f',lw=1.2))
    ax.text(x,y,text,ha='center',va='center',fontsize=10.5)

def arrow(a,b,label=None):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','lw':1.5,'color':'#336a76'})
    if label:
        ax.text((a[0]+b[0])/2+0.12,(a[1]+b[1])/2,label,va='center',fontsize=9)

ax.text(5,7.2,'Engagement is controlled at several stages',ha='center',fontsize=15,weight='bold')
box(2.1,6,'Partner signals +\nhost nutrient / defense state',w=3.5)
box(7.6,6,'Local infection and\ndevelopmental permission',w=3.5)
arrow((3.95,6),(5.75,6))
ax.text(2.6,4.95,'Lotus nodulation feedback example',ha='center',fontsize=11,weight='bold')
box(2.6,4.25,'Root symbiotic signaling\nand CLE peptides',w=3.8)
box(2.6,2.8,'Shoot HAR1 pathway\nreduced permissive miR2111',w=3.8)
box(2.6,1.35,'Root TML restraint rises\nless further infection',w=3.8,color='#f8ece5')
arrow((2.6,3.8),(2.6,3.25))
arrow((2.6,2.35),(2.6,1.8))
ax.text(7.6,4.95,'Control after association',ha='center',fontsize=11,weight='bold')
box(7.6,4.25,'Actual nutrient delivery\nand host carbon allocation',w=3.6)
box(7.6,2.8,'Conditional support:\nsanctions or reciprocal rewards',w=3.6)
box(7.6,1.35,'Partner success and\ncontinued exchange',w=3.6,color='#f8ece5')
arrow((7.6,3.8),(7.6,3.25))
arrow((7.6,2.35),(7.6,1.8))
ax.text(5,0.35,'Quantity control and partner-performance control are distinct.\nNot all beneficial microorganisms use the common symbiosis pathway.',ha='center',fontsize=10,color='#43515a')
fig.savefig('paper-plm1-symbiosis-feedback.png',dpi=160,facecolor='white')
plt.close(fig)
