"""Generate kaplan-meier-censored-cohort.png in CWD; Python 3.14, Matplotlib.

Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
Compute tied and untied steps with exact rational arithmetic.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt


COHORT = [("A", 1, True), ("B", 2, False), ("C", 3, True),
          ("D", 3, True), ("E", 3, False), ("F", 5, False)]


def steps(cohort, all_exits_are_events=False):
    survival = Fraction(1)
    result = []
    for time in sorted({record[1] for record in cohort}):
        at_risk = sum(exit_time >= time for _, exit_time, _ in cohort)
        events = sum(exit_time == time and (observed or all_exits_are_events)
                     for _, exit_time, observed in cohort)
        censored = sum(exit_time == time and not observed
                       for _, exit_time, observed in cohort)
        survival *= Fraction(at_risk - events, at_risk)
        result.append((time, at_risk, events, censored, survival))
    return result


def draw_curve(ax, rows, color, label, linestyle="-", marks=True):
    ax.step([0] + [row[0] for row in rows],
            [1] + [float(row[4]) for row in rows], where="post",
            color=color, lw=2.6, linestyle=linestyle, label=label)
    if marks:
        for time, _, _, censored, survival in rows:
            if censored:
                ax.plot(time, float(survival), marker="|", ms=12,
                        markeredgewidth=2, color=color)


def main():
    tied = steps(COHORT)
    untied_cohort = [(name, 4 if name == "D" else time, event)
                    for name, time, event in COHORT]
    untied = steps(untied_cohort)
    wrong = steps(COHORT, all_exits_are_events=True)
    assert [(n, d, c) for _, n, d, c, _ in tied] == [
        (6, 1, 0), (5, 0, 1), (4, 2, 1), (1, 0, 1)]
    assert tied[-1][4] == Fraction(5, 12)
    assert [row[4] for row in untied] == [
        Fraction(5, 6), Fraction(5, 6), Fraction(5, 8),
        Fraction(5, 16), Fraction(5, 16)]
    assert [row[4] for row in wrong] == [
        Fraction(5, 6), Fraction(2, 3), Fraction(1, 6), Fraction(0)]

    fig = plt.figure(figsize=(11.4, 6.3), dpi=110, facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=(0.78, 1.25),
                           height_ratios=(3.4, 1), hspace=0.38, wspace=0.28)
    histories = fig.add_subplot(grid[0, 0])
    curve = fig.add_subplot(grid[0, 1])
    table_ax = fig.add_subplot(grid[1, 1])
    notes = fig.add_subplot(grid[1, 0])
    blue, orange, gray = "#007c83", "#b35422", "#747474"
    for row, (name, time, event) in enumerate(COHORT):
        y = 5 - row
        histories.plot([0, time], [y, y], color=blue, lw=2.5)
        histories.plot(time, y, "o" if event else "|", color=blue,
                       ms=7 if event else 13, markeredgewidth=2)
    histories.set(yticks=range(6), yticklabels=list("FEDCBA"),
                  ylim=(-0.6, 5.6), title="Original observed histories",
                  xlabel="Follow-up (years)", ylabel="Subject")
    histories.plot([], [], "o", color=blue, label="Observed event")
    histories.plot([], [], "|", ms=12, markeredgewidth=2, color=blue,
                   label="Right censoring")
    histories.legend(loc="upper right", fontsize=9, frameon=True)
    draw_curve(curve, tied, blue, "Tied events at year 3")
    draw_curve(curve, untied, orange, "D's event moved to year 4", "--")
    draw_curve(curve, wrong, gray, "Wrong: censoring counted as events", ":",
               marks=False)
    curve.set(title="Product-limit steps; ticks mark censoring",
              ylabel="Estimated survival probability", xlabel="Time (years)",
              ylim=(-0.04, 1.08), yticks=[0, 0.25, 0.5, 0.75, 1])
    curve.annotate("5/12", (4.6, 5 / 12), xytext=(4.3, 0.58),
                   fontsize=11, color=blue,
                   arrowprops={"arrowstyle": "->", "color": blue})
    curve.text(4.2, 0.25, "5/16", color=orange, fontsize=11)
    curve.text(3.55, 0.09, "1/6 (wrong)", color=gray, fontsize=10)
    curve.legend(loc="upper right", fontsize=9, frameon=True)
    for ax in (histories, curve):
        ax.set(xlim=(-0.05, 5.15), xticks=range(6), facecolor="white")
        ax.grid(axis="x", color="#e6e6e6", lw=0.7)
        ax.spines[["top", "right"]].set_visible(False)
        ax.title.set_fontsize(11)
    table_ax.axis("off")
    table = table_ax.table(
        cellText=[["Year", "1", "2", "3", "5"],
                  ["At risk before", "6", "5", "4", "1"],
                  ["Events / censored", "1 / 0", "0 / 1", "2 / 1", "0 / 1"],
                  ["Survival after", "5/6", "5/6", "5/12", "5/12"]],
        cellLoc="center", colWidths=[0.36, 0.16, 0.16, 0.16, 0.16],
        bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    for (row, _), cell in table.get_celld().items():
        cell.set_facecolor("#f1f6f6" if row == 0 else "white")
        cell.set_edgecolor("#cccccc")
    notes.axis("off")
    notes.text(0, 0.95,
               "At year 3, E is still in the denominator.\n"
               "Count events before censoring at a tie.\n\n"
               "All curves stop at year 5:\n"
               "the later tail is unobserved.",
               va="top", fontsize=10, linespacing=1.35)
    fig.suptitle("Six subjects: censoring changes later risk sets, not the current step",
                 fontsize=13, y=0.975)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.89, bottom=0.07)
    fig.savefig(Path.cwd() / "kaplan-meier-censored-cohort.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
