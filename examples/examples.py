"""
functions in this file are not currently being used and are only available because they are useful for understanding slack's bot framework
"""
import json
# @app.event("member_joined_channel") 
def chanel_joined(event, say): 

    user_id = event["user"] 
    texts = "member_joined_channel"
    blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": texts}
            }
        ]
    say(blocks=blocks, text=texts,channel=user_id)

    
# @app.message("hello")
def message_hello(message, say):
    # app.client.chat_postMessage(
    channel=message.get("user")
    print("message contains hello!", channel)
    with open("templates/welcome.json") as f:
        welcome_text = f.read()
    print("welcome text === ", welcome_text)
    welcome_text = welcome_text.replace("__USER_ID__", channel)
    welcome_json = json.loads(welcome_text)
    say(
        channel=channel,
        blocks=welcome_json,
        text=f"Hey there <@{message['user']}>!",
    )
    say(text="yee haw",channel=channel)
