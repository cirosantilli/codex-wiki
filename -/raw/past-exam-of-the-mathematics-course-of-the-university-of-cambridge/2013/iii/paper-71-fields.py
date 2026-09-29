"""Illustrate a coupled freezing/melting similarity solution.
Python 3.14.4; matplotlib 3.10.7 and numpy 2.3.5.
Output: paper-71-fields.png in the current directory. Honor MPLCONFIGDIR.
"""
import math
from pathlib import Path

def dilution(A):
    return 1/(1+math.sqrt(math.pi)*A*math.exp(A*A)*math.erfc(-A))

def solve_model(S=40.,eps=2.5e-4,R=2.):
    lo,hi=0.,6.
    for _ in range(90):
        A=(lo+hi)/2
        if R*dilution(A)>2/(math.pi*S)+2*eps*A/math.sqrt(math.pi):lo=A
        else:hi=A
    A=(lo+hi)/2;B=eps*A+1/(S*math.sqrt(math.pi))
    def residual(A,B):
        a=eps*A
        theta=math.sqrt(math.pi)*S*B*math.exp(B*B)*(math.erf(B)-math.erf(a))
        return (S*a-S*B*math.exp(B*B-a*a)+(1-theta)*math.exp(-a*a)/(math.sqrt(math.pi)*math.erfc(-a)),theta-R*dilution(A))
    for _ in range(30):
        f,g=residual(A,B)
        if max(abs(f),abs(g))<1e-13:break
        dA=1e-6;dB=1e-7
        af,ag=residual(A+dA,B);bf,bg=residual(A,B+dB)
        fa,ga=(af-f)/dA,(ag-g)/dA
        fb,gb=(bf-f)/dB,(bg-g)/dB
        det=fa*gb-fb*ga
        A+=(-f*gb+g*fb)/det
        B+=(-g*fa+f*ga)/det
    a=eps*A
    theta=math.sqrt(math.pi)*S*B*math.exp(B*B)*(math.erf(B)-math.erf(a))
    assert A>0 and B>a and 0<theta<1
    assert max(abs(v) for v in residual(A,B))<1e-10
    return dict(S=S,eps=eps,R=R,A=A,a=a,B=B,theta=theta,c=dilution(A))

def temperature(u,m):
    a,B,theta=m['a'],m['B'],m['theta']
    if u<a:return -1+(1-theta)*math.erfc(-u)/math.erfc(-a)
    if u<=B:return -theta*(math.erf(B)-math.erf(u))/(math.erf(B)-math.erf(a))
    return 0.

def concentration(v,m):
    return 1+(m['c']-1)*math.erfc(-v)/math.erfc(-m['A']) if v<=m['A'] else 0.

def main():
    import os,tempfile
    cache=None
    if 'MPLCONFIGDIR' not in os.environ:
        cache=tempfile.TemporaryDirectory(prefix='paper-71-mpl-')
        os.environ['MPLCONFIGDIR']=cache.name
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import Rectangle
    m=solve_model()
    fig,axes=plt.subplots(1,3,figsize=(11.2,6.5),dpi=100,facecolor='white')
    ax=axes[0];r=m['a']/m['B']
    ax.add_patch(Rectangle((0,-1.25),1,1.25+r,color='#9bc5e8'))
    ax.add_patch(Rectangle((0,r),1,1-r,color='#dbedf5'))
    ax.add_patch(Rectangle((0,1),1,.8,color='#eaf3fb'))
    ax.axhline(0,color='#666',ls=':',lw=1);ax.axhline(r,color='#2786a8',lw=2);ax.axhline(1,color='#b44b35',lw=2)
    ax.text(.5,1.45,'Fresh water\n$T=T_m$, $C=0$',ha='center')
    ax.text(.5,.53,'Pure ice\n$C=0$\n$T_i\\leq T\\leq T_m$',ha='center')
    ax.text(.5,-.65,'Diluted brine near ice\nFar below:\n$T\\to T_\\infty$, $C\\to C_0$',ha='center')
    ax.annotate('freezing: $b(t)$',xy=(1,1),xytext=(.25,1.08),fontsize=10)
    ax.annotate('melting: $a(t)>0$',xy=(1,r),xytext=(.12,-.2),fontsize=10)
    ax.annotate('',xy=(1.07,1.3),xytext=(1.07,1.02),arrowprops=dict(arrowstyle='->',color='#b44b35',lw=2))
    ax.annotate('',xy=(1.07,r+.17),xytext=(1.07,r+.01),arrowprops=dict(arrowstyle='->',color='#2786a8'))
    ax.text(.02,-.08,'initial contact $x=0$',fontsize=9,color='#555')
    ax.set(xlim=(-.03,1.12),ylim=(-1.25,1.8),xticks=[],yticks=[],title='Layers and moving boundaries')
    ax.text(.5,-1.42,'Layer cartoon, not a common scale',ha='center',fontsize=9)
    ax=axes[1];us=np.linspace(-2,.065,700);vals=[temperature(float(u),m) for u in us]
    ax.plot(vals,us,color='#b44b35',lw=2)
    ax.axhline(m['a'],color='#2786a8',ls='--',lw=1);ax.axhline(m['B'],color='#b44b35',ls='--',lw=1)
    ax.set(xlabel='$(T-T_m)/\\Delta T$',ylabel='$x/(2\\sqrt{\\kappa t})$',title='Temperature field',xlim=(-1.06,.05),ylim=(-2,.065))
    ax.grid(alpha=.2)
    ins=ax.inset_axes([.51,.15,.43,.33]);ui=np.linspace(m['a'],m['B'],100)
    ins.plot([temperature(float(u),m) for u in ui],ui/m['B'],color='#b44b35')
    ins.set(xlabel='$(T-T_m)/\\Delta T$',ylabel='$x/b$',title='Ice: enlarged',xlim=(-m['theta']*1.2,.001),ylim=(0,1.04))
    ins.tick_params(labelsize=8);ins.xaxis.label.set_size(8);ins.yaxis.label.set_size(8);ins.title.set_size(9)
    ax=axes[2];vs=np.linspace(-3,m['A'],600)
    ax.plot([concentration(float(v),m) for v in vs],vs,color='#2786a8',lw=2)
    ax.plot([m['c'],0],[m['A'],m['A']],color='#2786a8',lw=1)
    ax.plot([0,0],[m['A'],m['A']+.6],color='#2786a8')
    ax.axhline(m['A'],color='#2786a8',ls='--',lw=1)
    ax.annotate('$C_i/C_0=%.4f$'%m['c'],xy=(m['c'],m['A']),xytext=(.12,m['A']+.2),fontsize=10)
    ax.set(xlabel='$C/C_0$',ylabel='$x/(2\\sqrt{Dt})$',title='Salinity field',xlim=(-.04,1.05),ylim=(-3,m['A']+.6))
    ax.grid(alpha=.2)
    fig.suptitle('Ice freezes into fresh water while its lower surface melts into brine',fontsize=13)
    fig.text(.5,.025,'Illustrative exact similarity solution: $S=40$, $\\epsilon=2.5\\times10^{-4}$, $R=mC_0/\\Delta T=2$. Profile panels have different diffusion scales.',ha='center',fontsize=10)
    fig.subplots_adjust(left=.045,right=.97,bottom=.16,top=.88,wspace=.45)
    fig.savefig(Path('paper-71-fields.png'),dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
    if cache:cache.cleanup()

if __name__=='__main__':main()
