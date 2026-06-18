#!/bin/bash
cd /home/shinysocks/fran4wi-slackbot
git restore .
git pull && /home/shinysocks/.local/bin/uv run app.py
