'''
Unit testing for csv_helper
'''

import os
import unittest
from csv_helper import read_csv, sort_csv, write_csv
from empty_error import FileEmptyError

class TestFormula(unittest.TestCase):
    '''
    Test cases
    '''

    output_file = './files/test-output.csv'
    valid_input_file = './files/valid.csv'
    invalid_input_file = './files/invalid.csv'
    empty_file = './files/empty.csv'
    nonexistant_file = './files/nonexistant.csv'

    def tearDown(self):
        # cleanup
        if os.path.isfile(TestFormula.output_file):
            os.remove(TestFormula.output_file)

    unsorted_list = [['Number', 'Name'],
                    ['1', 'foo'],
                    ['10', 'fred'],
                    ['2', 'bar'],
                    ['11', 'plugh'],
                    ['14', 'thud'],
                    ['12', 'xyzzy'],
                    ['8', 'garply'],
                    ['9', 'waldo'],
                    ['6', 'corge'],
                    ['3', 'baz'],
                    ['4', 'qux'],
                    ['7', 'grault'],
                    ['5', 'quux'],
                    ['13', 'nacho']]

    sorted_list = [['Number', 'Name'],
                    ['1', 'foo'],
                    ['2', 'bar'],
                    ['3', 'baz'],
                    ['4', 'qux'],
                    ['5', 'quux'],
                    ['6', 'corge'],
                    ['7', 'grault'],
                    ['8', 'garply'],
                    ['9', 'waldo'],
                    ['10', 'fred'],
                    ['11', 'plugh'],
                    ['12', 'xyzzy'],
                    ['13', 'nacho'],
                    ['14', 'thud']]

    invalid_list = [['Name', 'Number'],
                    ['foo', '1'],
                    ['fred', '10'],
                    ['bar', '2'],
                    ['plugh', '11'],
                    ['thud', '14'],
                    ['xyzzy', '12'],
                    ['garply', '8'],
                    ['waldo', '9'],
                    ['corge', '6'],
                    ['baz', '3'],
                    ['qux', '4'],
                    ['grault', '7'],
                    ['quux', '5'],
                    ['nacho', '13']]

    def test_read(self):
        '''
        Test read_csv
        '''

        self.assertEqual(read_csv(TestFormula.valid_input_file), TestFormula.unsorted_list)
        self.assertEqual(read_csv(TestFormula.invalid_input_file), TestFormula.invalid_list)
        self.assertEqual(read_csv(TestFormula.empty_file), [])

        self.assertRaises(FileNotFoundError, read_csv, TestFormula.nonexistant_file)

    def test_sort(self):
        '''
        Test sort_csv
        '''

        # Ensure input list is not mutated
        some_list = [['row'], ['1'], ['1'], ['5'], ['3'], ['6']]
        copy_of_some_list = [['row'], ['1'], ['1'], ['5'], ['3'], ['6']]
        self.assertEqual(sort_csv(some_list), [['row'], ['1'], ['1'], ['3'], ['5'], ['6']])
        self.assertListEqual(some_list, copy_of_some_list)

        # No rows (empty file)
        self.assertRaises(FileEmptyError, sort_csv, [])

        # No data rows - no change.
        self.assertEqual(sort_csv([['These','Are','Headers','Without','Values']]), [['These','Are','Headers','Without','Values']])

        # Proper data - sort properly
        self.assertEqual(sort_csv(TestFormula.unsorted_list), TestFormula.sorted_list)

        # Invalid entries
        self.assertRaises(ValueError, sort_csv, TestFormula.invalid_list)

    def test_write(self):
        '''
        Test write_csv

        (Note that accepted behavior is overwriting)
        '''

        write_csv(TestFormula.output_file, [['a']])
        # Confirms file exists & contains 'a'
        self.assertListEqual(read_csv(TestFormula.output_file), [['a']])

        write_csv(TestFormula.output_file, TestFormula.sorted_list)
        # Confirms file exists & contains sorted list
        self.assertListEqual(read_csv(TestFormula.output_file), TestFormula.sorted_list)

        write_csv(TestFormula.output_file, TestFormula.unsorted_list)
        # Confirms file exists & contains unsorted list (verifies that even if input is "logically invalid," function is consistent with its definition)
        self.assertListEqual(read_csv(TestFormula.output_file), TestFormula.unsorted_list)

        write_csv(TestFormula.output_file, TestFormula.unsorted_list)
        # Confirms file exists & contains unsorted list (verifies that even if input is "logically invalid," function is consistent with its definition)
        self.assertNotEqual(read_csv(TestFormula.output_file), TestFormula.sorted_list)

if __name__ == "__main__":
    unittest.main()
