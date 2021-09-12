import unittest
import data_utils
import table_utils
from my_exceptions import *


class MyTest(unittest.TestCase):
	# Check if file-extension logic works
	def test_file_extension_validation_get_data_from_csv(self):
		self.assertRaises(ValueError, data_utils.get_data_from_csv, 
			"test.dat")
		self.assertRaises(ValueError, data_utils.get_data_from_csv, 
			"test_name.09.12.sh")
		self.assertRaises(ValueError, data_utils.get_data_from_csv,
			"/REJECT_DIR/bad0001.rej")

	# Check if checks for potentially empty data files work
	def test_file_contents_errors(self):
		self.assertRaises(Exception, data_utils.get_data_from_csv,
			"test_empty_file.csv")
		self.assertRaises(Exception, data_utils.get_data_from_csv,
			"test_headers_only.csv")
		self.assertRaises(Exception, data_utils.get_data_from_csv,
			"test_headers_only.csv", preserve_headers=True)

	# Check if erroring on owner not onboarded is successful
	def test_not_onboarded_fails_table_creation(self):
		self.assertRaises(OwnerNotOnboardedError, table_utils.create_table,
			"------", "testTable", ["col1", "col2"])
		self.assertRaises(OwnerNotOnboardedError, table_utils.create_table,
			"zac efron", "testTable2", ["col1", "col2"])
		self.assertRaises(OwnerNotOnboardedError, table_utils.create_table,
			"luigi_mario_wario", "testTable3", ["col1", "col2"])

	# Check if error on table-existing is successful
	def test_table_exists_throws_error(self):
		self.assertRaises(TableAlreadyExistsError, table_utils.create_table,
			"testUser", "testTable", ["col1", "col2"])
		self.assertRaises(TableAlreadyExistsError, table_utils.create_table,
			"testUser1", "testTable", ["col1", "col2"])

def main():
	print("Starting unit tests\n")
	# List each test performed.
	unittest.main(verbosity=2)

if __name__ == "__main__":
	main()
