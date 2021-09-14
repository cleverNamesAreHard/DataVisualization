import user_utils
import table_utils
import data_utils
import sys


def main(args):
    # For testing input against valid indeces
    indeces = []
    # Defaults to 0 so no-value results in error
    selection = 0
    # Controls the options that are displayed
    args_list = {
        1: {
            "text": "Onboard New User",
            "run_": user_utils.onboard_user
        },
        2: {
            "text": "Create New Table",
            "run_": table_utils.create_table
        }
    }
    # Display option list and put indeces into their list
    for arg_ in args_list:
        print("[{:2} ] {}".format(
            arg_,
            args_list[arg_]["text"]
        ))
        indeces.append(arg_)
    # Get User's input, and force it to int-type
    try:
        selection = int(input("\n# > "))
    # Check for non-numerics entered, and exit with error if needed
    except ValueError:
        sys.exit("Please enter a valid input: {}\n".format(
            ", ".join(str(index_) for index_ in indeces)
        ))
    # Check for non-entered numbers (0), or invalid numbers
    if selection not in indeces:
        sys.exit("Please enter a valid input: {}\n".format(
            ", ".join(str(index_) for index_ in indeces)
        ))
    # Run function assigned to option
    args_list[selection]["run_"]()


if __name__ == "__main__":
    main(sys.argv)
