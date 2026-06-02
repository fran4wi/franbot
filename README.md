# Getting Started ⚡️ Bolt for Python

> Slack app example from 📚 [Getting started with Bolt for Python](https://docs.slack.dev/tools/bolt-python/getting-started)

## Overview

This is a Slack app built with the [Bolt for Python framework](https://docs.slack.dev/tools/bolt-python/) that showcases responding to events and interactive buttons.

## File Descriptions

.env : has your environment variables. to see what you need, make a copy of .env.example and change the values.

sheets_env.json: gives the service key credentials so a google sheet can be updated.

app.py: entrypoint file.

event_output_examples: has code that isn't used, but is kept solely because it is helpful for getting onboarded into using slack's API.

texts: json files with automatic responses to certain events. folder should probably be renamed, but I am lazy.

attachments: images that are used in this README.md file.

## Running locally

### 0.1 Make a slack app

go to [slack's developer workspace](https://api.slack.com/apps?new_app=1). You should see this:

![make a new slack app](image.png)

give it a name and choose where you want to test the app.

Then, click "Create App"

In the side bar, go to "App Manifest"

![App Manifest page](image-1.png)

copy the manifest.json file that is attached to this repository into the text box. Press "save changes"

![alt text](image-2.png)

At the top of the screen, you should be prompted to make an "app level token". Click "click here to generate"

![alt text](image-3.png)

give the token a name. click "generate"

![alt text](image-4.png)

copy the token it gives you. 

![alt text](image-5.png)

Now, go to "oauth and permissions". In oauth tokens, click "install to test workspace". 

![alt text](image-6.png)

Click "allow"

![alt text](image-7.png)

Now, you should see it in your workspace

![alt text](image-8.png)

### 0.1 Make a google service key

to figure out how, follow the instructions outlined here: [How to create a google workspace service key](https://github.com/expo/fyi/blob/main/creating-google-service-account.md)



### 1. Setup environment variables

```zsh
# Replace with your tokens
export SLACK_BOT_TOKEN=<your-bot-token>
export SLACK_APP_TOKEN=<your-app-level-token>
```

### 2. Setup your local project

```zsh
# Clone this project onto your machine
git clone https://github.com/slack-samples/bolt-python-getting-started-app.git

# Change into this project
cd bolt-python-getting-started-app/

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

### 3. Start servers

```zsh
python3 app.py
```

## More examples

Looking for more examples of Bolt for Python? Browse to [bolt-python/examples/](https://github.com/slackapi/bolt-python/tree/main/examples) for a long list of usage, server, and deployment code samples!

## Contributing

### Issues and questions

Found a bug or have a question about this project? We'd love to hear from you!

1. Browse to [slackapi/bolt-python/issues](https://github.com/slackapi/bolt-python/issues/new/choose)
1. Create a new issue
1. Mention that you're using this example app

See you there and thanks for helping to improve Bolt for everyone!
