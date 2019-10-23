#!/usr/bin/env bash

# Run all commands here to set up Jupyter Lab for Plotly:
# https://plot.ly/python/getting-started/

export NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.0 --no-build
jupyter labextension install jupyterlab-plotly@1.1.0 --no-build
jupyter labextension install plotlywidget@1.1.0 --no-build
jupyter labextension install jupyterlab-chart-editor --no-build
jupyter lab build
unset NODE_OPTIONS
