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
                          "sample_data/test_empty_file.csv")
        self.assertRaises(Exception, data_utils.get_data_from_csv,
                          "sample_data/test_headers_only.csv")
        self.assertRaises(Exception, data_utils.get_data_from_csv,
                          "sample_data/test_headers_only.csv", preserve_headers=True)

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
                          testTable="abc.def",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(OwnerNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="phoenix0912",
                          testTable="zyxwvutHJSDG",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(OwnerNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="1337h@x0r@amazon.com",
                          testTable="validt>ablename",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(TableNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="medovicn",
                          testTable="in_validtablename1.t1",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(TableNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="another-badname.whatever\\okay",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(TableNameInvalidError,
                          table_utils.create_table_cli,
                          testUser="testuserone",
                          testTable="tablename1_x>ty",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])

    # Check if table existing and owner not-onboarded fails table creation
    def test_badowner_tableexists_create_table_cli(self):
        self.assertRaises(OwnerNotOnboardedError,
                          table_utils.create_table_cli,
                          testUser="validname",
                          testTable="tablename",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(OwnerNotOnboardedError,
                          table_utils.create_table_cli,
                          testUser="jessicaday",
                          testTable="abcdefg",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(OwnerNotOnboardedError,
                          table_utils.create_table_cli,
                          testUser="nickmiller",
                          testTable="kapowy",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(TableAlreadyExistsError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="test_table",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])
        self.assertRaises(TableAlreadyExistsError,
                          table_utils.create_table_cli,
                          testUser="testuserone",
                          testTable="testtable",
                          headers="a,b",
                          types=["TEXT", "DECIMAL"])


    def test_headers_not_csv_fails(self):
        self.assertRaises(HeadersNotCSVError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="not_real_table",
                          headers="name.age.sex")
        self.assertRaises(HeadersNotCSVError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="fake_table_table",
                          headers="1header")


    def test_headers_invalid_types_fail(self):
        self.assertRaises(InvalidTypeError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="what_even_is_python",
                          headers="name,age,weight,test",
                          types=["text","integer","float", "char"])
        self.assertRaises(InvalidTypeError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="why_not_java",
                          headers="name,age,weight,test",
                          types=["text","integer","decimal", "float"])


    def test_assymetrical_types_headers_fails(self):
        self.assertRaises(TypesAssymetricalError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="oh_im_not_a_pleb",
                          headers="name,age",
                          types=["text","integer","decimal"])
        self.assertRaises(TypesAssymetricalError,
                          table_utils.create_table_cli,
                          testUser="testuser",
                          testTable="obviously_best_language",
                          headers="name,age,sex",
                          types=["text","integer"])

    def test_load_table(self):
        self.assertRaises(TimeNotEpochError,
                          table_utils.load_table,
                          "medovicn",
                          "apollo_audit_data",
                          "./sample_data/audit_data_2021_09_05.csv",
                          snapshot="2021-10-10")

def main():
    print("Starting unit tests\n")
    # List each test performed.
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
