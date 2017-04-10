import unittest
from alphabet_exception import AlphabetException
from alphabet import Alphabet

class AlphabetTest(unittest.TestCase):
	def test_should_throw_alphabet_exception_on_initialisation_for_invalid_input(self):
		expected_message = 'INVALID INPUT'
		with self.assertRaises(AlphabetException) as exception_mock:
			Alphabet('1')

		raised_exception = exception_mock.exception
		self.assertEqual(expected_message, raised_exception.message)

	def test_should_throw_alphabet_exception_on_initialisation_for_repeated_input(self):
		expected_message = 'INVALID INPUT'
		with self.assertRaises(AlphabetException) as exception_mock:
			Alphabet('AA')

		raised_exception = exception_mock.exception
		self.assertEqual(expected_message, raised_exception.message)

	def test_should_throw_alphabet_exception_on_initialisation_for_repeated_input_character_case(self):
		expected_message = 'INVALID INPUT'
		with self.assertRaises(AlphabetException) as exception_mock:
			Alphabet('Aa')

		raised_exception = exception_mock.exception
		self.assertEqual(expected_message, raised_exception.message)

	def test_should_throw_alphabet_exception_on_initialisation_for_alphanumeric_input(self):
		expected_message = 'INVALID INPUT'
		with self.assertRaises(AlphabetException) as exception_mock:
			Alphabet('A1')

		raised_exception = exception_mock.exception
		self.assertEqual(expected_message, raised_exception.message)

	def test_should_not_throw_the_alphabet_exception_on_initialisation_for_valid_input(self):
		try:
			Alphabet('A')
		except:
			self.fail("Alphabet exception raised")

	def test_should_not_throw_the_alphabet_exception_on_initialisation_for_valid_lowercase_input(self):
		try:
			Alphabet('a')
		except:
			self.fail("Alphabet exception raised")

	def test_output_string_for_letter_A_is_A(self):
		expected_string = 'A'
		self.assertEqual(expected_string, str(Alphabet('A')))

	def test_out_string_for_letter_B_has_both_letters(self):
		expected_string = ' A\nB B\n A'
		self.assertEqual(expected_string, str(Alphabet('B')))

	def test_out_string_for_letter_E_has_both_letters(self):
		expected_string = '    A\n   B B   \n  C   C  \n D     D \nE       E\n D     D \n  C   C  \n   B B   \n    A'
		self.assertEqual(expected_string, str(Alphabet('E')))

	def test_out_string_for_letter_d_has_both_letters(self):
		expected_string = '   A\n  B B  \n C   C \nD     D\n C   C \n  B B  \n   A'
		self.assertEqual(expected_string, str(Alphabet('d')))

if __name__ == '__main__':
	unittest.main()
