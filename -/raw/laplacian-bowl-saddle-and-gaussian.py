"""Original analytic surfaces colored by their Laplacian; PNG goes to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
import numpy as np


def main():
    x = np.linspace(-1.6, 1.6, 101)
    X, Y = np.meshgrid(x, x)
    R2 = X**2 + Y**2
    fields = [R2, X**2-Y**2, np.exp(-R2)]
    laplacians = [np.full_like(R2, 4.), np.zeros_like(R2), 4*(R2-1)*np.exp(-R2)]
    titles = [r"Bowl: $f=x^2+y^2$", r"Saddle: $f=x^2-y^2$", r"Bump: $f=e^{-(x^2+y^2)}$"]
    descriptions = [r"$\Delta f=2+2=4$", r"$\Delta f=2-2=0$", r"$\Delta f=4(r^2-1)e^{-r^2}$"]
    norm = Normalize(vmin=-4, vmax=4)
    cmap = LinearSegmentedColormap.from_list("signed_laplacian", ["#2166ac", "#cccccc", "#b2182b"])
    fig = plt.figure(figsize=(12.8, 5.3), dpi=120, facecolor="white")
    axes = [fig.add_subplot(1, 3, i+1, projection="3d") for i in range(3)]
    for ax, field, laplacian, title in zip(axes, fields, laplacians, titles):
        facecolors = cmap(norm(laplacian))
        if ax is axes[2]:
            facecolors[np.abs(R2-1)<.055] = [0.12, 0.12, 0.12, 1.]
        ax.plot_surface(X, Y, field, facecolors=facecolors,
                        rcount=101, ccount=101, linewidth=0, antialiased=False, shade=False)
        ax.set(xlabel=r"$x$", ylabel=r"$y$", zlabel=r"$f(x,y)$",
               xlim=(-1.6, 1.6), ylim=(-1.6, 1.6))
        ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
        ax.tick_params(labelsize=9, pad=0)
        ax.set_title(title, fontsize=13, pad=8)
        ax.view_init(elev=26, azim=-55)
        ax.set_box_aspect((1, 1, .8))
        for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
            axis.pane.set_facecolor("white")
    fig.suptitle("The Laplacian adds second derivatives in perpendicular directions",
                 fontsize=17, weight="bold", y=.96)
    for center, formula, explanation in zip([.177, .482, .787], descriptions,
            ["Positive in every location", "Zero despite the saddle shape", "Negative core; positive outside the black circle"]):
        fig.text(center, .19, formula, ha="center", fontsize=14)
        fig.text(center, .135, explanation, ha="center", fontsize=10.5)
    cax = fig.add_axes([.93, .30, .015, .40])
    bar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax)
    bar.set_label(r"Color: $\Delta f$", fontsize=12)
    bar.set_ticks([-4, 0, 4])
    fig.text(.5, .045, "Height shows the field; color shows its Laplacian. Vertical scales differ between panels.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.01, right=.905, top=.82, bottom=.26, wspace=.02)
    fig.savefig(Path(__file__).stem+".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
