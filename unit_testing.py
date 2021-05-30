# cs362 - hw07
# casey nord
# spring 2021

# NOTE: this program is designed to run with python3
#       running with python2 may produce unexpected output

import unittest


class FizzBuzzTests(unittest.TestCase):

    def test_correct_values(self):
        self.assertEqual(fizzbuzz(1), "1")


if __name__ == '__main__':
    unittest.main()
