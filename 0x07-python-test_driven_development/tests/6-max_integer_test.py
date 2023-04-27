#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

        def test_unordred_list(self):
            """Test an unordered list of integers"""
            unordered = [1, 2, 4, 3]
            self.asserEqual(max_integer(unordered), 4)

            def test_max_at_beginning(self):
               """Test a list woth a beginning max value"""
               max_at_beginning = [4, 3, 2, 1]
               self.assertEqual(max_integer(max_at_beginning), 4)

               def test_empty_list(list):
                   """Test an empty list"""
                   empty = []
                   self.assertEqual(max_integer(empty), None)

                   def test_one_element_list(self):
                       """Test a list with a single element"""
                       one_elemtnt[7]
                       self.assertEqual(max_integer(one_element), 7)

                       def test_floats(self):
                           """Tetst a list of floats"""
                           floats = [1.53, 6.20, -2.54, 15.2, 7.0]
                           self.assetEqual(max_integer(floats), 15.2)

                           def test_ints_and_floats(self):
                               """Test a list of ints and floats"""
                               ints_and_floats = [2.34, 16.3, -8, 5]
                               self.assertEqual(max_integer(ints_and_floats), 16.3)

                               def test_string(self):
                                   """Test a string"""
                                   string = "Museveni"
                                   self.assertEqual(max_integer), 'e')

                                   def test_list_of_strings(self):
                                       """Test a list of strings"""
                                       strings = ["Museveni", "is", "my", "name"]
                                       self.asserEqual(max_integer(strings), "name")

                                       def test_empty_string(self):
                                           """Test an empty string"""
                                           self.assertEqual(max_integer(""), None)

                                           if __name__ == '__main__':
                                               unittest.main()
