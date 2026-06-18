from os import getenv
from os.path import exists as path_exists
from json import loads
from google_interface import container as Google_Interface


def load_template(TEMPLATE_PATH:str|None) -> str:
    """
    load_template loads up a template for use replying to other events

    Args:
        TEMPLATE_PATH (str | None): path to a .json file. 

    Returns:
        str: the template that has been loaded
    """
    if not TEMPLATE_PATH:
        Google_Interface.LOG_ERROR([f"ERROR: WORKSPACE_JOIN_TEMPLATE_PATH ENVIRONMENT VARIABLE NOT SET"])
    elif path_exists(TEMPLATE_PATH) == False: 
        Google_Interface.LOG_ERROR([f"ERROR: WORKSPACE_JOIN_TEMPLATE_PATH DOES NOT EXIST"])
    with open(TEMPLATE_PATH) as f:
        TEMPLATE = f.read()
    return TEMPLATE

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
    welcome_json: dict = loads(welcome_text)

    return welcome_json

