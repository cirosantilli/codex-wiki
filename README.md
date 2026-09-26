# Codex Wiki

This repository contains a Codex-generated knowledge written in OurBigBook markup, created with a decent amount of human guidance.

The human readable readme is index.bigb.

The agent guidelines are at AGENTS.md.

Google Analytics 4 can be enabled at deployment time by adding a `googleAnalyticsMeasurementId` property such as `"G-XXXXXXXXXX"` to `ourbigbook.json`. If the property is absent, the generated pages do not load Google Analytics.

Figure generators use the Python environment declared in `pyproject.toml`, tested with Python 3.14.4. To reproduce the figures:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
export MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
find past-exam-of-the-mathematics-course-of-the-university-of-cambridge -name '*.py' -exec python {} \;
```
