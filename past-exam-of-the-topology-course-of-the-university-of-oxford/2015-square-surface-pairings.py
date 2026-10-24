"""Generate 2015-square-surface-pairings.png in the current directory; Python 3.14/Matplotlib."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    examples=[('Sphere', [('a',1),('a',-1),('b',1),('b',-1)], 3, 'orientable'),
              ('Projective plane', [('a',1),('a',1),('b',1),('b',-1)], 2, 'nonorientable'),
              ('Torus', [('a',1),('b',1),('a',-1),('b',-1)], 1, 'orientable'),
              ('Klein bottle', [('a',1),('b',1),('a',-1),('b',1)], 1, 'nonorientable')]
    vertices=np.array([[0,0],[1,0],[1,1],[0,1]])
    fig, axes=plt.subplots(1,4,figsize=(11.4,3.2),dpi=110,facecolor='white')
    for ax,(name,word,count,orientation) in zip(axes,examples):
        ax.fill([0,1,1,0],[0,0,1,1],facecolor='#f8fafc')
        for i,(letter,sign) in enumerate(word):
            a=vertices[i];b=vertices[(i+1)%4];color='#2563eb' if letter=='a' else '#b45309'
            ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=1.4)
            start,end=(a,b) if sign==1 else (b,a)
            p=start+0.32*(end-start);q=start+0.68*(end-start)
            ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'-|>','color':color,'lw':2})
            centre=(a+b)/2;outward=np.array([b[1]-a[1],a[0]-b[0]])
            labelpos=centre+0.16*outward
            ax.text(*labelpos,letter,ha='center',va='center',fontsize=12,color=color)
        ax.set_title(name,fontsize=11,pad=10)
        ax.text(0.5,-0.35,rf'$V={count},\quad\chi={count-1}$'+'\n'+orientation,ha='center',va='center',fontsize=9)
        ax.set_xlim(-0.3,1.3);ax.set_ylim(-0.58,1.25);ax.set_aspect('equal');ax.axis('off')
    fig.tight_layout(pad=1.1,w_pad=1.5)
    fig.savefig('2015-square-surface-pairings.png',dpi=110,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
