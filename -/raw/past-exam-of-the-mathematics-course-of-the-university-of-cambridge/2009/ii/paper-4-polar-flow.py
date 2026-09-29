"""Sinusoidal radial flow and its homoclinic basin boundary.
Python 3.14; NumPy/Matplotlib. Writes paper-4-polar-flow.png to CWD.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
h=-0.001
theta=np.pi
w=1.0
angles=[theta]
values=[w]
def rhs(t,w): return (1-2*np.sin(t))*w-1
for _ in range(7000):
    k1=rhs(theta,w)
    k2=rhs(theta+h/2,w+h*k1/2)
    k3=rhs(theta+h/2,w+h*k2/2)
    k4=rhs(theta+h,w+h*k3)
    nw=w+h*(k1+2*k2+2*k3+k4)/6
    nt=theta+h
    if nw<1 and theta<0:
        root=theta+h*(w-1)/(w-nw)
        angles.append(root)
        values.append(1.0)
        break
    theta,w=nt,nw
    angles.append(theta)
    values.append(w)
else: raise RuntimeError("No homoclinic endpoint found")
a=np.array(angles)
r=1-1/np.array(values)
assert np.min(r)>-1e-10 and np.max(r)<1
x,y=r*np.cos(a),r*np.sin(a)
fig,ax=plt.subplots(figsize=(6.5,6.3),facecolor="white")
ax.set_facecolor("white")
ax.fill(x,y,color="#f6dcc4",alpha=0.8,label="Basin attracted to origin")
axis=np.linspace(-1.3,1.3,161)
xx,yy=np.meshgrid(axis,axis)
rr=np.hypot(xx,yy)
cs=np.divide(xx,rr,out=np.zeros_like(xx),where=rr>0)
ss=np.divide(yy,rr,out=np.zeros_like(yy),where=rr>0)
rdot=rr*(1-rr)*(rr-2*ss)
xd=rdot*cs-rr*rr*ss
yd=rdot*ss+rr*rr*cs
ax.streamplot(axis,axis,xd,yd,color="#999999",density=0.85,linewidth=0.6,arrowsize=0.9)
circle=np.linspace(0,2*np.pi,501)
ax.plot(np.cos(circle),np.sin(circle),color="#236d9d",lw=2.5,label=r"Stable cycle $r=1$")
ax.plot(x,y,color="#ad6433",lw=2,label="Homoclinic basin boundary")
ax.scatter([0],[0],s=28,color="#222222",zorder=5)
ax.annotate("",xy=(np.cos(0.2),np.sin(0.2)),xytext=(1,0),arrowprops={"arrowstyle":"->","color":"#236d9d","lw":2})
ax.set_aspect("equal")
ax.set_xlim(-1.3,1.3)
ax.set_ylim(-1.3,1.3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Radial flow with $g(\theta)=2\sin\theta$")
ax.legend(loc="lower left",fontsize=8,framealpha=0.95)
fig.tight_layout()
fig.savefig("paper-4-polar-flow.png",dpi=150,facecolor="white",transparent=False)
plt.close(fig)
