"""Oxford A10 (2014): mapped ellipse flow and its stagnation points.

Writes 2014-ellipse-flow.png in the process CWD.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies: repository root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, U, alpha = .65, 1., np.pi/6
    A, B = 1+a*a, 1-a*a
    x = np.linspace(-3.3,3.3,650)
    y = np.linspace(-2.2,2.2,440)
    X,Y = np.meshgrid(x,y)
    Z = X+1j*Y
    discriminant = np.sqrt(Z*Z-4*a*a+0j)
    first, second = (Z+discriminant)/2, (Z-discriminant)/2
    zeta = np.where(abs(first)>=abs(second),first,second)
    psi = np.imag(U*(np.exp(-1j*alpha)*zeta+np.exp(1j*alpha)/zeta))
    psi = np.ma.masked_where((X/A)**2+(Y/B)**2 <= 1.003,psi)
    fig,ax = plt.subplots(figsize=(7.3,4.9),facecolor="white")
    ax.contour(X,Y,psi,levels=np.arange(-2.8,2.81,.2),colors="#176b93",linewidths=.9)
    theta=np.linspace(0,2*np.pi,600)
    ax.fill(A*np.cos(theta),B*np.sin(theta),facecolor="#e6e9ec",edgecolor="#37474f",lw=1.6,zorder=3)
    stag=np.array([1,-1])*(A*np.cos(alpha)+1j*B*np.sin(alpha))
    ax.plot(stag.real,stag.imag,"o",color="#b4591c",ms=6,zorder=4)
    ax.annotate(r"$\theta=\alpha$",xy=(stag[0].real,stag[0].imag),xytext=(1.7,.85),
                arrowprops={"arrowstyle":"->","color":"#b4591c"},color="#b4591c",fontsize=11)
    ax.annotate("",xy=(-1.8,-1.0),xytext=(-2.8,-1.0-np.tan(alpha)),
                arrowprops={"arrowstyle":"->","color":"#b4591c","lw":2})
    ax.text(-2.95,-1.85,r"$U=1,\ \alpha=30^\circ$",color="#b4591c",fontsize=11)
    ax.set(xlim=(-3.3,3.3),ylim=(-2.2,2.2),aspect="equal",xlabel="$x$",ylabel="$y$",
           title="Joukowski ellipse: oblique uniform flow")
    ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig("2014-ellipse-flow.png",dpi=155,facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
