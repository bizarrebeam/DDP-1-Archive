import unittest
import os # only for checking whether the filesaving after generate the barcode is working:)
from ean13 import MyBarcode

"""
testing whether ean13.py, given desired filename
and real-product barcode number, would return the
right checkdigit and save it right away
as postscript file.
"""
class TestMyBarcode(unittest.TestCase):

    # 1st product: pia 100
    def test_generate_and_check_first_barcode(self):                  
        my_barcode_app = MyBarcode()
        my_barcode_app.entry_input_code.insert(0, '899294212040')
        checkdigit = my_barcode_app.generate_checkdigit()

        # validate and get the filename
        filename = 'tc1_pia100.ps'
        my_barcode_app.entry_save_barcode.insert(0, filename)
        my_barcode_app.validate_input()

        # assert that the checkdigit is correct
        self.assertEqual(checkdigit, 8)

        # assert that the file exists
        self.assertTrue(os.path.exists(filename))

    # 2nd product: greenfields
    def test_generate_and_check_second_barcode(self):
        my_barcode_app = MyBarcode()
        my_barcode_app.entry_input_code.insert(0, '899335112262')
        checkdigit = my_barcode_app.generate_checkdigit()

        # validate and get the filename
        filename = 'tc2_greenfields.ps'
        my_barcode_app.entry_save_barcode.insert(0, filename)
        my_barcode_app.validate_input()

        # assert that the checkdigit is correct
        self.assertEqual(checkdigit, 5)

        # assert that the file exists
        self.assertTrue(os.path.exists(filename))

    # 3rd product: lafonte
    def test_generate_and_check_third_barcode(self):
        my_barcode_app = MyBarcode()
        my_barcode_app.entry_input_code.insert(0, '888890060011')
        checkdigit = my_barcode_app.generate_checkdigit()

        # validate and get the filename
        filename = 'tc3_lafonte.eps'
        my_barcode_app.entry_save_barcode.insert(0, filename)
        my_barcode_app.validate_input()

        # assert that the checkdigit is correct
        self.assertEqual(checkdigit, 5)

        # assert that the file exists
        self.assertTrue(os.path.exists(filename))

if __name__ == '__main__':
    unittest.main()
