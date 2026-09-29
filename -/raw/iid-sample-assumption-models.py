"""Original dependency diagrams for iid, common-coin, and heterogeneous samples."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def node(ax,x,y,text,color):
    ax.text(x,y,text,ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.42','fc':color,'ec':'#31546b','lw':1.2})


def arrow(ax,a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,lw=1.25,color='#546776'))


def main():
    fig,axes=plt.subplots(1,3,figsize=(12.3,5.2),dpi=100,facecolor='white')
    fig.suptitle('Identical distributions and independent draws are separate requirements',fontsize=16,y=.97)
    positions=[.12,.37,.63,.88]
    for ax in axes:ax.set_xlim(-.02,1.02);ax.set_ylim(0,1);ax.axis('off')
    axes[0].set_title('IID: independent, one common law',fontsize=12,pad=14)
    for i,x in enumerate(positions,1):
        node(axes[0],x,.7,f'Z{i}\np = ½','#d8eaf4');node(axes[0],x,.26,f'X{i}', '#eef4f7');arrow(axes[0],(x,.57),(x,.36))
    axes[0].text(.5,.94,'Four separate fair Bernoulli draws',ha='center',fontsize=11)
    axes[0].text(.5,.06,'Each pattern has probability 1/16',ha='center',fontsize=11)
    axes[1].set_title('Identical laws, shared randomness',fontsize=12,pad=14)
    node(axes[1],.5,.7,'Z\np = ½','#f4d9bf')
    for i,x in enumerate(positions,1):
        node(axes[1],x,.26,f'X{i}', '#eef4f7');arrow(axes[1],(.5,.59),(x,.36))
    axes[1].text(.5,.94,'One draw, copied four times',ha='center',fontsize=11)
    axes[1].text(.5,.06,'Only 0000 or 1111; probability ½ each',ha='center',fontsize=10.5)
    axes[2].set_title('Independent, different laws',fontsize=12,pad=14)
    ps=['¼','¾','¼','¾']
    for i,(x,p) in enumerate(zip(positions,ps),1):
        node(axes[2],x,.7,f'Z{i}\np = {p}', '#d8eaf4' if p=='¼' else '#f4d9bf');node(axes[2],x,.26,f'X{i}','#eef4f7');arrow(axes[2],(x,.57),(x,.36))
    axes[2].text(.5,.94,'Separate draws; unequal success probabilities',ha='center',fontsize=10.3)
    axes[2].text(.5,.06,'Joint probabilities factor, marginals differ',ha='center',fontsize=10.3)
    fig.subplots_adjust(left=.025,right=.98,bottom=.13,top=.77,wspace=.17)
    fig.text(.5,.035,'Arrows show the specified random-variable construction. All probabilities follow from the chosen models.',ha='center',fontsize=10.5)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)


if __name__=='__main__':main()
