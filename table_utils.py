from os import path, makedirs
from my_exceptions import *


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
    if path.isdir(f"./{owner}"):
        if path.isdir(f"./{owner}/{tablename}"):
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
