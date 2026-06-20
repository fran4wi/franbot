#!/bin/bash
cd $HOME/franbot
git restore .
git pull && $HOME/.local/bin/uv run app.py
