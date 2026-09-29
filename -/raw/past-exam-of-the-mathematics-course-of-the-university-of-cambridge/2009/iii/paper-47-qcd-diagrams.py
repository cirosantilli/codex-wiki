"""Born and first-QCD-correction diagrams; Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Write the opaque PNG basename to the caller CWD; preserve caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def line(ax, p, q, forward=True):
    p, q = np.array(p), np.array(q)
    ax.plot([p[0], q[0]], [p[1], q[1]], color="#253442", linewidth=1.55)
    first, second = (p, q) if forward else (q, p)
    a = first + 0.42 * (second-first)
    z = first + 0.60 * (second-first)
    ax.annotate("", xy=z, xytext=a, arrowprops={"arrowstyle": "-|>", "color": "#253442", "lw": 1.2, "mutation_scale": 10})


def boson(ax, p, q, gluon=False, bend=0.0):
    p, q = np.array(p), np.array(q)
    vector = q-p
    unit = vector / np.linalg.norm(vector)
    normal = np.array([-unit[1], unit[0]])
    t = np.linspace(0, 1, 300)
    envelope = np.sin(np.pi*t)**0.5
    base = p + t[:, None]*vector + (bend*np.sin(np.pi*t))[:, None]*normal
    path = base + (0.045*np.sin(12*np.pi*t)*envelope)[:, None]*normal
    if gluon:
        path += (0.021*np.cos(12*np.pi*t)*envelope)[:, None]*unit
    ax.plot(path[:, 0], path[:, 1], color="#b56017" if gluon else "#226eb0", linewidth=1.6)


def cross(ax, p):
    p = np.array(p)
    for offset in (np.array([0.07, 0.07]), np.array([0.07, -0.07])):
        ax.plot([p[0]-offset[0], p[0]+offset[0]], [p[1]-offset[1], p[1]+offset[1]], color="#a82239", lw=2)


def diagram(ax, kind, title):
    electron, positron = (0.0, 0.75), (0.0, -0.75)
    left, vertex = (0.72, 0.0), np.array([1.65, 0.0])
    quark, anti = np.array([3.15, 0.85]), np.array([3.15, -0.85])
    line(ax, electron, left)
    line(ax, positron, left, False)
    boson(ax, left, vertex)
    line(ax, vertex, quark)
    line(ax, vertex, anti, False)
    ax.text(-0.13, 0.83, r"$e^-$", fontsize=11)
    ax.text(-0.13, -0.93, r"$e^+$", fontsize=11)
    ax.text(1.05, 0.17, r"$\gamma^*$", fontsize=11)
    ax.text(3.22, 0.78, r"$q$", fontsize=11)
    ax.text(3.22, -0.95, r"$\bar q$", fontsize=11)
    if kind in ("real_q", "real_anti"):
        end = quark if kind == "real_q" else anti
        point = vertex + .43*(end-vertex)
        gend = np.array([3.18, 0.03 if kind == "real_q" else -0.03])
        boson(ax, point, gend, True)
        ax.text(3.23, gend[1]-0.03, r"$g$", fontsize=11)
        ax.plot(*point, "o", ms=3, color="#253442")
    elif kind == "vertex":
        p = vertex+.50*(quark-vertex)
        q = vertex+.50*(anti-vertex)
        boson(ax, p, q, True, .32)
    elif kind in ("self_q", "self_anti"):
        end = quark if kind == "self_q" else anti
        p = vertex+.28*(end-vertex)
        q = vertex+.74*(end-vertex)
        boson(ax, p, q, True, .31 if kind == "self_q" else -.31)
    elif kind == "ct_vertex":
        cross(ax, vertex)
    elif kind in ("ct_q", "ct_anti"):
        end = quark if kind == "ct_q" else anti
        cross(ax, vertex+.52*(end-vertex))
    ax.set_title(title, fontsize=12, pad=10)
    ax.set_xlim(-.28, 3.55)
    ax.set_ylim(-1.18, 1.18)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    entries = [("born", "Born: photon-mediated quark pair"),
               ("real_q", "Real emission from the quark"),
               ("real_anti", "Real emission from the antiquark"),
               ("vertex", "Virtual gluon vertex correction"),
               ("self_q", "Quark self-energy / external-leg factor"),
               ("self_anti", "Antiquark self-energy / external-leg factor"),
               ("ct_vertex", "Local vertex counterterm"),
               ("ct_q", "Quark field counterterm"),
               ("ct_anti", "Antiquark field counterterm")]
    fig, axes = plt.subplots(3, 3, figsize=(14.4, 10.0), dpi=100, facecolor="white")
    for ax, (kind, title) in zip(axes.flat, entries):
        diagram(ax, kind, title)
    fig.suptitle("Inclusive hadron production: Born and first QCD correction", fontsize=17, y=.975)
    fig.text(.5, .024, "Blue wavy lines: photons. Orange curled lines: gluons. Crosses: local counterterms.\nSelf-energy panels represent the external-state normalization contributions, not additional final particles.", ha="center", va="center", fontsize=11)
    fig.subplots_adjust(left=.025, right=.975, bottom=.08, top=.92, hspace=.42, wspace=.18)
    fig.savefig(Path.cwd()/"paper-47-qcd-diagrams.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
