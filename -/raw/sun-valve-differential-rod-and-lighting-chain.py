"""Functional sun-valve/lighting schematic; emit a white PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(15,7.2),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1,1.4]})
    fig.subplots_adjust(left=.025,right=.985,bottom=.13,top=.84,wspace=.12)
    fig.suptitle('A thermal comparison controls daylight shutoff; a separate mechanism produces flashes',fontsize=17,y=.97)
    ax.set(xlim=(0,7),ylim=(0,8));ax.axis('off')
    bx.set(xlim=(0,10),ylim=(0,8));bx.axis('off')
    ax.set_title('Three polished references and one dark rod',fontsize=13,pad=18)
    bx.set_title('Separate functions in a gas-lighting chain',fontsize=13,pad=18)
    ax.add_patch(FancyBboxPatch((1.05,1.65),4.9,4.85,boxstyle='round,pad=.12',facecolor='#f5fafc',edgecolor='#8aa8b5',linewidth=1.7))
    ax.add_patch(Rectangle((1.0,1.45),5.0,.24,facecolor='#697a83'))
    for x in [1.7,2.5,5.15]:
        ax.add_patch(Rectangle((x-.10,1.70),.20,3.15,facecolor='#bfcbd2',edgecolor='#5f727e'))
    ax.plot([1.6,5.25],[4.85,4.85],color='#8a9ca6',linewidth=2)
    ax.add_patch(Rectangle((3.7-.14,1.70),.28,4.0,facecolor='#222',edgecolor='#111'))
    ax.annotate('',xy=(4.45,5.7),xytext=(4.45,4.85),arrowprops={'arrowstyle':'<->','color':'#a53b2f','linewidth':1.6})
    ax.text(4.65,5.27,'Relative\nextension',va='center',fontsize=11,color='#8d3027')
    ax.text(3.70,6.0,'Dark rod',ha='center',fontsize=12)
    ax.text(1.75,5.15,'Polished\nreference rods',ha='center',fontsize=11)
    ax.text(3.5,1.04,'Common support; matched material in the model',ha='center',fontsize=10)
    for i in range(3):
        ax.add_patch(FancyArrowPatch((.15+i*.45,7.15),(1.1+i*.45,6.1),arrowstyle='-|>',mutation_scale=16,color='#d19a24',linewidth=2))
    ax.text(.1,7.5,'Incident light',fontsize=12)
    ax.text(3.5,.18,'Differential heating → differential expansion\n→ mechanical command to the valve',ha='center',va='center',fontsize=12)

    def box(x,y,w,h,text,color='#edf3f8'):
        bx.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=color,edgecolor='#425564',linewidth=1.6))
        bx.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.4)
    def arrow(a,b,style='-',color='#425564'):
        bx.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,linewidth=1.7,linestyle=style,color=color))
    box(.3,5.1,2.15,1.3,'Gas supply')
    box(3.55,5.1,2.25,1.3,'Sun valve\ndaylight shutoff','#fff0d6')
    box(7.15,5.1,2.4,1.3,'Flasher\nrepeated pulses','#e7f1ed')
    box(7.15,2.0,2.4,1.3,'Main burner')
    box(.3,2.0,2.15,1.3,'Pilot flame\nsteady ignition','#fff0d6')
    arrow((2.58,5.75),(3.40,5.75));arrow((5.95,5.75),(7.0,5.75));arrow((8.35,4.95),(8.35,3.45))
    arrow((1.375,4.95),(1.375,3.45));arrow((2.6,2.65),(7.0,2.65),style='--',color='#b76c30')
    bx.text(4.80,3.0,'Ignites the admitted gas',ha='center',fontsize=11,color='#91511e')
    bx.text(4.675,7.3,'Rod-extension command',ha='center',fontsize=12)
    arrow((4.675,7.02),(4.675,6.55),color='#a53b2f')
    bx.text(5,.55,'Daylight permission and flash timing are different controls.\nThe pilot remains a separate consumption term.',ha='center',fontsize=12)
    fig.text(.5,.025,'Original functional schematic. Rod displacement is exaggerated; geometry and internal linkages are not to scale.',ha='center',fontsize=11)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
