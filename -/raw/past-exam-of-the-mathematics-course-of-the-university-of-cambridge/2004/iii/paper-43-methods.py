"""Original statistical sketches. Python 3.14/NumPy 2.3/Matplotlib 3.10.
Writes only paper-43-methods.png to caller cwd; respects caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig,axes=plt.subplots(3,2,figsize=(11,13))
    ax=axes[0,0]
    t=np.linspace(0,2*np.pi,60,endpoint=False)
    theta=.6; rot=np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    points=np.column_stack([np.sqrt(18)*np.cos(t),np.sqrt(2)*np.sin(t)])@rot.T
    ax.scatter(*points.T,s=12,color='#427ba0')
    for j,col in enumerate(['#a44b25','#247547']):
        v=rot[:,j]*[4.5,1.8][j]
        ax.annotate('',xy=v,xytext=-v,arrowprops={'arrowstyle':'<->','color':col,'lw':2})
        ax.text(*(v+np.array([.1,.1])),f'PC{j+1}',color=col)
    ax.set_aspect('equal');ax.set_xlabel('Centered variable 1');ax.set_ylabel('Centered variable 2')
    ax.set_title('PCA: orthogonal directions of sample variation')
    ax=axes[0,1];values=np.array([9,1,.4,.2,.1,.05])
    ax.plot(range(1,7),values,'o-',color='#427ba0')
    ax.set_xticks(range(1,7));ax.set_xlabel('Principal component');ax.set_ylabel('Variance (common normalization)')
    ax.set_title('Scree plot for illustrative six-variable data')
    ax=axes[1,0]
    for xy,w,h,col,label in [((0,0),.5,1,'#dbe8f1','A'),((.5,0),.5,.6,'#f5dec9','B'),((.5,.6),.5,.4,'#daebd4','C')]:
        ax.add_patch(Rectangle(xy,w,h,facecolor=col,edgecolor='none'))
        ax.text(xy[0]+w/2,xy[1]+h/2,label,ha='center',va='center',fontsize=16)
    ax.plot([.5,.5],[0,1],color='black');ax.plot([.5,1],[.6,.6],color='black')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal');ax.set_xlabel('Predictor x1');ax.set_ylabel('Predictor x2')
    ax.set_title('Recursive axis-aligned partition')
    ax=axes[1,1]
    nodes={'root':(.5,.9),'A':(.2,.5),'right':(.75,.5),'B':(.6,.12),'C':(.9,.12)}
    for a,b in [('root','A'),('root','right'),('right','B'),('right','C')]:
        ax.plot([nodes[a][0],nodes[b][0]],[nodes[a][1],nodes[b][1]],color='#427ba0')
    labels={'root':'x1 < 0.5?','right':'x2 < 0.6?','A':'Leaf A','B':'Leaf B','C':'Leaf C'}
    for n,(x,y) in nodes.items():ax.text(x,y,labels[n],ha='center',va='center',bbox={'facecolor':'white','edgecolor':'#427ba0','boxstyle':'round,pad=0.5'})
    for x,y,label in [(.32,.71,'yes'),(.68,.71,'no'),(.64,.3,'yes'),(.86,.3,'no')]:ax.text(x,y,label,fontsize=9)
    ax.set_xlim(0,1);ax.set_ylim(0,1.05);ax.axis('off');ax.set_title('Equivalent classification or regression tree')
    # An exact Euclidean distance example, independently recovered by double centering.
    P=np.array([[-2,-1],[-1,1],[0,-.5],[1,1.5],[2,-1]],dtype=float)
    D=np.linalg.norm(P[:,None,:]-P[None,:,:],axis=2)
    H=np.eye(5)-np.ones((5,5))/5
    G=-.5*H@(D**2)@H
    eigen,U=np.linalg.eigh(G);indices=np.argsort(eigen)[::-1][:2]
    X=U[:,indices]*np.sqrt(eigen[indices])
    for ax,Q,title in [(axes[2,0],P,'Input configuration: Euclidean distances'),(axes[2,1],X,'Classical scaling: same distances, new axes')]:
        ax.scatter(*Q.T,color='#427ba0',s=45)
        for i,(x,y) in enumerate(Q):ax.text(x+.08,y+.08,chr(65+i))
        ax.set_aspect('equal');ax.margins(.2);ax.set_xlabel('Coordinate 1');ax.set_ylabel('Coordinate 2');ax.set_title(title)
    for ax in axes.flat:
        if ax.axison:ax.spines[['top','right']].set_visible(False)
    fig.tight_layout(pad=2)
    fig.savefig('paper-43-methods.png',dpi=110,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
