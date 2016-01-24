from alphabet_exception import AlphabetException
import re

class Alphabet:
	INITIAL_SPACE_COUNT = 0
	SPACE = ' '
	def __init__(self, input):
		self._validate_input_variable(input)
		self.result = self._formulate_output_string(input)


	def _validate_input_variable(self, input):
		valid_match = re.match('^[A-z]$', input)
		if not valid_match:
			raise AlphabetException()

	def _space(self, number):
		return number * Alphabet.SPACE

	def _pyramid(self, end_position, start_position):
		number_of_spaces = end_position - start_position
		result = self._space(number_of_spaces) + 'A\n'
		result += self._append_middle_pyramid(start_position, end_position) 
		result += self._space(number_of_spaces) + 'A'
		return result

	def _reverse_pyramid(self, half_pyramid):
		second_half = ''
		first_part = half_pyramid.strip('\n').rsplit('\n', 1)
		if len(first_part) > 1:
			second_half += first_part[0][::-1] + '\n'
		return second_half
		
	def _first_half_of_pyramid(self, start_counter, end_counter):
		number_of_spaces = end_counter - start_counter
		space_in_between = multiplier = Alphabet.INITIAL_SPACE_COUNT

		first_half = ''
		
		for letter_position in range(start_counter, end_counter):
			number_of_spaces -= 1
			space_in_between += 1
			current_letter = chr(letter_position + 1)
			first_half += self._space(number_of_spaces) + current_letter + self._space(space_in_between) + self._space(multiplier) + current_letter + self._space(number_of_spaces) + '\n'
			multiplier += 1
		
		return first_half

	def _append_middle_pyramid(self, start_counter, end_counter):
		first_half = self._first_half_of_pyramid(start_counter, end_counter)
		second_half = self._reverse_pyramid(first_half)
		return first_half + second_half 

	def _formulate_output_string(self, input):
		start_position = ord('A')
		end_position = ord(input.upper())
		if end_position - start_position == 0:
			return 'A'
		else:
			return self._pyramid(end_position, start_position)
			
	def __str__(self):
		return self.result