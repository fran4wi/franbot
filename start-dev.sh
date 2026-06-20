#!/bin/bash
cd $HOME/repos/franbot-dev
git restore .
git pull && $HOME/.local/bin/uv run app.py
