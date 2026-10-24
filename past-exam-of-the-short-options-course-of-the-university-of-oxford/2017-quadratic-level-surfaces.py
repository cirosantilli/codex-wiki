"""Generate 2017-quadratic-level-surfaces.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(12, 5), dpi=100, facecolor="white")
    theta = np.linspace(0, 2*np.pi, 80)
    for panel, level in enumerate([0, 1, -1], 1):
        ax = fig.add_subplot(1, 3, panel, projection="3d")
        if level == 1:
            angle, z = np.meshgrid(theta, np.linspace(-1.5, 1.5, 60))
            radius = np.sqrt(1+z*z)
            ax.plot_surface(radius*np.cos(angle), radius*np.sin(angle), z, color="#2563eb", alpha=.72, linewidth=0, rcount=45, ccount=55)
        else:
            angle, radius = np.meshgrid(theta, np.linspace(0, 1.65, 55))
            z = radius if level == 0 else np.sqrt(1+radius*radius)
            for sign in [-1, 1]:
                ax.plot_surface(radius*np.cos(angle), radius*np.sin(angle), sign*z, color="#2563eb", alpha=.72, linewidth=0, rcount=45, ccount=55)
        if level == 0:
            ax.scatter([0], [0], [0], color="#b91c1c", s=45, depthshade=False, zorder=10)
            fig.text((panel-.5)/3, .045, "Only singular point: origin", ha="center", color="#b91c1c", fontsize=11)
        else:
            fig.text((panel-.5)/3, .045, "Smooth everywhere", ha="center", fontsize=11)
        label = {0:"Double cone", 1:"One-sheeted hyperboloid", -1:"Two-sheeted hyperboloid"}[level]
        ax.set_title(rf"$\alpha={level}$: "+label, fontsize=11, pad=12)
        ax.set(xlim=(-2,2), ylim=(-2,2), zlim=(-2,2), xlabel="x", ylabel="y", zlabel="z")
        ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);ax.set_zticks([-2,0,2])
        ax.set_box_aspect((1,1,1))
        ax.view_init(elev=18, azim=-55)
    fig.suptitle(r"The level sets $x^2+y^2-z^2=\alpha$", fontsize=17, y=.95)
    fig.subplots_adjust(left=.015, right=.97, top=.82, bottom=.16, wspace=.09)
    fig.savefig("2017-quadratic-level-surfaces.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
