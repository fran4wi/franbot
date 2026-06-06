import os
import user_join
from dotenv import load_dotenv
from slack_bolt import App
from collections.abc import Callable
from slack_bolt.adapter.socket_mode import SocketModeHandler

# This sample slack application uses SocketMode
# For the companion getting started setup guide,
# see: https://docs.slack.dev/tools/bolt-python/getting-started

# use dotenv instead of system envvars
load_dotenv()
app = App(
        name="FranBot",
        token=os.getenv("SLACK_BOT_TOKEN"),
        signing_secret=os.getenv("SLACK_SIGN_SECRET")
        )


@app.event("team_join") 
def handle_event__team_join(event:dict, say:Callable[[dict,str,str],None]) -> None:

    """
    event_team_join handles what happens when a new member joins the workspace. 
    
    It will a function that sends a welcome message through a direct message to the volunteer,
    then write a message to a channel,

    Args:
        event (_type_): _description_
        say (_type_): _description_
    """
    user_id : str = event["user"]["id"]
    welcome_json : dict = user_join.new_workspace_user_message(user_id)
    say(blocks=welcome_json, text="!", channel=user_id)
    user_join.write_to_sheet(event)
    return


if __name__ == "__main__":
    try:
        SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    except KeyboardInterrupt:
        print("goodbye")
