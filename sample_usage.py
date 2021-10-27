import table_utils


# Files to load to table
filenames = ["./sample_data/test_real_data.csv",
			 "./sample_data/test_real_data_1.csv",
			 "./sample_data/test_real_data_2.csv"]

# Table info
username = "testuser"
tablename = "test_table"

print("Initial size of file: {}".format(
	table_utils.get_table_len(username, tablename)))

for filename in filenames:
	table_utils.load_table(
		username,
		tablename,
		filename
	)
	# Shows that the table has grown after each Load command
	print("Size of file: {}".format(
		table_utils.get_table_len(username, tablename)))

