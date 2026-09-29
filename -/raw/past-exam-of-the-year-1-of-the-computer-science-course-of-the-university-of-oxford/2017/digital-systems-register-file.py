"""Original register-file block diagrams; write the PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig,axes=plt.subplots(1,2,figsize=(12,7),dpi=100)
for ax,alternative in zip(axes,[False,True]):
    ax.set(xlim=(0,10),ylim=(0,10));ax.axis('off')
    def box(x,y,w,h,label,color='#e4edf6',size=11):
        ax.add_patch(Rectangle((x,y),w,h,facecolor=color,edgecolor='#263f54',lw=1.4))
        ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=size)
    def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=12,lw=1.25,color='#263f54'))
    ax.set_title('MIPS: suppressed writes to zero' if alternative else 'Generic register file: two reads, one write',fontsize=12,pad=13)
    box(3.7,3,2.3,4.2,'',color='#fafbfc')
    for y,label in [(6.25,'0 (hardwired)' if alternative else 'register 0'),(5.35,'register 1'),(4.45,'⋮'),(3.55,'register 31' if alternative else 'register k − 1')]:
        box(3.9,y,1.9,.65,label,color='#dfefdf' if alternative and y>6 else '#e4edf6',size=10)
    # Word width is labelled on the input bus to avoid crossing the clock wire.
    ax.text(4.85,8.15,'write data (32 bits)' if alternative else 'write data (n bits)',ha='center',fontsize=11);arrow((4.85,7.9),(4.85,7.22))
    box(1.1,2.5,1.65,1.2,'address\ndecoder',size=11)
    ax.text(.2,4.1,'write\naddress',fontsize=10,ha='left');arrow((.9,3.75),(1.6,3.72))
    if not alternative:
        ax.text(.2,1.55,'RegWrite',fontsize=10);arrow((1.2,1.8),(1.8,2.48))
    arrow((2.78,3.1),(3.68,4.6));ax.text(2.85,4.1,'weᵢ',fontsize=11)
    ax.text(4.85,1.5,'clock edge',ha='center',fontsize=10);arrow((4.85,1.8),(4.85,2.98))
    for n,y in [(1,6),(2,4.1)]:
        box(7, y-.4,.9,.8,'MUX',size=10)
        arrow((6.02,y),(6.98,y));arrow((7.92,y),(9.7,y))
        ax.text(9.55,y+.23,f'read {n}',ha='right',fontsize=10)
        if n==1:
            ax.text(8.2,7.7,'read address 1',ha='center',fontsize=10)
            arrow((7.45,7.4),(7.45,6.43))
        else:
            ax.text(8.1,2.8,'read address 2',ha='center',fontsize=10)
            arrow((7.45,3.0),(7.45,3.68))
    line='weᵢ = [write address = i],  i = 1,…,31' if alternative else 'weᵢ = RegWrite ∧ [write address = i]'
    ax.text(5,.65,line,ha='center',fontsize=10)
    if alternative:ax.text(5,.1,'Read address 0 returns 0; write address 0 enables nothing.',ha='center',fontsize=9)
fig.subplots_adjust(left=.025,right=.985,bottom=.06,top=.9,wspace=.14)
fig.savefig(Path.cwd()/'digital-systems-register-file.png',facecolor='white')
