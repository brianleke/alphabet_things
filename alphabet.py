from alphabet_exception import AlphabetException
import re

class Alphabet:
	def __init__(self, input):
		self._validate_input_variable(input)
		self.result = self._formulate_output_string(input)


	def _validate_input_variable(self, input):
		result = re.match('^[A-z]$', input)
		if not result:
			raise AlphabetException()

	def _space(self, number):
		return number * ' '

	def _pre_space(self, number):
		return (number - 1) * ' '

	def _increment(self, end_position, start_position):
		number_of_spaces = end_position - start_position
		space_in_between = 0
		result = ' ' * number_of_spaces + 'A\n'
		result += self._append_right_format(end_position, start_position, 1, number_of_spaces, space_in_between) 
		return result

	def _append_right_format(self, end_position, start_position, flag, number_of_spaces, space_in_between):
		result = ''
		for letter_position in range(start_position, end_position, flag):
			number_of_spaces -= flag
			space_in_between += flag
			current_letter = chr(letter_position + flag)
			result += self._space(number_of_spaces) + current_letter + self._space(space_in_between) + current_letter + '\n'
		return result

	def _decrement(self, end_position, start_position):
		space_in_between = end_position - start_position
		number_of_spaces = 0
		start_position += 1
		result = self._append_right_format(start_position, end_position, -1, number_of_spaces, space_in_between)
		result += ' ' * space_in_between  + 'A'
		return result

	def _formulate_output_string(self, input):
		start_position = ord('A')
		end_position = ord(input.upper())
		if end_position - start_position == 0:
			return 'A'
		else:
			return self._increment(end_position, start_position) + self._decrement(end_position, start_position)

	def __str__(self):
		return self.result