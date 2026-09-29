"""Original complete-linkage example; Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Output the basename PNG to CWD; respect the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

POINTS = np.array([[0.,0.], [.25,.20], [2.,.15], [2.25,-.10], [1.,2.5], [1.20,2.70]])

def complete_linkage(points):
    distances = np.linalg.norm(points[:,None,:]-points[None,:,:], axis=2)
    clusters = {i: [i] for i in range(len(points))}
    merges = []
    while len(clusters) > 1:
        keys = sorted(clusters)
        candidates = [(float(distances[np.ix_(clusters[a],clusters[b])].max()),a,b) for pos,a in enumerate(keys) for b in keys[pos+1:]]
        height,a,b = min(candidates)
        node = len(points)+len(merges)
        merges.append((node,a,b,height))
        clusters[node] = clusters.pop(a)+clusters.pop(b)
    return merges

def main():
    merges = complete_linkage(POINTS)
    children = {node:(a,b) for node,a,b,_ in merges}
    root = merges[-1][0]
    def leaves(node):
        return [node] if node not in children else leaves(children[node][0])+leaves(children[node][1])
    order = leaves(root)
    positions = {node:(i,0.) for i,node in enumerate(order)}
    colors = ["#2369a5", "#cd6325", "#3a8e46"]
    fig, axes = plt.subplots(1,2, figsize=(10.8,4.5), dpi=100, facecolor="white", constrained_layout=True)
    for i, point in enumerate(POINTS):
        axes[0].plot(*point, "o", color=colors[i//2], ms=8)
        axes[0].annotate(chr(65+i), point, xytext=(5,5), textcoords="offset points")
    axes[0].set(xlabel="Coordinate 1", ylabel="Coordinate 2", title="A constructed six-point configuration", xlim=(-.3,2.7), ylim=(-.4,3.1))
    axes[0].set_aspect("equal")
    for node,a,b,height in merges:
        xa,ha = positions[a]
        xb,hb = positions[b]
        axes[1].plot([xa,xa,xb,xb], [ha,height,height,hb], color="#555555", lw=1.8)
        positions[node] = ((xa+xb)/2, height)
    within = max(height for _,a,b,height in merges if a < len(POINTS) and b < len(POINTS))
    between = min(height for _,a,b,height in merges if a >= len(POINTS) or b >= len(POINTS))
    cut = (within+between)/2
    axes[1].axhline(cut, ls="--", color="#b22c35", label="Three-cluster cut")
    axes[1].set(xticks=range(len(POINTS)), xticklabels=[chr(65+i) for i in order], xlabel="Observations", ylabel="Complete-linkage distance", title="Merges computed from these points", ylim=(-.05,merges[-1][3]*1.17))
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "paper-46-clustering-sketch.png", facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
