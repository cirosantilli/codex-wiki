"""Generate an idealized event-notification timeline, not measured hardware data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; the opaque matching PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    events = np.array([2, 5, 9])
    polls = np.arange(0, 13, 2)
    detections = polls[np.searchsorted(polls, events, side="left")]
    delays = detections - events
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=110, facecolor="white")
    ax.set_facecolor("white")
    ink, blue, green, orange = "#203040", "#155d8a", "#187355", "#a84b12"
    rows = [(3, "Device events"), (2, "Periodic polls"),
            (1, "Polling detects"), (0, "Ideal interrupt\nnotification")]
    for y, _ in rows:
        ax.hlines(y, -0.2, 12.2, color="#d0d8df", linewidth=1.5)
    for event in events:
        ax.vlines(event, -0.08, 3.08, color="#bbc5cc", linestyle=":", zorder=1)
    ax.scatter(events, np.full(3, 3), s=95, color=blue, zorder=3)
    ax.scatter(polls, np.full(7, 2), s=80, marker="|", linewidths=2.5,
               color=ink, zorder=3)
    ax.scatter(detections, np.full(3, 1), s=95, color=orange, zorder=3)
    ax.scatter(events, np.zeros(3), s=95, marker="D", color=green, zorder=3)
    for event, detect, delay in zip(events, detections, delays):
        ax.text(event, 3.2, str(event), ha="center", color=blue)
        ax.text(detect, 1.16, str(detect), ha="center", color=orange)
        if delay:
            ax.annotate("", xy=(detect, 0.68), xytext=(event, 0.68),
                        arrowprops={"arrowstyle": "<->", "color": orange})
        ax.text((event + detect) / 2, 0.43, f"delay {delay}",
                ha="center", color=orange, fontsize=11)
    ax.set(xlim=(-0.35, 12.35), ylim=(-0.5, 3.65),
           xticks=np.arange(13), yticks=[y for y, _ in rows],
           yticklabels=[label for _, label in rows], xlabel="Time (arbitrary units)")
    ax.tick_params(axis="y", length=0, pad=12)
    for spine in ["top", "left", "right"]:
        ax.spines[spine].set_visible(False)
    ax.set_title("Interrupts versus polling: when is an event noticed?",
                 fontsize=17, weight="bold", color=ink, pad=18)
    fig.text(0.5, 0.115,
             "Pending events persist; an event at a poll time is visible to that poll.",
             ha="center", fontsize=11, color=ink)
    fig.text(0.5, 0.065,
             "Model, not measurement: delivery / dispatch latency, service time and check costs excluded.",
             ha="center", fontsize=10.5, color=ink)
    fig.subplots_adjust(left=0.2, right=0.98, top=0.85, bottom=0.25)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
