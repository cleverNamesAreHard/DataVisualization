import unittest
import data_utils
import table_utils
import user_utils
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
        self.assertRaises(TableAlreadyExistsError,
                          table_utils.create_table,
                          "testuser", "testTable", ["col1", "col2"])
        self.assertRaises(TableAlreadyExistsError,
                          table_utils.create_table,
                          "testuserone", "testTable", ["col1", "col2"])

    # Check if error on already onboarded owner is successful
    def test_owner_already_onboarded_throws_error(self):
        self.assertRaises(OwnerAlreadyOnboardedError,
                          user_utils.onboard_user,
                          "medovicn")
        self.assertRaises(OwnerAlreadyOnboardedError,
                          user_utils.onboard_user,
                          "testuser")
        self.assertRaises(OwnerAlreadyOnboardedError,
                          user_utils.onboard_user,
                          "testuserone")

    # Check if unsanitary CLI input fails owner onboarding
    def test_bad_input_on_owner_onboard_cli(self):
        self.assertRaises(OwnerNameInvalidError,
                          user_utils.onboard_user_cli,
                          test="AbraCadabra")
        self.assertRaises(OwnerNameInvalidError,
                          user_utils.onboard_user_cli,
                          test="phoenix0912")
        self.assertRaises(OwnerNameInvalidError,
                          user_utils.onboard_user_cli,
                          test="1337h@x0r@amazon.com")

    # Check if unsanitary CLI input fails table creation
    def test_bad_input_on_create_table_cli(self):
        self.assertRaises(OwnerNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="AbraCadabra",
                          testTable="abc")
        self.assertRaises(OwnerNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="phoenix0912",
                          testTable="zyxwvut")
        self.assertRaises(OwnerNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="1337h@x0r@amazon.com",
                          testTable="validtablename")
        self.assertRaises(TableNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="medovicn",
                          testTable="in_validtablename1")
        self.assertRaises(TableNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="another-badname.whatever\\okay")
        self.assertRaises(TableNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="testuserone",
                          testTable="tablename1")

    # Check if table existing and owner not-onboarded fails table creation
    def test_badowner_tableexists_create_table_cli(self):
        self.assertRaises(OwnerNotOnboardedError,
                          table_utils.create_table_cli,
                          testUser="validname",
                          testTable="tablename")
        self.assertRaises(OwnerNotOnboardedError,
                          table_utils.create_table_cli,
                          testUser="jessicaday",
                          testTable="abcdefg")
        self.assertRaises(OwnerNotOnboardedError,
                          table_utils.create_table_cli,
                          testUser="nickmiller",
                          testTable="kapowy")
        self.assertRaises(TableAlreadyExistsError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="test_table")
        self.assertRaises(TableAlreadyExistsError,
                          table_utils.create_table_cli,
                          testUser="testuserone",
                          testTable="testtable")


def main():
    print("Starting unit tests\n")
    # List each test performed.
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
