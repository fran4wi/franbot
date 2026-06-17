from os.path import exists as path_exists
from json import loads


def load_template(path: str | None, ginterface):
    if not path:
        ginterface.LOG_ERROR(
            [f"ERROR: WORKSPACE_JOIN_TEMPLATE_PATH ENVIRONMENT VARIABLE NOT SET"]
        )
    elif path_exists(path) == False:
        ginterface.LOG_ERROR([f"ERROR: WORKSPACE_JOIN_TEMPLATE_PATH DOES NOT EXIST"])
    else:
        with open(path) as f:
            return f.read()


def new_workspace_user_message(user_id: str, template: str):
    """
    user_join_blocks creates a custom message for the bot to write back
    to the user who just joined the workspace.

    Args:
        user_id (str): the id of the person who is joining the workspace.

    Returns:
        dict: texts/welcome.json, but with placeholders replaced with actual data.
    """
    welcome_text = template.replace("__USER_ID__", user_id)
    return loads(welcome_text)
