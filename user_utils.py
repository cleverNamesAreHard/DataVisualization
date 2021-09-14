from os import path, makedirs
from my_exceptions import *

# Description:
#   VOID, creates a user's folder in the application's file structure
# Params:
#   owner     REQUIRED     STRING      Username of the resource owner
# Usage:
#   onboard_user("medovicn")


def onboard_user(user):
    if path.isdir(f"./{owner}"):
        raise OwnerAlreadyOnboardedError(owner)
    else:
        makedirs(f"./{owner}")
