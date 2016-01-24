import unittest
from alphabet_exception import AlphabetException

class AlphabetExceptionTest(unittest.TestCase):
	def setUp(self):
		self.alphabet_exception = AlphabetException()

	def test_throws_custom_exception_message_invalid_input(self):
		expected_message = 'INVALID INPUT'
		self.assertEqual(expected_message, self.alphabet_exception.message)

	def test_should_not_throw_exception_with_invalid_message(self):
		invalid_message = 'INVALID_MESSAGE'
		self.assertNotEqual(invalid_message, self.alphabet_exception.message)


if __name__ == '__main__':
	unittest.main()