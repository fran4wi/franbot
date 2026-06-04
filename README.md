# Slack Bot for Hong Slack

> Slack app example from 📚 [Getting started with Bolt for Python](https://docs.slack.dev/tools/bolt-python/getting-started)

## Overview

This is a Slack app built with the [Bolt for Python framework](https://docs.slack.dev/tools/bolt-python/) that showcases responding to events and interactive buttons.

## File Descriptions

 - `.env.sample`: contains a template for your environment variables. should be renamed to `.env`
 - `sheets_env.json`: gives the service key credentials so a google sheet can be updated.
 - `app.py`: entrypoint file.
 - `event_output_examples/`: contains code that isn't used, but is kept solely because it is helpful for getting onboarded into using slack's API.
 - `texts/`: json files with automatic responses to certain events. folder should probably be renamed, but I am lazy.

## Running locally

### 1. Make a slack app
 * Go to [slack's developer workspace](https://api.slack.com/apps?new_app=1).
 * Give it a name and choose where you want to test the app.
 * Then, click "Create App"
 * In the side bar, go to "App Manifest"
 * Copy the manifest.json file that is attached to this repository into the text box. Press "save changes"
 * At the top of the screen, you should be prompted to make an "app level token". Click "click here to generate"
 * Give the token a name. click "generate"
 * Copy the token it gives you. 

 * Now, go to "oauth and permissions". In oauth tokens, click "install to test workspace". 
 * Click "allow"

**Now, you should see it in your workspace**

### 2. Make a google service key
to figure out how, follow the instructions outlined here: [How to create a google workspace service key](https://github.com/expo/fyi/blob/main/creating-google-service-account.md)

### 3. Setup environment variables
 * edit `.env.sample` with your environment variables
 * rename `.env.sample` to `.env`

### 4. Setup your local project
First, ensure that **uv** is installed: [uv-installation](https://docs.astral.sh/uv/getting-started/installation/)

```bash
# Clone this project onto your machine
git clone https://github.com/fran4wi/slack-bot-python

# Change Directory into this project
cd slack-bot-python

# Run the app
uv run app.py
```
## More examples
Looking for more examples of Bolt for Python? Browse to [bolt-python/examples/](https://github.com/slackapi/bolt-python/tree/main/examples) for a long list of usage, server, and deployment code samples!

