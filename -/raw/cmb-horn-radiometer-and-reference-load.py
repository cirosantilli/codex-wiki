"""Functional source comparison, not an apparatus reconstruction; PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def main():
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(12.7, 5.8), constrained_layout=True)
    ax.set(xlim=(-.3, 13.3), ylim=(-.2, 6.3))
    ax.axis('off')
    def box(x,y,w,h,label,color='#eaf1f6',dashed=False):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.05',facecolor=color,edgecolor='#334857',lw=1.4,linestyle='--' if dashed else '-'))
        ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=11.5)
    def arrow(a,b,color='#334857',dashed=False):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.5,color=color,linestyle='--' if dashed else '-'))
    boxes=[(0,4,1.65,1.0,'Sky'),(2.05,4,1.75,1.0,'Atmosphere'),(4.2,4,1.8,1.0,'Horn\nantenna'),(6.45,4,1.8,1.0,'Comparison\nswitch'),(8.7,4,1.8,1.0,'Maser\nreceiver'),(10.95,4,1.8,1.0,'Detected\noutput')]
    for x,y,w,h,label in boxes:box(x,y,w,h,label)
    for i in range(len(boxes)-1):arrow((boxes[i][0]+boxes[i][2],4.5),(boxes[i+1][0],4.5))
    ax.text(2.925,5.45,'Attenuation + emission',ha='center',fontsize=10.5)
    arrow((2.925,5.25),(2.925,5.02))
    box(3.9,2.05,2.35,.85,'Ground pickup',color='#fff1de')
    arrow((5.075,2.92),(5.075,3.98),color='#b16a1c')
    ax.text(5.1,5.7,'Antenna thermal loss',ha='center',fontsize=10.5)
    arrow((5.1,5.47),(5.1,5.02),color='#b16a1c')
    box(6.45,2.05,2.3,.85,'Helium-cooled\nreference',color='#e8f3ef')
    arrow((7.35,2.92),(7.35,3.98))
    box(9.0,.65,2.5,.9,'Warm reference\n(illustrative only)',color='#f7f7f7',dashed=True)
    ax.plot([10.25,10.25,8.05],[1.55,3.4,3.4],color='#334857',lw=1.5,linestyle='--')
    arrow((8.05,3.4),(8.05,3.98),dashed=True)
    ax.text(.05,.55,'A calibrated response scale does not remove real radiation\nfrom the atmosphere, ground or antenna.',fontsize=12,ha='left',va='center')
    fig.suptitle('Source comparison and propagation corrections are separate tasks',fontsize=16)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
