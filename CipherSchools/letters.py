import sys

def triangle_letters(lines=6):
	'''
	lines : int: number of lines to print
	'''
	character_ascii_code = 65 # ASCII code fo 'A'
	for line  in range(1, lines):
		# Display as many characters as the line number
		for characters in range(0, line):
			print(chr(character_ascii_code), end=' ')
			character_ascii_code += 1  # increment to next character's ascii code
		print('') # Move to next line

if __name__ == "__main__":
	# lets add cmd line arguments
	if len(sys.argv) > 1:
		lines = int(sys.argv[1]) # change string to int
		triangle_letters(lines)	# to print variale number of lines using cmdline
	else:
		triangle_letters() # default value 6 will be used

