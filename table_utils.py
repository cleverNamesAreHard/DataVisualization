from os import path, makedirs
from my_exceptions import *
import time
import user_utils
import data_utils

# Description:
#   BOOLEAN, returns whether or not a table exists in the user's folder
# Param:
#   owner     REQUIRED    STRING    Username of the resource owner
#   tablename REQUIRED    STRING    Name of the table to look up
# Usage:
#   a = user_is_onboarded("dev1", "table1")
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
    allowable_chars_s = "abcdefghijklmnopqrstuvwxyz_"
    allowable_chars = [char_ for char_ in allowable_chars_s]
    for char_ in tablename:
        if char_ not in allowable_chars:
            return False
    return True

# Description:
#   VOID, used to get and sanitize user input via CLI, and pass to
#   create_table()
def create_table_cli(**args):
    # Get User from Args or from Input
    user = ""
    if "testUser" not in args:
        user = input("Please enter the owner to onboard to:\n> ")
        user = user.lower()
    else:
        user = args["testUser"]
    if not user_utils.user_is_valid(user):
        raise OwnerNameInvalidError(user)
    if not user_utils.user_is_onboarded(user):
        raise OwnerNotOnboardedError(user)
    # Get Table name from Args or from Input
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
    # Get Headers from Args or from Input, and sanitize
    headers = []
    headers_s = ""
    if "headers" in args:
        headers_s = args["headers"]
    else:
        headers_s = input("Please enter your comma-separated headers:\n> ")
    if len(headers_s.split(",")) == 1:
        raise HeadersNotCSVError(headers_s)
    else:
         headers = headers_s.split(",")
    headers.append("snapshot")
    # Get types from Args or from Input, and sanitize
    types = []
    for header in headers:
        valid_types = ["TEXT", "BOOLEAN", "INTEGER", "DECIMAL"]
        type_s = ", ".join(type_x for type_x in valid_types)
        if "types" in args:
            types = args["types"]
            for type_ in types:
                if type_.upper() not in valid_types:
                    raise InvalidTypeError(type_.upper())
        else:
            print(f"\nValid types are {type_s}")
            type_ = input("Please enter the type for the following header:\n" \
                f"{header} > ")
            if type_.upper() in valid_types:
                types.append(type_.upper())
            else:
                raise InvalidTypeError(type_.upper())
    types.append("INTEGER")
    # Create the table if allowed
    if len(types) == len(headers):
        create_table(user, tablename, headers, types=types)
    else:
        raise TypesAssymetricalError(len(types), len(headers))

# Description:
#   VOID, pulls data from CSV (via data_utils), and enteres into table
# Params:
#   user        REQUIRED     STRING      Username of the table owner
#   tablename   REQUIRED     STRING      Text name of the table being created
#   data_source REQUIRED     STRING      Text name of file to open
#   snapshot    OPTIONAL     INTEGER     Epoch int timestamp for data entry day
#   delim       OPTIONAL     CHAR        Character to spit rows in source data
# Usage:
#   load_table("medovicn", "test_real_data",
#       "./sample_data/test_real_data.csv",
#       snapshot = 123456789, delim="\t")
def load_table(user, tablename, data_source, **args):
    '''
        Implement Error Catching for User, tablename, etc
    '''
    snapshot = ""
    if "snapshot" in args:
        try:
            snapshot = int(args["snapshot"])
        except ValueError:
            raise TimeNotEpochError(args["snapshot"])
    else:
        snapshot = int(time.time())
    delimeter = ","
    if "delim" in args:
        delimeter = args["delim"]
    new_table_contents = data_utils.get_data_from_csv(
        data_source,
        preserve_headers = False,
        delim = delimeter
    )
    if len(new_table_contents) == 0:
        raise FileEmptyError(data_source)
    with open(f"./{user}/{tablename}/data.csv", "a") as f_out:
        for row in new_table_contents["data"]:
            temp_s = ",".join(row)
            temp_s += f",{snapshot}\n"
            f_out.write(temp_s)
    print("Data load complete!")

# Description:
#   VOID, used to get and sanitize user input via CLI, and pass to
#   create_table()
def load_table_cli(**args):
    if "testSnapshot" in args:
        try:
            snapshot = int(args["testSnapshot"])
        except ValueError:
            raise TimeNotEpochError(args["testSnapshot"])
    else:
        snapshot = int(time.time())
    user = ""
    if "testUser" in args:
        user = args["testUser"]
    else:
        user = input("Enter the owner of the table:\n> ")
    tablename = ""
    if "testTable" in args:
        tablename = args["testTable"]
    else:
        tablename = input("Enter the name of the table:\n> ")
    delimeter = ","
    if "testDelim" in args:
        delimeter = args["testDelim"]
    else:
        delimeter = input("Enter the delimeter to split on:\n> ")
    table_location = ""
    if "testLocation" in args:
        data_location = args["testLocation"]
    else:
        data_location = input("Enter the path to the file to load:\n> ")
    load_table(user, tablename, data_location, delim=delimeter)

def get_table_len(username, tablename):
    if not user_utils.user_is_onboarded(username):
        raise OwnerNotOnboardedError(username)
    if not table_exists(username, tablename):
        raise TableDoesNotExistError(tablename)
    file_len = sum(1 for line in open("./{}/{}/data.csv".format(
        username, tablename
    )))
    # don't count headers
    return file_len - 1
