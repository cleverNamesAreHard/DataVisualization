from csv import reader
import ast


# Description:
#   Returns a dict() with header info and file contents
# Params:
#   filename            REQUIRED    STRING      name of input data file
#   preserve_headers    OPTIONAL    BOOL        keep first line of file?
#   delim               OPTIONAL    CHAR        what to split lines by
# Usage:
#   returnDict = get_data_from_csv("some_file.csv", preserve_headers=True)
# Returns:
#   returnDict["hasHeaders"]    = True
#   returnDict["headers"]       = [col1, col2, col3, col4]
#   returnDict["data"]          = [[col1, col2, col3, col4],
#                                  [ro11, ro12, ro13, ro14],
#                                  [ro21, ro22, ro23, ro24]]
def get_data_from_csv(filename, **args):
    # This may be expanded to include other types
    acceptable_filetypes = ["csv", "txt"]
    file_appension = filename.split(".")[-1]
    # Unit tests will fail if this raises an error
    if file_appension not in acceptable_filetypes:
        raise ValueError("Invalid filetype.  Supported: ",
                         acceptable_filetypes,
                         "Entered: ", file_appension)
    # Optional argument, but the value is necessary
    # Defaults to False
    preserve_headers = False
    headers_ = []
    if "preserve_headers" in args:
        if args["preserve_headers"]:
            preserve_headers = True

    # Read in file contents
    data_out = []
    # This is to catch for possible headers on line 1
    headers = True
    with open(filename, "r") as f_in:
        # Optional argument, but the value is necessary
        delim = ","
        if "delim" in args:
            delim = args["delim"]
        # File-Read loop
        for row in reader(f_in, delimiter=delim):
            # Any line but the first
            if not headers:
                data_out.append(row)
            # First line in the file
            else:
                if preserve_headers:
                    # Keep the headers for later
                    headers_ = row
                # Move on to the body of the file
                headers = False
    # Empty files should throw an error for the purposes of this library
    # Note, a header-only file will still trip this condition, because
    #  headers are not stored in data_out until the else-clause
    if len(data_out) == 0:
        raise Exception("Empty or headers-only file input!")
    else:
        # Join them back together, per user input
        if preserve_headers:
            data_out.insert(0, headers_)
    # Create return variable
    dictOut = {}
    dictOut["hasHeaders"] = preserve_headers
    if preserve_headers:
        dictOut["headers"] = headers_
    dictOut["data"] = data_out
    return dictOut

# Description:
#   Returns a list() with with types for data storage
# Params:
#   values     REQUIRED     LIST      1 row of values from data table
# Usage:
#   types = get_types(["nick", 24, "male", "data analyst"])
# Returns:
#   types = ["TEXT", "INTEGER", "TEXT", "TEXT"]


def get_types(values):
    types_out = []
    for value_ in values:
        this_type = ""
        # Remove white-space at end of string
        s = value_.strip()
        try:
            # Create an object from evaluating the input value
            t = ast.literal_eval(s)
        # If it can't be forced to a type, it's a String
        except ValueError:
            this_type = "TEXT"
            types_out.append(this_type)
            continue
        except SyntaxError:
            this_type = "TEXT"
            types_out.append(this_type)
            continue
        # We're only allowing these for now
        if type(t) in [int, float, bool]:
            if t in set((True, False)):
                this_type = "BOOLEAN"
            if isinstance(t, int):
                this_type = "INTEGER"
            if isinstance(t, float):
                this_type = "DECIMAL"
        # Otherwise, we force it to String
        else:
            this_type = "TEXT"
        types_out.append(this_type)
    return types_out
