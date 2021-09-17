from os import path, makedirs
from my_exceptions import *

# Description:
#   VOID, creates a user's folder in the application's file structure
# Params:
#   user     REQUIRED     STRING      Username of the resource owner
# Usage:
#   onboard_user("medovicn")


def onboard_user(user):
    if path.isdir(f"./{user}"):
        raise OwnerAlreadyOnboardedError(user)
    else:
        makedirs(f"./{user}")
    print(f"User {user} onboarded!")

# Description:
#   BOOLEAN, returns whether or not a username input was valid
# Param:
#   user    REQUIRED    STRING      Username of the resource owner
# Usage:
#   a = user_is_valid("abC")
#   b = user_is_valid("zyx")
#   a
#   > False
#   b
#   > True


def user_is_valid(user):
    allowable_chars = set("abcdefghijklmnopqrstuvwxyz")
    return set(user) <= allowable_chars

# Description:
#   BOOLEAN, returns whether or not a user is onboarded
# Param:
#   user    REQUIRED    STRING      Username of the resource owner
# Usage:
#   a = user_is_onboarded("testUser1")
#   b = user_is_valid("spirited away")
#   a
#   > True
#   b
#   > False


def user_is_onboarded(user):
    if path.isdir(f"./{user}"):
        return True
    else:
        return False

# Description:
#   VOID, used to get and sanitize user input via CLI, and pass to
#    onboard_user()
# Params:
#   For internal testing only


def onboard_user_cli(**args):
    user = ""
    if "test" not in args:
        user = input("Please enter the username to onboard:\n> ")
        user = user.lower()
    else:
        user = args["test"]
    if user_is_valid(user):
        onboard_user(user)
    else:
        raise OwnerNameInvalidError(user)
