from os import getenv
from json import loads



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

