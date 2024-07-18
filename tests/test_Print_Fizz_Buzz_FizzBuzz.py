##!/usr/bin/env python3

#Created by FOURNIER UGARTE Óscar

import io
import unittest.mock

from Print_Fizz_Buzz_FizzBuzz import Print_Fizz_Buzz_FizzBuzz


class MyTestCase(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_unitary(self, number, expected_output, mock_stdout):
        Print_Fizz_Buzz_FizzBuzz.print_Fizz_Buzz_FizzBuzz_number(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_first_None(self):
        self.assertEqual(Print_Fizz_Buzz_FizzBuzz.print_Fizz_Buzz_FizzBuzz_number(10), None)

    def test_firt_True(self):
        self.assertEqual(Print_Fizz_Buzz_FizzBuzz.print_Fizz_Buzz_FizzBuzz_number(10), True)

    def test_unitary_with_3(self):
        self.test_unitary(3, 'Fizz')

    def test_unitary_with_5(self):
        self.test_unitary(5, 'Buzz')

    def test_unitary_with_3x5(self):
        self.test_unitary( ( 3 * 5 ), 'FizzBuzz')

    def test_unitary_with_1(self):
        self.test_unitary(1, '1')

    def test_pair_with_3n(self):
        self.test_unitary( ( 3 * 2 ), 'Fizz')
        self.test_unitary( ( 3 * 21 ), 'Fizz')

    def test_pair_with_5n(self):
        self.test_unitary( ( 5 * 4 ), 'Buzz')
        self.test_unitary( ( 5 * 43 ), 'Buzz')

    def test_pair_with_3x5n(self):
        self.test_unitary( ( ( 3 * 5 ) * 34 ), 'FizzBuzz')
        self.test_unitary( ( ( 3 * 5 ) * 3433 ), 'FizzBuzz')

    def test_pair_with_1n(self):
        self.test_unitary( ( 1 * 11 ), '11')
        self.test_unitary( ( 1 * 9998 ), '9998')

    def test_range_with_3n(self, start = -1098, end = 1098):
        limit = 1E7
        if start < end and ( end - start ) <= limit:
            for number in range(start, end):
                if not ( number % ( 3 * 5 ) ) == 0 and (number % 3) == 0:
                    self.test_unitary(number, 'Fizz')

    def test_range_with_5n(self, start = -1098, end = 1098):
        limit = 1E7
        if start < end and ( end - start ) <= limit:
            for number in range(start, end):
                if not ( number % ( 3 * 5 ) ) == 0 and (number % 5) == 0:
                    self.test_unitary(number, 'Buzz')

    def test_range_with_3x5n(self, start = -1098, end = 1098):
        limit = 1E7
        if start < end and ( end - start ) <= limit:
            for number in range(start, end):
                if ( number % ( 3 * 5 ) ) == 0:
                    self.test_unitary(number, 'FizzBuzz')

    def test_range_with_1n(self, start = -1098, end = 1098):
        limit = 1E7
        if start < end and ( end - start ) <= limit:
            for number in range(start, end):
                if not ( number % ( 3 * 5 ) ) == 0 \
				and not ( number % 3 ) == 0 \
				and not ( number % 5 ) == 0:
                    self.test_unitary(number, str(number))

    # The set of important ones
    def tests(self):
        self.test_unitary_with_3()
        self.test_unitary_with_5()
        self.test_unitary_with_3x5()
        self.test_unitary_with_1()
        self.test_pair_with_3n()
        self.test_pair_with_5n()
        self.test_pair_with_3x5n()
        self.test_pair_with_1n()
        self.test_range_with_3n()
        self.test_range_with_5n()
        self.test_range_with_3x5n()
        self.test_range_with_1n()

    def test_unitary_with_float_3(self):
        self.test_unitary(3.0, 'Fizz')

    def test_unitary_with_float_5(self):
        self.test_unitary(5.0, 'Buzz')

    def test_unitary_with_float_3x5(self):
        self.test_unitary( ( 3.0 * 5.0 ), 'FizzBuzz')

    def test_unitary_with_float_1(self):
        self.test_unitary(1.0, '1.0')


if __name__ == '__main__':
    unittest.main()

#Created by Óscar FOURNIER UGARTE