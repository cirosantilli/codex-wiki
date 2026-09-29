"""Original point-force mobility field, not a source illustration."""
import numpy as np
import matplotlib.pyplot as plt

def main():
 plt.rcParams.update({'font.size':10})
 x=np.linspace(-3,3,17);X,Y=np.meshgrid(x,x);r=np.hypot(X,Y);r[r<.3]=np.nan
 ux=(1+X*X/r**2)/r;uy=X*Y/r**3
 fig,ax=plt.subplots(1,2,figsize=(8.2,4),layout='constrained',gridspec_kw={'width_ratios':[1.3,1]})
 ax[0].quiver(X,Y,ux,uy,color='#266f9b',angles='xy',scale_units='xy',scale=5,width=.004)
 ax[0].scatter([0],[0],s=65,c='crimson',zorder=5);ax[0].annotate('',(1,0),(0,0),arrowprops={'arrowstyle':'->','color':'crimson','lw':2});ax[0].text(.65,.2,'F',c='crimson')
 ax[0].set_aspect('equal');ax[0].set(xlim=(-3.3,3.3),ylim=(-3.3,3.3),xlabel='x / reference length',ylabel='y / reference length',title='Point force along +x')
 ax[1].bar(['Parallel','Perpendicular'],[2,1],color=['#377ca5','#dfa94c'],width=.6);ax[1].set(ylabel=r'$8\pi\eta r\,\mu$',ylim=(0,2.45),title='Equal separation, different mobility')
 for j,v in enumerate([2,1]):ax[1].text(j,v+.08,str(v),ha='center')
 for a in ax:a.spines[['top','right']].set_visible(False)
 fig.savefig('paper-1-oseen-response.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
