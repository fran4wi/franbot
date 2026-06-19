#!/bin/bash
cd /home/shinysocks/franbot-dev
git restore .
git pull && /home/shinysocks/.local/bin/uv run app.py
