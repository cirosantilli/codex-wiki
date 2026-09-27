"""Original optical layout; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired output directory. Dimensions and conics are illustrative;
the Ritchey–Chrétien sketch is not an optimized aplanatic prescription.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/2018-paper-338-mpl-cache')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
KIND = 'schmidt'
fig, ax = plt.subplots(figsize=(11,4),dpi=100,facecolor='white')
fig.subplots_adjust(left=.025,right=.985,top=.88,bottom=.08)
blue='#1764a0'; orange='#cf7000'; red='#ba2434'
ax.set_xlim(-.1,12.9);ax.set_ylim(-3.0,3.65);ax.set_aspect('equal');ax.axis('off')
ax.plot([0,12.4],[0,0],'--',color='#888',lw=1)
ax.text(.1,-.36,'optical axis',color='#666',fontsize=10)
def rays(points):
    for a,b in zip(points[:-1],points[1:]):
        a=np.asarray(a);b=np.asarray(b)
        ax.plot([a[0],b[0]],[a[1],b[1]],color=orange,lw=2)
        u=a+.47*(b-a);v=a+.58*(b-a)
        ax.annotate('',xy=v,xytext=u,arrowprops={'arrowstyle':'->','color':orange,'lw':1.5})
def label(text,xy,pos):
    ax.annotate(text,xy=xy,xytext=pos,fontsize=10,ha='center',arrowprops={'arrowstyle':'-','color':'#555'})
def primary(shape,hole=False):
    for a,b in ([(-2.5,-.45),(.45,2.5)] if hole else [(-2.5,2.5)]):
        yy=np.linspace(a,b,160);ax.plot(shape(yy),yy,color=blue,lw=4)
def focus(F,horizontal=False):
    if horizontal:ax.plot([F[0]-.45,F[0]+.45],[F[1],F[1]],color=red,lw=3)
    else:ax.plot([F[0],F[0]],[F[1]-.45,F[1]+.45],color=red,lw=3)
y0=2.; f=4.;F1=np.array([6.,0.]);F2=np.array([11.5,0.])
parabola=lambda y:10-y*y/(4*f)
P=np.array([parabola(y0),y0])
if KIND=='newtonian':
    primary(parabola)
    slope=y0/(P[0]-F1[0]);xs=(9+6*slope)/(1+slope);S=np.array([xs,9-xs]);F=np.array([9.,3.])
    yy=np.linspace(-1.25,1.25,80);ax.plot(9-yy,yy,color=blue,lw=3)
    focus(F,True);rays([[0,y0],P,S,F]);ax.plot([9,9],[0,3],'--',color='#888',lw=1)
    label('concave parabolic primary',(9.6,-2.3),(8,-2.6))
    label('flat 45° secondary',S,(6.25,3.05))
    label('side focal plane',F,(11.2,3.1))
elif KIND in ('cassegrain','ritchey-chretien'):
    if KIND=='ritchey-chretien':
        k=-1.15;c=1/8
        shape=lambda y:10-c*y*y/(1+np.sqrt(1-(1+k)*c*c*y*y))
        P=np.array([shape(y0),y0]);sp=c*y0/np.sqrt(1-(1+k)*c*c*y0*y0)
        normal=np.array([1.,sp]);normal/=np.linalg.norm(normal)
        outgoing=np.array([1.,0.])-2*normal[0]*normal
        F1=np.array([P[0]-P[1]*outgoing[0]/outgoing[1],0.])
        primary(shape,True)
    else:primary(parabola,True)
    xs=7.7;S=F1+(xs-F1[0])/(P[0]-F1[0])*(P-F1)
    centre=(F1[0]+F2[0])/2;c=(F2[0]-F1[0])/2
    a=abs(np.linalg.norm(S-F2)-np.linalg.norm(S-F1))/2;b=np.sqrt(c*c-a*a)
    yy=np.linspace(-1.15,1.15,120);xx=centre-a*np.sqrt(1+yy*yy/(b*b));ax.plot(xx,yy,color=blue,lw=4)
    focus(F2);rays([[0,y0],P,S,F2])
    label('convex hyperbolic secondary',S,(5.25,3.0))
    label('concave '+('hyperbolic' if KIND=='ritchey-chretien' else 'parabolic')+' primary',(9.6,-2.25),(8.8,-2.6))
    label('focal plane\nbehind primary',F2,(11.55,2.7))
    ax.text(10.55,-.7,'primary hole',fontsize=9,ha='center')
elif KIND=='gregorian':
    primary(parabola,True)
    xs=4.4;S=F1+(xs-F1[0])/(P[0]-F1[0])*(P-F1)
    centre=(F1[0]+F2[0])/2;c=(F2[0]-F1[0])/2
    a=(np.linalg.norm(S-F2)+np.linalg.norm(S-F1))/2;b=np.sqrt(a*a-c*c)
    yy=np.linspace(-1.2,1.2,120);xx=centre-a*np.sqrt(1-yy*yy/(b*b));ax.plot(xx,yy,color=blue,lw=4)
    focus(F2);rays([[0,y0],P,F1,S,F2]);ax.plot(*F1,'x',color=red,ms=7)
    label('concave ellipsoidal secondary',S,(3.2,-2.5))
    label('intermediate focus',F1,(6.3,-1.9))
    label('concave parabolic primary',(9.6,-2.25),(9.0,-2.65))
    label('final focal plane',F2,(11.3,2.8))
elif KIND=='schmidt':
    C=np.array([2.,0.]);R=8.;F=np.array([6.,0.]);entry=np.array([2.,2.])
    primary(lambda y:2+np.sqrt(64-y*y))
    def trace(theta):
        d=np.array([np.cos(theta),np.sin(theta)])
        t=-2*np.sin(theta)+np.sqrt(64-4*np.cos(theta)**2)
        hit=entry+t*d;n=(hit-C)/R;out=d-2*np.dot(d,n)*n
        return hit,out
    def err(theta):
        hit,out=trace(theta);v=F-hit;return out[0]*v[1]-out[1]*v[0]
    lo=-.15;hi=.15
    assert err(lo)*err(hi)<0
    for _ in range(80):
        mid=(lo+hi)/2
        if err(lo)*err(mid)<=0:hi=mid
        else:lo=mid
    P,out=trace((lo+hi)/2);assert np.dot(out,F-P)>0
    yy=np.linspace(-2.5,2.5,140);xx=2+.10*(yy/2.5)**4
    ax.plot(xx,yy,color=blue,lw=3);ax.plot(xx-.07,yy,color=blue,lw=1)
    yy=np.linspace(-1.15,1.15,100);ax.plot(2+np.sqrt(16-yy*yy),yy,color=red,lw=3)
    rays([[0,y0],entry,P,F]);ax.plot(*C,'o',color='#666',ms=4)
    label('aspheric corrector + stop\nat centre of curvature',entry,(3.05,2.98))
    label('concave spherical primary',(9.6,-2.2),(9,-2.65))
    label('curved focal surface',F,(6.0,-2.4))
    ax.text(6.1,.45,'internal camera',fontsize=9)
ax.text(.1,2.4,'parallel marginal ray',color=orange,fontsize=10)
ax.set_title({'newtonian':'Newtonian','cassegrain':'Classical Cassegrain','ritchey-chretien':'Ritchey–Chrétien','gregorian':'Gregorian','schmidt':'Classical Schmidt'}[KIND]+' — schematic, not to scale',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
