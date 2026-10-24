"""Original piston wave sketches. Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7.
Representative gamma=1.4, c0=1 and U=+/-0.5. Run from output directory.
Dependencies in wiki pyproject.toml. Curved C-minus rays use RK4 for drawing only.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(11.5,5.2),constrained_layout=True)
gamma=1.4;c0=1.;T=2.;time=np.linspace(0,T,301)
U=.5;V=(gamma+1)*U/4+np.sqrt(c0*c0+((gamma+1)*U/4)**2);ratio=V/(V-U);p_ratio=1+gamma*V*U;c1=np.sqrt(p_ratio/ratio)
ax=axes[0];ax.fill_betweenx(time,U*time,V*time,color='#e6f0f7')
ax.plot(U*time,time,color='black',lw=2,label='piston');ax.plot(V*time,time,color='#b63232',lw=2,label='shock')
for tb in [.15,.35,.6,.9,1.2]:
    ts=c1*tb/(U+c1-V);tt=np.linspace(tb,min(ts,T),80);xx=U*tb+(U+c1)*(tt-tb);ax.plot(xx,tt,color='#276d9b',lw=1)
for x0 in [.15,.3,.5,.8,1.2]:
    ts=x0/(V-c0);tt=np.linspace(0,min(ts,T),80);ax.plot(x0+c0*tt,tt,color='#276d9b',lw=1)
for x0 in [.4,.9,1.4,2.]:
    ts=x0/(V+c0);tt=np.linspace(0,min(ts,T),50);ax.plot(x0-c0*tt,tt,'--',color='#888888',lw=.8)
    if ts<T:
        tend=(V-U+c1)*ts/c1;tt=np.linspace(ts,min(tend,T),50);ax.plot(V*ts+(U-c1)*(tt-ts),tt,'--',color='#888888',lw=.8)
ax.set(title=r'Advancing piston: compressive shock ($U=0.5$)',xlim=(0,3.5))
U=-.5;c1=c0+(gamma-1)*U/2;tail=U+c1
ax=axes[1];ax.fill_betweenx(time,tail*time,c0*time,color='#deedf8')
ax.plot(U*time,time,color='black',lw=2,label='piston')
for speed in np.linspace(tail,c0,9):ax.plot(speed*time,time,color='#276d9b',lw=1)
ax.plot(tail*time,time,color='#b63232',lw=1.8,label='fan edges');ax.plot(c0*time,time,color='#b63232',lw=1.8)
def minus_speed(t,x):
    if t<=0 or x/t>=c0:return -c0
    if x/t<=tail:return U-c1
    z=x/t;u=2*(z-c0)/(gamma+1);c=(2*c0+(gamma-1)*z)/(gamma+1);return u-c
for x0 in [.4,.8,1.2,1.8,2.4]:
    dt=.002;tt=[0.];xx=[x0]
    for _ in range(int(T/dt)):
        t=tt[-1];x=xx[-1];a=minus_speed(t,x);b=minus_speed(t+dt/2,x+dt*a/2);c=minus_speed(t+dt/2,x+dt*b/2);d=minus_speed(t+dt,x+dt*c);xn=x+dt*(a+2*b+2*c+d)/6
        if xn<U*(t+dt):break
        tt.append(t+dt);xx.append(xn)
    ax.plot(xx,tt,'--',color='#888888',lw=.8)
ax.set(title=r'Receding piston: rarefaction ($U=-0.5$)',xlim=(-1.2,3.0))
for ax in axes:
    ax.set(ylim=(0,T),xlabel='$x$',ylabel='$t$');ax.grid(alpha=.12);ax.legend(loc='upper right',fontsize=8)
fig.savefig('2009-piston-characteristics.png',dpi=150,facecolor='white')
