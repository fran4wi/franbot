from os import getenv
from json import loads


def write_to_sheet(event_data: dict, sheet) -> None:
    """
    write_to_sheet writes the event data for a new user
    joining the workspace to a google sheet

    Args:
        event_data (dict): object with profile information about
        the new user who has joined. To see an example, see
        "event_outputs_examples/user_join_event_example.json"
    """
    user: dict = event_data.get("user")
    id: str = user.get("id")
    profile_email: str = user.get("profile").get("email")
    first_name: str = user.get("profile").get("first_name")
    last_name: str = user.get("profile").get("last_name")
    JOIN_WS_SHEET_ID: str = getenv("JOIN_WS_SHEET_ID")
    event_ts: str = event_data.get("event_ts")

    worksheet = sheet.get_worksheet(0)
    worksheet.append_row([id, profile_email, first_name, last_name, event_ts])


def new_workspace_user_message(user_id: str, template: str) -> dict:
    """
    user_join_blocks creates a custom message for the bot to write back
    to the user who just joined the workspace.

    Args:
        user_id (str): the id of the person who is joining the workspace.

    Returns:
        dict: texts/welcome.json, but with placeholders replaced with actual data.
    """
    welcome_text = template.replace("__USER_ID__", user_id)
    welcome_text = welcome_text.replace(
        "__VOLUNTEER_HANDBOOK_LINK__", getenv("VOLUNTEER_HANDBOOK_LINK")
    )
    welcome_text = welcome_text.replace(
        "__NEW_WS_JOINER_REACHOUT_IDS__", getenv("NEW_WS_JOINER_REACHOUT_IDS")
    )
    welcome_json: dict = loads(welcome_text)

    return welcome_json

