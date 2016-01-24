from pprint import pprint
import sys
from alphabet_exception import AlphabetException
from alphabet import Alphabet

def main(argv=None):
	if argv is None:
		argv = sys.argv

	try:
		try:
			input_value = argv[1]
			print >>sys.stdout, str(Alphabet(input_value))
		except IndexError:
			raise AlphabetException()
	except AlphabetException, alphabetException:
		print >>sys.stderr, alphabetException.message
		return 2

if __name__ == "__main__":
    sys.exit(main())