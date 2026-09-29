"""Original proof diagram for the composite modulus 561; PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, xy, wh, text, color, size=12):
    x,y=xy;w,h=wh
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.015',
                 ec='#40546a',fc=color,lw=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.6)


def main():
    fig,ax=plt.subplots(figsize=(10.8,5.8),facecolor='white')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.text(.5,.96,'Why every coprime base passes modulo 561',ha='center',
            fontsize=18,weight='bold')
    box(ax,(.18,.77),(.64,.13),r'$561=3\cdot11\cdot17$'+'\n'+r'Assume $\gcd(a,561)=1$', '#eaf2fa',14)
    for x,p,q in [(.03,3,280),(.365,11,56),(.7,17,35)]:
        exponent=p-1
        assert 560==exponent*q
        text=(fr'Modulo {p}'+'\n'+fr'$a^{{{exponent}}}\equiv1$'+'\n'+
              fr'$560={exponent}\times{q}$'+'\n'+fr'$a^{{560}}\equiv1$')
        box(ax,(x,.38),(.27,.27),text,'#e6f3ed',14)
        ax.annotate('',xy=(x+.135,.66),xytext=(.5,.765),
                    arrowprops={'arrowstyle':'-|>','color':'#40546a','lw':1.3})
        ax.annotate('',xy=(.5,.235),xytext=(x+.135,.365),
                    arrowprops={'arrowstyle':'-|>','color':'#40546a','lw':1.3})
    box(ax,(.13,.065),(.74,.16),'Chinese remainder theorem'+'\n'+
        r'$(1,1,1)$ combines uniquely to $1\;(\mathrm{mod}\;561)$', '#fff2df',14)
    ax.text(.5,.012,'Distinct prime factors + each predecessor dividing 560 = an all-unit certificate.',
            ha='center',fontsize=10.5,color='#40546a')
    fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
