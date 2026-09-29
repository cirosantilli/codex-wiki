"""Original derived PMOS networks; Python 3.14.4 / Matplotlib 3.10.7.
Writes the matching opaque PNG to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def main():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 4), dpi=110)
    fig.patch.set_facecolor('white')
    def device(ax, x, y, name):
        ax.plot([x,x],[y+.28,y+1],color='black',lw=1.4)
        ax.plot([x,x],[y-1,y-.28],color='black',lw=1.4)
        ax.add_patch(Rectangle((x-.09,y-.28),.18,.56,facecolor='#e8edf3',edgecolor='black'))
        ax.plot([x-.3,x-.3],[y-.3,y+.3],color='black',lw=1.3)
        ax.add_patch(Circle((x-.43,y),.08,facecolor='white',edgecolor='black'))
        ax.plot([x-.85,x-.51],[y,y],color='black',lw=1.2)
        ax.text(x-.9,y,name,ha='right',va='center',fontsize=12)
    for ax, labels, title, middle in zip(axes,[('a','b','c','d'),('a','b','c','d')],
           ['Before the P–Q connection','After the P–Q connection'],[True,False]):
        ax.set(xlim=(-.35,3.85),ylim=(.4,5.8))
        ax.axis('off');ax.set_title(title,fontsize=11)
        ax.plot([1,3],[5,5],color='black',lw=1.4)
        ax.plot([1,3.65],[1,1],color='black',lw=1.4)
        ax.text(2,5.25,'Vdd',ha='center',fontsize=11)
        ax.text(3.72,1,'z',va='center',fontsize=12)
        for x,y,label in [(1,4,labels[0]),(3,4,labels[1]),(1,2,labels[2]),(3,2,labels[3])]:
            device(ax,x,y,label)
        if middle:ax.plot([1,3],[3,3],color='black',lw=1.4)
    fig.text(.5,.035,'Each device is PMOS: its branch conducts when its labelled input is 0.',
             ha='center',fontsize=9)
    fig.subplots_adjust(left=.04,right=.98,bottom=.1,top=.87,wspace=.12)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
