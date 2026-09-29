"""Construct noisy polynomial fits and a noiseless control; save basename.png to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Degree selection uses only three-fold CV on the twelve training observations.
The deterministic held-out grid and known target are diagnostics, not selectors.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial


def target(x):
    return 1 + 0.5 * x + 2 * x**2


def experiment():
    degrees = (1, 2, 7)
    x = np.linspace(-1, 1, 12)
    disturbance = np.array([.12, -.17, .10, .18, -.13, .08,
                            -.16, .11, -.08, .15, -.12, .06])
    y = target(x) + disturbance
    # Interleaved folds: each observation is held out exactly once.
    fold = np.arange(x.size) % 3
    cv_errors = []
    models = []
    train_errors = []
    for degree in degrees:
        squared_errors = np.empty(x.size)
        for k in range(3):
            held = fold == k
            assert (~held).sum() > degree
            model = Polynomial.fit(x[~held], y[~held], degree)
            squared_errors[held] = (y[held] - model(x[held]))**2
        cv_errors.append(squared_errors.mean())
        model = Polynomial.fit(x, y, degree)
        models.append(model)
        train_errors.append(np.mean((y - model(x))**2))

    # Lock the degree before constructing/evaluating the final diagnostic points.
    selected_degree = degrees[int(np.argmin(cv_errors))]
    test_x = -1 + 2 * (np.arange(400) + .5) / 400
    assert np.min(np.abs(test_x[:, None] - x[None, :])) > 1e-8
    target_errors = [np.mean((target(test_x) - model(test_x))**2)
                     for model in models]
    controls = {}
    for degree in (2, 7):
        control = Polynomial.fit(x, target(x), degree)
        controls[degree] = (np.mean((target(x) - control(x))**2),
                            np.mean((target(test_x) - control(test_x))**2))
        assert max(controls[degree]) < 1e-27
    assert selected_degree == 2
    assert np.all(np.diff(train_errors) < 0)
    assert target_errors[2] > 20 * target_errors[1]
    return (degrees, x, y, test_x, models, np.array(train_errors),
            np.array(cv_errors), np.array(target_errors), controls)


def main():
    (degrees, x, y, test_x, models, train_errors,
     cv_errors, target_errors, controls) = experiment()
    print("Degree | noisy training MSE | training-only CV MSE | held-out target MSE")
    for degree, train, cv, test in zip(degrees, train_errors, cv_errors, target_errors):
        print(f"{degree:6d} | {train:.12g} | {cv:.12g} | {test:.12g}")
    for degree, (train, test) in controls.items():
        print(f"Noiseless degree {degree}: training MSE {train:.5g}; target MSE {test:.5g}")
    print("Selected degree: 2 (training-only CV)")

    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig = plt.figure(figsize=(10.5, 6.5), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(2, 3, height_ratios=(2.3, 1.35))
    colors = ("#b36a21", "#177b62", "#6c54aa")
    curve_x = np.linspace(-1, 1, 700)
    for column, (degree, model, color) in enumerate(zip(degrees, models, colors)):
        ax = fig.add_subplot(grid[0, column])
        ax.plot(curve_x, target(curve_x), "--", color="#343b42", lw=1.8,
                label="Known target f(x)")
        ax.plot(curve_x, model(curve_x), color=color, lw=2.2, label="Noisy-data fit")
        ax.scatter(x, y, color="#4b5660", s=26, zorder=4, label="Noisy training data")
        shown = np.arange(12, 400, 25)
        ax.scatter(test_x[shown], target(test_x[shown]), marker="v", s=30,
                   facecolors="white", edgecolors="#7a858f", zorder=3,
                   label="Held-out target points")
        ax.set(xlabel="Predictor x", ylabel="Response", xlim=(-1.05, 1.05),
               ylim=(.55, 3.8), title=f"Degree {degree}" +
               (" — selected by CV" if degree == 2 else ""))
        ax.grid(alpha=.16)
        if column == 0:
            ax.legend(loc="upper center", fontsize=8.5)

    table_ax = fig.add_subplot(grid[1, :])
    table_ax.axis("off")
    table = table_ax.table(
        cellText=[[f"{value:.6f}" for value in values]
                  for values in (train_errors, cv_errors, target_errors)],
        rowLabels=["Noisy training MSE", "Training-only three-fold CV MSE",
                   "Held-out noiseless-target MSE"],
        colLabels=[f"Degree {degree}" for degree in degrees],
        cellLoc="center", rowLoc="left", bbox=(.40, .29, .59, .66))
    table.auto_set_font_size(False)
    table.set_fontsize(10.5)
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor("#d5dbe0")
        if column == 1:
            cell.set_facecolor("#e9f5ee")
    table_ax.text(.5, .12, "Noiseless control: degrees 2 and 7 reproduce f(x); both MSEs < 10⁻²⁷.",
                  ha="center", va="center", transform=table_ax.transAxes, fontsize=11)
    fig.suptitle("Better fit to noisy observations can mean worse recovery of the target", fontsize=14)
    fig.supxlabel("Constructed demonstration • 12 training points • 400 separate target points • no test-based tuning",
                  fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
