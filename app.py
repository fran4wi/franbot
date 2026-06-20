from os import getenv
from json import loads
from os.path import exists as path_exists
from slack_bolt import App
from dotenv import load_dotenv
from gspread import service_account
from collections.abc import Callable
import utils
from google_interface import Google_Container
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime

ABOUT_STRING = datetime.now().strftime( "%m/%d/%Y, %H:%M:%S")
# global state variables
WELCOME_TEMPLATE: str = ""
GOOGLE_INTERFACE = None

# use dotenv instead of system envvars
load_dotenv()

app = App(
    name="FranBot",
    token=getenv("SLACK_BOT_TOKEN"),
    signing_secret=getenv("SLACK_SIGN_SECRET"),
)


@app.event("team_join")
def handle_event__team_join(event: dict, say: Callable[[dict, str, str], None]) -> None:
    """
    event_team_join handles what happens when a new member joins the workspace.

    It will a function that sends a welcome message through a direct message to the volunteer,
    then write a message to a channel,

    Args:
        event (_type_): _description_
        say (_type_): _description_
    """
    user_id = event["user"]["id"]
    welcome_json = utils.new_workspace_user_message(user_id, WELCOME_TEMPLATE)

    say(blocks=welcome_json, text="!", channel=user_id)
    GOOGLE_INTERFACE.new_user_join(event)
    # user_join.write_to_sheet(event, GOOGLE_SHEET)


@app.command("/franbot/test/welcome_message")
def test_welcome_message(ack, body: dict, say):
    """
    test_welcome_message : a command we use to make sure our welcome message is formatted correctly.

    Args:
        ack (Callable[[], None]): used to tell slack you got the command request.
        body (dict ) : information on who and where the command was called. we are using it so that we can
        see where the DM should be sent back to.
        say(Callable[[dict,str,str],None]): the response you give back to the end user, through their DM's.
    """
    # Acknowledge command request
    ack()

    user_id = body.get("user_id")
    welcome_json = utils.new_workspace_user_message(user_id, WELCOME_TEMPLATE)
    say(blocks=welcome_json, text="!", channel=user_id)

@app.command("/franbot/about")
def command_about(ack: Callable[[], None], respond: Callable[[str], None]):
    """
    command_about : command that gives information about the bot. right now, it only gives
    the latest time it was deployed.

    Args:
        ack (Callable[[], None]): used to tell slack you got the command request.
        respond (Callable[[str], None]): the response you give back to the end user.
    """
    # Acknowledge command request
    ack()
    # print("!!!!")
    respond(ABOUT_STRING)
    GOOGLE_INTERFACE.fran([])

if __name__ == "__main__":
    # create a new google container
    GOOGLE_INTERFACE = Google_Container(
        loads(getenv("GOOGLE_SERVICEKEY_JSON")), loads(getenv("GSHEET_LOG_IDS"))
    )

    WELCOME_TEMPLATE = utils.load_template(
        getenv("WORKSPACE_JOIN_TEMPLATE_PATH"), GOOGLE_INTERFACE
    )
    try:
        SocketModeHandler(app, getenv("SLACK_APP_TOKEN")).start()
    except KeyboardInterrupt:
        print("goodbye")
