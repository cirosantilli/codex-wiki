from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.5,4.7));a,b=3.,2.;f=np.sqrt(a*a-b*b);A=np.array([-f,0.]);B=np.array([f,0.]);theta=np.linspace(0,2*np.pi,500)
for aa in [ax,bx]:
 aa.plot(a*np.cos(theta),b*np.sin(theta),color="#234e70",lw=1.8);aa.scatter([-f,f],[0,0],color="#a74835",s=25,zorder=4);aa.text(-f,-.32,"A",ha="center");aa.text(f,-.32,"B",ha="center");aa.set(xlim=(-3.65,3.65),ylim=(-2.6,2.6),aspect="equal");aa.axis("off")
t=.88;P=np.array([a*np.cos(t),b*np.sin(t)]);ua=(P-A)/np.linalg.norm(P-A);ub=(P-B)/np.linalg.norm(P-B);n=(ua+ub)/np.linalg.norm(ua+ub);tangent=np.array([-n[1],n[0]])
ax.plot([A[0],P[0],B[0]],[A[1],P[1],B[1]],color="#287b65",lw=1.8)
ax.plot([P[0]-tangent[0],P[0]+tangent[0]],[P[1]-tangent[1],P[1]+tangent[1]],color="#bb5039",lw=1.5)
ax.annotate("",xy=P+.65*n,xytext=P-.5*n,arrowprops=dict(arrowstyle="->",color="#777777",lw=1.4));ax.text(*(P+.75*n),"Normal",fontsize=10,ha="center");ax.text(*(P-.95*tangent),"Tangent",fontsize=10,color="#bb5039");ax.text(P[0]-.15,P[1]+.13,"P",fontsize=12)
ax.set_title(r"$\nabla(r_A+r_B)=\mathbf{u}_A+\mathbf{u}_B$",fontsize=13)
for t in [.28,.7,1.2,1.8,2.5,3.5,4.4,5.3,5.9]:
 P=np.array([a*np.cos(t),b*np.sin(t)]);bx.plot([A[0],P[0]],[A[1],P[1]],color="#277c65",lw=1,alpha=.65);bx.plot([P[0],B[0]],[P[1],B[1]],color="#b44c39",lw=1,alpha=.65)
bx.set_title("Every reflected in-plane path reaches B",fontsize=12)
fig.text(.5,.035,"All A–P–B path lengths equal 2a; focusing is shown in the geometrical-optics approximation.",ha="center",fontsize=10)
fig.subplots_adjust(left=.02,right=.98,bottom=.1,top=.88,wspace=.12)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
