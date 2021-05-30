# cs362 - hw07
# casey nord
# spring 2021

import io
import sys
import unittest

from functions import fizzbuzz

# subclass unittest.TestCase to add capturing stdout
# taken from https://stackoverflow.com/a/66317713
class TestCase(unittest.TestCase):

    def assertStdout(self, expected_output):
        return _AssertStdoutContext(self, expected_output)

    # as a bonus, this syntactical sugar becomes possible:
    def assertPrints(self, *expected_output):
        expected_output = "\n".join(expected_output) + "\n"
        return _AssertStdoutContext(self, expected_output)


class _AssertStdoutContext:

    def __init__(self, testcase, expected):
        self.testcase = testcase
        self.expected = expected
        self.captured = io.StringIO()

    def __enter__(self):
        sys.stdout = self.captured
        return self

    def __exit__(self, exc_type, exc_value, tb):
        sys.stdout = sys.__stdout__
        captured = self.captured.getvalue()
        self.testcase.assertEqual(captured, self.expected)

    def assertStdout(self, expected_output):
        return _AssertStdoutContext(self, expected_output)    


class FizzBuzzTests(TestCase):

    def test_correct_values(self):
        with self.assertStdout("1\n"):
            fizzbuzz(1)
        with self.assertStdout("Fizz\n"):
            fizzbuzz(3)
        with self.assertStdout("Buzz\n"):
            fizzbuzz(5)
        with self.assertStdout("FizzBuzz\n"):
            fizzbuzz(15)


if __name__ == '__main__':
    unittest.main()
