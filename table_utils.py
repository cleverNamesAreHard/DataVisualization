from os import path, makedirs
from my_exceptions import *
import user_utils

# Description:
#   BOOLEAN, returns whether or not a table exists in the user's folder
# Param:
#   owner     REQUIRED    STRING    Username of the resource owner
#   tablename REQUIRED    STRING    Name of the table to look up
# Usage:
#   a = user_is_onboarde("dev1", "table1")
#   b = user_is_valid("dev2", "table2")
#   a
#   > True
#   b
#   > False


def table_exists(owner, tablename):
    if path.isdir(f"./{owner}/{tablename}"):
        return True
    else:
        return False

# Description:
#   VOID, creates a table directory under the owner, populates an empty
#    data file, and fills in the column headers.
#   If specified, it will create the config file for the headers, which
#    specify the data types of each column for later analyses
# Params:
#   owner     REQUIRED     STRING      Username of the table owner
#   tablename REQUIRED     STRING      Text name of the table being created
#   headers   REQUIRED     LIST        String names of columns for table
#   types     OPTIONAL     LIST        Types of each column.  From
#                                      data_utils.py:get_types()
# Usage:
#   create_table("medovicn", "test_real_data",
#       ["name","age","sex","occupation"],
#       types=["TEXT","INTEGER","TEXT","TEXT"])


def create_table(owner, tablename, headers, **args):
    if user_utils.user_is_onboarded(owner):
        if table_exists(owner, tablename):
            # The path (table) already exists
            raise TableAlreadyExistsError(tablename)
        else:
            # Make the directory for the table
            makedirs(f"./{owner}/{tablename}")
            # Make the table's data-file
            with open(f"./{owner}/{tablename}/data.csv", "w") as f_out:
                f_out.write("{}\n".format(
                    ",".join(header for header in headers)
                ))
            # If the types var is set, set up the config file
            if "types" in args:
                with open(f"./{owner}/{tablename}/conf.csv", "w") as f_out:
                    f_out.write("{}\n".format(
                        ",".join(type_ for type_ in args["types"])
                    ))
    # If the owner hasn't been onboarded, there could be a permissions issue
    # This should cause unit tests to fail on build for now.
    else:
        raise OwnerNotOnboardedError(owner)
    print("Table Created!\n")

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


def tablename_is_valid(tablename):
    allowable_chars = set("abcdefghijklmnopqrstuvwxyz_")
    return set(tablename) <= allowable_chars

# Description:
#   VOID, used to get and sanitize user input via CLI, and pass to
#   create_table()


def create_table_cli(**args):
    user = ""
    if "testUser" not in args:
        print(args)
        user = input("Please enter the owner to onboard to:\n> ")
        user = user.lower()
    else:
        user = args["testUser"]
    if not user_utils.user_is_valid(user):
        raise OwnerNameInvalidError(user)
    if not user_utils.user_is_onboarded(user):
        raise OwnerNotOnboardedError(user)
    tablename = ""
    if "testTable" not in args:
        tablename = input("Please enter the tablename to create:\n> ")
        tablename = tablename.lower()
    else:
        tablename = args["testTable"]
    if not tablename_is_valid(tablename):
        raise TableNameInvalidError(tablename)
    if table_exists(user, tablename):
        raise TableAlreadyExistsError(tablename)
    pass

    
'''
    TODO:
        Write in header import by file and by typing (first)
'''
