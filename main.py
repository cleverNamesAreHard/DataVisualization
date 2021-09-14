from data_utils import get_data_from_csv, get_types
from table_utils import create_table


def main():
    data_in = get_data_from_csv("test_real_data.csv",
                                preserve_headers=True)
    headers = data_in["headers"]
    header_types = get_types(data_in["data"][1])
    create_table("medovicn", "test_real_data", headers, types=header_types)


if __name__ == "__main__":
    main()
